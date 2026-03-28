# Consulting Intelligence Agent

## Overview

Multi-agent system: Orchestrator + 3 subagents (Researcher, Analyst, Evaluator).
Uses custom Skills and MCP server for consulting meeting prep briefs.

## Architecture

- Main agent orchestrates workflow via Claude Agent SDK
- Researcher subagent: gathers web intelligence via MCP tools
- Analyst subagent: synthesizes into brief using consulting-brief skill
- Evaluator subagent: scores brief, triggers revision if needed

## Tech Stack

- Claude Agent SDK (Python), Custom MCP server (FastMCP/Tavily)
- Custom Skills: consulting-brief, eval-brief
- Subagents defined in .claude/agents/

## Key Files

- src/mcp_server.py — MCP server with research tools
- src/agent.py — Main orchestrator agent
- .claude/agents/researcher.md — Researcher subagent definition
- .claude/agents/analyst.md — Analyst subagent definition
- .claude/agents/evaluator.md — Evaluator subagent definition
- skills/consulting-brief/SKILL.md — Brief format skill
- skills/eval-brief/SKILL.md — Evaluation criteria skill
