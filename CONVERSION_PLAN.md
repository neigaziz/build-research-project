# Chatbox-compatible Open Dataset Project Builder

## Approved design
Preserve the existing single-skill architecture, full SKILL.md workflow, all supporting documents, Python validator and tests. Keep the source plugin untouched. Add only a linked Chatbox runtime adapter and replace the one execution-context reference to ChatGPT with Chatbox. Include a byte-identical original-plugin snapshot, including metadata and icon, for provenance. Package one skill-root folder as ZIP. Do not install until the user approves installation separately.

## Implementation plan
1. Write and run failing package tests for root metadata, exact workflow preservation, unchanged references/scripts/tests, local links, and original-plugin snapshot.
2. Build the conversion from the actual source files without rewriting scientific instructions; add Chatbox runtime guidance and README with original starter prompts.
3. Run package regression checks and the existing five validator tests. Inspect archive paths and exclude .DS_Store and __pycache__.
4. Record exact file checksums, adaptation diff and test evidence. Deliver ZIP via create_download.
5. Ask for approval immediately before using Chatbox install_skill; if approved, verify load_skill activation. Runtime analysis is not claimed merely from installation or tests.

## Acceptance boundaries
All 11 stages and all existing safeguards must survive verbatim except the named execution-context replacement and the additive adapter link. Tool availability remains conditional. Plugin UI decoration is retained as assets/metadata, not promised as Chatbox UI support. No unrelated refactoring, new MCP service, or shortened instructions.
