# CLAUDE.md

## Security rule: scan before installing skills or plugins

Before installing **any** new skill or plugin (Claude Code skill, plugin, MCP server, or agent skill from any source), always:

1. Run a SkillSpector scan on it first:
   ```bash
   skillspector scan <path-or-git-url>
   ```
   SkillSpector (NVIDIA) is installed via `uv tool install` and uses `SKILLSPECTOR_PROVIDER=claude_cli`, so it authenticates through the existing `claude` CLI session — no API key needed.
2. Read the resulting risk rating.
3. **Do not install** if the rating is **HIGH** or **CRITICAL**. Report the findings to the user instead and stop.
4. Only proceed with installation when the rating is below HIGH (e.g. LOW/MEDIUM/none), and mention the scan result to the user.

This rule is permanent and applies to every session in this repository.
