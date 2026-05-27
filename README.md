# Codex Skills Collection

[中文](#中文) | [English](#english)

## 中文

这是一个面向 Codex 的 skills 集合仓库，用来沉淀可复用的工作流、工具脚本和领域知识。每个 skill 都是独立能力，可以通过 Codex plugin marketplace 安装。

当前包含：

| Skill | 用途 |
| --- | --- |
| `organize-folders` | 扫描、分析和规划文件夹/磁盘整理方案，生成目录结构、迁移清单、归档规则和维护建议。默认只读扫描，实际移动文件前需要确认。 |

### 安装

在 Codex 中添加这个 marketplace：

```text
/plugin marketplace add bojahng/skills
```

然后在 Codex 插件界面安装 `organize-folders`。安装完成后重启 Codex，让新的 skill 生效。

### 使用示例

```text
使用 $organize-folders 帮我扫描 D 盘，生成整理建议，不要移动文件。
```

```text
使用 $organize-folders 扫描下载目录最近 7 天的新文件，并给出归档建议。
```

```text
使用 $organize-folders 为这个资料库生成迁移清单和新目录说明表。
```

### 安全原则

- 默认只读扫描，不移动、不删除、不重命名文件。
- 任何实际改动前都需要 dry-run 和用户确认。
- 默认禁止删除文件、覆盖文件、清空目录、去重删除和移动系统目录。
- 首次整理推荐使用沙盒预览模式，确认后再正式迁移。

### 仓库结构

```text
.
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── plugins/
│   └── organize-folders/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── organize-folders/
│               ├── SKILL.md
│               ├── agents/
│               ├── references/
│               └── scripts/
└── README.md
```

## English

This repository is a collection of Codex skills: reusable workflows, helper scripts, and domain-specific instructions. Each skill is packaged as an installable Codex plugin.

Included skills:

| Skill | Purpose |
| --- | --- |
| `organize-folders` | Scans, analyzes, and plans folder or drive organization. It can generate directory structures, migration plans, archive rules, and maintenance guidance. It defaults to read-only scanning and requires confirmation before moving files. |

### Installation

Add this marketplace in Codex:

```text
/plugin marketplace add bojahng/skills
```

Then install `organize-folders` from the Codex plugin UI. Restart Codex after installation so the new skill is picked up.

### Usage Examples

```text
Use $organize-folders to scan my D drive and generate organization suggestions without moving files.
```

```text
Use $organize-folders to scan files added to my Downloads folder in the last 7 days and suggest where to archive them.
```

```text
Use $organize-folders to generate a migration plan and a new directory guide for this document library.
```

### Safety Principles

- Read-only scanning by default: no moving, deleting, or renaming files unless confirmed.
- Any real change requires a dry run and explicit user confirmation.
- Deleting files, overwriting files, emptying directories, duplicate deletion, and moving system folders are disabled by default.
- First-time organization should use a sandbox preview before formal migration.

### Repository Layout

```text
.
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── plugins/
│   └── organize-folders/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── organize-folders/
│               ├── SKILL.md
│               ├── agents/
│               ├── references/
│               └── scripts/
└── README.md
```
