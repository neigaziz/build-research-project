# Open Dataset Project Builder — Chatbox skill

A minimal compatibility conversion of the supplied ChatGPT/Codex plugin. All 11 research stages remain intact. Existing references, executable Python validator and its five tests are unchanged. The complete original plugin is retained byte-for-byte under `original-plugin/` (excluding macOS metadata).

## Installation
This archive contains one root skill folder, `build-research-project`, with SKILL.md directly inside it. Extract it and use Chatbox's supported local-skill import/installation mechanism if provided by your version. In a Chatbox agent session exposing `install_skill`, ask the agent to install the extracted folder; the agent must use a permitted staging location and request approval. UI labels vary by Chatbox version; no specific unverified menu sequence is assumed. This archive is a skill package, not a .codex-plugin plugin.

If a skill named `build-research-project` already exists, do not silently overwrite it. Review the installed version and choose an explicit replacement/migration path first.

## Activation
Start a new conversation after installation if necessary so the skill catalogue refreshes. Ask: “Use the build-research-project skill to build a complete reproducible research project using openly accessible datasets for [question].” The agent should load this skill before following its workflow. Installation and activation are separate from demonstrating an actual executed scientific project.

## Tool requirements
Enable the available search/fetch tools, file tools and code execution appropriate to the intended work. Python/R and statistical packages are runtime dependencies, not bundled software. The structural validator needs Python >=3.10 and no third-party libraries. The skill does not provide new credentials, external services, general execution access, data or statistical packages. Read `references/chatbox-runtime.md` for conditional tool mappings and blocked-stage behaviour.

## Original starter prompts
- Build a complete research project using suitable free and open datasets for this question: [describe your question].
- Find an evidence-based research gap, select public datasets and run a reproducible analysis of [topic].
- Audit my proposed dataset and research question, then create a validated, reproducible analysis project.

## What changed
Only one platform name in the original SKILL.md was changed, from “active ChatGPT session” to “active Chatbox session”; an additive runtime-adapter link was inserted. No original workflow sections were removed, shortened or split. See `conversion.diff` for the exact changes. New runtime guidance explains Chatbox tools, delivery, permissions and dependency checks without replacing the original capability contract.

## Preserved metadata and limitations
The original icon, author, descriptions, category, capability list and starter prompts remain in `original-plugin/`. Plugin-specific interface rendering is controlled by Chatbox and is not supplied by a skill. Equivalent runtime tools are required for equivalent execution; model output and scientific results cannot be guaranteed identical across providers. Original third-party data licensing and authorship rules remain applicable; this conversion does not grant a new licence for source materials.

## Validation scope
`tests/test_validate_project.py` contains the unchanged original validator tests. Build-time parity tests were run separately against the original source directory. `FILE_MANIFEST.json` records SHA-256 and byte size for packaged files other than itself. Successful static checks do not prove live skill activation, dataset retrieval or scientific correctness.
