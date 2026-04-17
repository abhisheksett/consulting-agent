# Consulting Intelligence Agent (Claude Code)

An autonomous multi-agent system that generates structured consulting meeting prep briefs - researching, writing, evaluating, and revising without human intervention.

Built using Claude Code as the runtime - no API key required, runs entirely on a Claude subscription. The Claude Code version of this project. For the programmatic Agent SDK version with memory, A2A protocol, LangGraph, and CrewAI, see [consulting-agent-with-sdk](https://github.com/abhisheksett/consulting-agent-with-sdk).

---

## What It Does

Given a topic and optional client name, the agent:

1. **Researches** the topic using live web search (Tavily via custom MCP server)
2. **Writes** a structured consulting brief using a custom Skill
3. **Evaluates** the brief on a 30-point rubric
4. **Revises** automatically if score < 20 (up to 2 cycles)
5. **Saves** the final brief to `output/`

---

## Architecture

```
┌──────────────────────────────────────────┐
│         Claude Code (Orchestrator)       │
│  Reads CLAUDE.md · Discovers subagents   │
│  Loads skills · Coordinates workflow     │
└────────┬─────────────────────────────────┘
         │
    ┌────▼────┐    ┌──────────┐    ┌───────────┐
    │Researcher│    │ Analyst  │    │ Evaluator │
    │subagent  │    │ subagent │    │ subagent  │
    └────┬────┘    └──────────┘    └───────────┘
         │
    ┌────▼──────────────────┐
    │   Custom MCP Server   │
    │   (FastMCP + Tavily)  │
    │   search_industry()   │
    │   research_company()  │
    │   get_tech_trends()   │
    └───────────────────────┘
```

**How Claude Code routes to subagents:** Claude reads every file in `.claude/agents/` on startup. When a task matches a subagent's `description` field, Claude delegates automatically - no explicit routing code needed. The description field is the routing signal.

---

## Agentic Patterns Implemented

| Pattern | Where |
|---|---|
| Orchestrator-Worker | Claude Code coordinates 3 specialist subagents |
| Evaluator-Optimizer | Evaluator scores brief, orchestrator decides revise or accept |

---

## Project Structure

```
consulting-agent/
├── .claude/
│   └── agents/                        ← Subagent definitions (Claude Code convention)
│       ├── industry-researcher.md     ← Role, tools, instructions
│       ├── analyst.md
│       └── evaluator.md
├── skills/
│   ├── consulting-brief-generator/    ← How to write a consulting brief
│   │   └── SKILL.md
│   └── eval-consulting-brief/         ← How to score a brief (rubric)
│       └── SKILL.md
├── src/
│   └── (orchestration logic)
├── output/                            ← Generated briefs saved here
├── .env.example
├── CLAUDE.md                          ← Project context loaded by Claude Code every session
├── PLANNING.md
└── TASKS.md
```

---

## Subagents

| Agent | Role | Tools |
|---|---|---|
| Industry Researcher | Web research - trends, market dynamics, key players | MCP search tools, WebSearch, WebFetch |
| Analyst | Synthesizes research into structured brief using Skill | Read, Write, Bash |
| Evaluator | Scores brief on 6-criterion rubric, provides feedback | Read, Bash |

**Evaluation rubric (30 points):** executive summary, research depth, talking points, risk awareness, strategic questions, overall readiness - scored 1-5 each. Score ≥ 20 passes.

---

## Skills

Skills are portable domain knowledge files in `SKILL.md` format. Claude loads only the name and description initially (progressive disclosure) - full instructions load only when the task requires that skill.

**`consulting-brief-generator`** - defines the structure and quality standards for a consulting meeting prep brief: executive summary, key trends, talking points, risk factors, recommended questions.

**`eval-consulting-brief`** - defines the evaluation rubric. The evaluator subagent uses this to score the brief and produce specific, actionable feedback.

Skills are an open standard - they work across Claude.ai, Claude Code, and the Agent SDK.

---

## Claude Code vs Agent SDK

This repo uses Claude Code as the runtime. The key difference from the SDK version:

| | Claude Code (this repo) | Agent SDK |
|---|---|---|
| Routing | Claude decides automatically based on subagent descriptions | Your Python code decides explicitly |
| Agent definitions | `.md` files in `.claude/agents/` | `AgentDefinition` objects in Python |
| Control | Less - Claude chooses when to delegate | More - you control every step |
| API key | Not required (Claude subscription) | Required |

For the full programmatic version with memory, A2A, LangGraph, and CrewAI, see [consulting-agent-with-sdk](https://github.com/abhisheksett/consulting-agent-with-sdk).

---

## Setup

**Prerequisites:** [Claude Code](https://code.claude.com), [uv](https://docs.astral.sh/uv/)

```bash
git clone https://github.com/abhisheksett/consulting-agent
cd consulting-agent
uv sync

cp .env.example .env
# Add TAVILY_API_KEY to .env
```

## Usage

```bash
# Run via Claude Code
claude -p "Prepare a meeting prep brief on AI agents in healthcare for UnitedHealth Group"

# Or open Claude Code interactively
claude
# Then: /meeting-prep AI agents in healthcare
```

The brief is saved to `output/brief-<topic>.md`.

---

## Key Concepts Demonstrated

- **Claude Code subagents** - `.claude/agents/` convention, automatic routing via description field
- **Custom Skills** - `SKILL.md` format, progressive disclosure, portable domain knowledge
- **Custom MCP server** - FastMCP `@tool` decorator, Tavily integration
- **Eval loop** - evaluator scores output, orchestrator revises if needed

---

## Related Projects

- [consulting-agent-with-sdk](https://github.com/abhisheksett/consulting-agent-with-sdk) - Agent SDK version with memory, A2A, LangGraph, CrewAI
- [rag-explorer](https://github.com/abhisheksett/rag-explorer) - Naive vs Hybrid vs Agentic RAG comparison
