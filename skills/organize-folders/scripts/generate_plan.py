#!/usr/bin/env python3
"""根据归类建议生成整理计划，不执行任何改动。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from orglib import default_dir_names, load_json, markdown_table, now_iso, safe_filename, write_json


DEFAULT_LINK_THRESHOLD_MB = 512


def unique_target(target: Path, used: set[str]) -> Path:
    candidate = target
    index = 2
    while str(candidate).lower() in used:
        candidate = target.with_name(f"{target.stem}_{index}{target.suffix}")
        index += 1
    used.add(str(candidate).lower())
    return candidate


def should_link_in_sandbox(source: Path, threshold_bytes: int) -> bool:
    """Use links for directories and large files so previews do not duplicate data."""
    try:
        if source.is_dir():
            return True
        if source.is_file():
            return source.stat().st_size >= threshold_bytes
    except OSError:
        return False
    return False


def build_plan(classifications: dict, target_root: Path, sandbox: bool, link_threshold_mb: int = DEFAULT_LINK_THRESHOLD_MB) -> dict:
    base = target_root / "_organized_preview" if sandbox else target_root
    items: list[dict] = []
    used_targets: set[str] = set()
    link_threshold_bytes = max(0, link_threshold_mb) * 1024 * 1024

    if sandbox:
        items.append(
            {
                "action": "create_sandbox",
                "source": "",
                "target": str(base),
                "reason": "首次整理建议先创建沙盒目录预览新结构。",
                "risk": "low",
                "confidence": "high",
                "requires_confirmation": True,
            }
        )

    for dirname in default_dir_names():
        items.append(
            {
                "action": "create_dir",
                "source": "",
                "target": str(base / dirname),
                "reason": "创建默认编号英文目录结构。",
                "risk": "low",
                "confidence": "high",
                "requires_confirmation": False,
            }
        )

    for item in classifications.get("items", []):
        source = Path(item["path"])
        suggested_dir = item.get("suggested_dir", "00.inbox")
        if suggested_dir == "skip":
            action = "skip"
            target = ""
        elif item.get("requires_confirmation"):
            action = "manual-review"
            target = str(unique_target(base / suggested_dir / safe_filename(source.name), used_targets))
        else:
            action = "link" if sandbox and should_link_in_sandbox(source, link_threshold_bytes) else ("copy" if sandbox else "move")
            target_path = unique_target(base / suggested_dir / safe_filename(source.name), used_targets)
            target = str(target_path)

        items.append(
            {
                "action": action,
                "source": str(source),
                "target": target,
                "reason": item.get("reason", ""),
                "risk": item.get("risk", "medium"),
                "confidence": item.get("confidence", "low"),
                "requires_confirmation": bool(item.get("requires_confirmation") or action in {"manual-review", "copy", "link"}),
                "classification": item,
            }
        )

    return {
        "version": 1,
        "generated_at": now_iso(),
        "target_root": str(target_root),
        "sandbox": sandbox,
        "sandbox_link_threshold_mb": link_threshold_mb,
        "items": items,
    }


def to_markdown(plan: dict) -> str:
    rows = [
        [item["action"], item.get("source", ""), item.get("target", ""), item.get("risk", ""), item.get("requires_confirmation", ""), item.get("reason", "")]
        for item in plan["items"]
    ]
    return "\n".join(
        [
            "# 目录整理计划",
            "",
            f"- 生成时间：`{plan['generated_at']}`",
            f"- 目标根目录：`{plan['target_root']}`",
            f"- 沙盒模式：`{plan['sandbox']}`",
            f"- 沙盒链接阈值：`{plan.get('sandbox_link_threshold_mb', DEFAULT_LINK_THRESHOLD_MB)} MB`",
            "",
            markdown_table(["动作", "原路径", "目标路径", "风险", "需确认", "原因"], rows),
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="生成整理计划。")
    parser.add_argument("--classifications", required=True, help="classify_files.py 生成的 JSON 文件")
    parser.add_argument("--target-root", required=True, help="整理目标根目录")
    parser.add_argument("--sandbox", action="store_true", help="生成沙盒整理计划")
    parser.add_argument("--link-large-threshold-mb", type=int, default=DEFAULT_LINK_THRESHOLD_MB, help="沙盒模式下大于等于该大小的文件使用链接而不是复制；默认 512")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    parser.add_argument("--output", help="输出文件")
    args = parser.parse_args()

    classifications = load_json(args.classifications)
    plan = build_plan(classifications, Path(args.target_root).expanduser().resolve(), args.sandbox, args.link_large_threshold_mb)
    text = to_markdown(plan) if args.format == "markdown" else json.dumps(plan, ensure_ascii=False, indent=2)

    if args.output:
        if args.format == "json":
            write_json(args.output, plan)
        else:
            Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
