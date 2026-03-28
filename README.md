# Consulting Intelligence Agent

Multi-agent system for generating consulting meeting prep briefs.

## Architecture

- **Orchestrator**: Coordinates 3 specialized subagents
- **Researcher**: Gathers web intelligence via custom MCP server
- **Analyst**: Synthesizes research using custom Skill format
- **Evaluator**: Scores brief quality, triggers revision if needed

## Tech Stack

| Component         | Technology                             |
| ----------------- | -------------------------------------- |
| Runtime           | Claude Agent SDK (Python)              |
| Agent definitions | Subagents (.claude/agents/)            |
| Domain knowledge  | Custom Skills (SKILL.md)               |
| External tools    | Custom MCP Server (FastMCP + Tavily)   |
| Built-in tools    | Read, Write, Bash, WebSearch, WebFetch |
| Eval              | Evaluator subagent with scoring rubric |
