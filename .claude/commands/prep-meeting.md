Prepare a consulting meeting brief using the full agent team.

**Topic:** $ARGUMENTS

## Workflow (execute in order):

### Phase 1: Research

Delegate to the **researcher** subagent:

- Use the consulting-research MCP tools (search_industry,
  research_company, get_tech_trends)
- Also use WebSearch and WebFetch for additional depth
- Gather: industry trends, company news, tech/AI relevance,
  competitive landscape
- Return structured findings with source URLs

### Phase 2: Synthesis

Delegate to the **analyst** subagent:

- Take the researcher's findings
- Create a meeting prep brief following the consulting-brief
  skill format EXACTLY
- Save draft to output/ directory

### Phase 3: Evaluation

Delegate to the **evaluator** subagent:

- Score the brief using the eval-brief skill rubric
- Return JSON scores and specific feedback

### Phase 4: Revision (if needed)

If evaluator scores the brief below 20/30:

- Send feedback to the **analyst** subagent
- Ask it to revise the specific weaknesses
- Re-evaluate once (max 1 revision cycle)

### Phase 5: Output

- Save the FINAL brief to output/
- Save eval results alongside
- Print summary: topic, final score, output path
