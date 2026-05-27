# Agent Skills Collection

[中文](#中文) | [English](#english)

## 中文

这是一个面向常见 AI Agent 的 skills 集合仓库，用来沉淀可复用的工作流、工具脚本和领域知识。每个 skill 都是独立能力，核心内容遵循通用 `SKILL.md` 结构；同时也提供 Codex plugin marketplace 元数据，方便在 Codex 中一键安装。

当前包含：

| Skill | 用途 |
| --- | --- |
| `organize-folders` | 扫描、分析和规划文件夹/磁盘整理方案，生成目录结构、迁移清单、归档规则和维护建议。默认只读扫描，实际移动文件前需要确认。 |

### 支持的 Agent

这个仓库面向支持 `SKILL.md` / Agent Skills 目录结构的工具使用，包括 Codex、Claude 兼容技能环境、Eloquen 等多 Agent 场景，以及支持 GitHub skill 安装的通用 skills CLI。

### 安装

Codex plugin marketplace：

```text
/plugin marketplace add bojahng/skills
```

然后在 Codex 插件界面安装 `organize-folders`。安装完成后重启 Codex，让新的 skill 生效。

通用 skills CLI：

```text
npx skills add bojahng/skills --skill organize-folders
```

如果 CLI 不能识别 marketplace 仓库结构，可以使用 skill 目录的 GitHub 路径：

```text
npx skills add https://github.com/bojahng/skills/tree/main/plugins/organize-folders/skills/organize-folders
```

手动安装：

```text
复制 plugins/organize-folders/skills/organize-folders 到你的 agent skills 目录。
```

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

- 这个 skill 的核心设计是“先分析，再确认，再执行”。
- 默认只读扫描，不移动、不删除、不重命名文件。
- 任何实际改动前都需要 dry-run 和用户确认。
- 默认禁止删除文件、覆盖文件、清空目录、去重删除和移动系统目录。
- 首次整理推荐使用沙盒预览模式，确认后再正式迁移。

### 发现与收录

这个仓库适合被 skills marketplace、GitHub 聚合索引和通用 skills CLI 收录。推荐的 GitHub topics：

```text
codex
claude
eloquen
agent-skills
skill-md
claude-skills
ai-agents
productivity
file-organization
```

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
├── LICENSE
└── README.md
```

## English

This repository is a collection of skills for common AI agents: reusable workflows, helper scripts, and domain-specific instructions. Each skill follows the general `SKILL.md` directory pattern, and the repository also includes Codex plugin marketplace metadata for one-click installation in Codex.

Included skills:

| Skill | Purpose |
| --- | --- |
| `organize-folders` | Scans, analyzes, and plans folder or drive organization. It can generate directory structures, migration plans, archive rules, and maintenance guidance. It defaults to read-only scanning and requires confirmation before moving files. |

### Supported Agents

This repository is intended for tools that support `SKILL.md` / Agent Skills directory structures, including Codex, Claude-compatible skill environments, Eloquen-style agents, multi-agent setups, and generic skills CLIs that install from GitHub.

### Installation

Codex plugin marketplace:

```text
/plugin marketplace add bojahng/skills
```

Then install `organize-folders` from the Codex plugin UI. Restart Codex after installation so the new skill is picked up.

Generic skills CLI:

```text
npx skills add bojahng/skills --skill organize-folders
```

If the CLI does not recognize the marketplace repository layout, use the GitHub path to the skill directory:

```text
npx skills add https://github.com/bojahng/skills/tree/main/plugins/organize-folders/skills/organize-folders
```

Manual install:

```text
Copy plugins/organize-folders/skills/organize-folders into your agent skills directory.
```

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

- This skill is designed around "analyze first, confirm next, execute last".
- Read-only scanning by default: no moving, deleting, or renaming files unless confirmed.
- Any real change requires a dry run and explicit user confirmation.
- Deleting files, overwriting files, emptying directories, duplicate deletion, and moving system folders are disabled by default.
- First-time organization should use a sandbox preview before formal migration.

### Discovery

This repository is designed to be indexed by skills marketplaces, GitHub-based skill catalogs, and generic skills CLIs. Recommended GitHub topics:

```text
codex
claude
eloquen
agent-skills
skill-md
claude-skills
ai-agents
productivity
file-organization
```

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
├── LICENSE
└── README.md
```
