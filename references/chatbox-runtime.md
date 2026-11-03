# Chatbox runtime guidance

## Scope and precedence
This is a compatibility adapter for the unchanged Open Dataset Project Builder workflow, not a new research workflow. Preserve all 11 stages, scientific safeguards, provenance rules, output contracts and execution statuses. References to a plugin archive in the original workflow describe source packaging; installing this skill does not itself provide execution or network access. The archival files under `original-plugin/` are provenance only; do not load or execute them as a second skill.

## Discover capabilities rather than assuming them
Chatbox can use different models and tool configurations. Inspect the tools actually exposed in the active conversation. Tool names below are conditional examples, not guaranteed interfaces. A model provider alone does not ensure tools are enabled. Do not fabricate unavailable tools, execute an instruction by merely printing it, or describe a planned analysis as completed.

| Original capability | Chatbox mapping when available | If missing |
|---|---|---|
| Literature and dataset discovery | Enabled web-search/browsing tools or configured scholarly/repository MCP tools | Ask for source links/files or label discovery blocked |
| Read and verify provider pages/licences | Fetch/browser tools with actual page content | Do not infer permission from a search snippet |
| Download datasets | Enabled download tool or permitted network commands in an execution tool | Supply verified retrieval instructions; never claim a download |
| Inspect/create project files | `list_files`, `read_file`, `search_files`, `write_file`, `edit_file`, or equivalent | Mark filesystem deliverables blocked |
| Run Python/R, checksums, analyses and tests | `run_command` or an enabled execution tool, after inspecting installed runtimes and dependencies | Mark affected execution/validation blocked |
| Inspect figures | `view_image` or an enabled image-viewing tool | Disclose that visual inspection was not performed |
| Deliver project/report/archive | Create actual files, then call `create_download` if exposed | Never invent a clickable filesystem/sandbox link; explain delivery limitation |

The presence of a parsing MCP server does not imply general Python or R execution. Remote MCP filesystem paths may belong to a different host; do not assume a remotely downloaded file is accessible to local code. Verify access or use an authorised transfer route.

## Files, dependencies and permissions
Use a user-approved project directory, otherwise the host-provided sandbox. Resolve bundled resources relative to this skill's installed directory; the project working directory may be different. Prefer narrow file tools for edits and shell execution for calculations or pipeline runs. Do not hard-code this installation's personal paths. Respect Chatbox's approval and sandbox policies. Only retry outside the sandbox through the host's explicit supported process after a real eligible failure; never expand permissions silently.

Check Python/R versions and required libraries before selecting an executable method. The bundled Python validator uses only the standard library and requires Python 3.10 or newer because it uses union type annotations and pathlib APIs. Do not install packages, change the user's environment, publish files externally, or install other skills without the approval required by the host/user. A downloadable attachment in the conversation is not authorisation to publish to a public hosting service.

## Bundled validator and tests
Use actual installed skill paths rather than assuming project scripts and skill scripts share a directory:

```bash
python3 "<installed-skill-directory>/scripts/validate_project.py" "<actual-project-directory>"
python3 -m unittest discover -s "<installed-skill-directory>/tests" -p 'test_validate_project.py' -v
```

Replace the angle-bracket values with verified paths before running. Save validator output and distinguish structural/checksum validation from scientific validation. The existing five tests cover a valid structure, checksum mismatch, missing report, duplicate reports and path traversal. They do not establish that a scientific analysis or model is correct.

## Reporting and delivery
Continue to use the original execution ledger and COMPLETE / PARTIAL / BLOCKED / DESIGN ONLY classifications. Preserve one canonical final report, all required supporting files, and lawful data redistribution rules. For unavailable browsing, execution, statistical libraries or attachment tools, report the exact limitation and complete only supported work. With `create_download`, delivery is successful only after that tool confirms persistence. Do not present raw sandbox paths as download links.

## Interface metadata
The original plugin name, author, description, icon, capabilities and starter prompts are preserved in `original-plugin/.codex-plugin/plugin.json` and `original-plugin/assets/icon.svg`. Chatbox skill discovery uses the root SKILL.md name and description. A skill package cannot force Chatbox to render plugin-specific icons, categories or clickable composer prompts. This UI difference does not remove the underlying workflow.
