# OpenSciFlow Promotion Kit

Use this when introducing OpenSciFlow publicly.

## One-line description

OpenSciFlow is an early open initiative for building verified execution capsules for AI for Science tools.

## Short description

OpenSciFlow does not promise that scientific tools will run everywhere. It makes tool requirements, environment assumptions, verification status, run records, and known failures explicit and machine-readable.

Core phrase:

```text
Not write once, run anywhere.
Write once, check before run, record after run.
```

## Chinese short description

OpenSciFlow 是一个面向 AI for Science 的早期开源倡议，目标是为科研工具构建 verified execution capsule。

它不保证科研工具到处都能运行，而是把工具依赖、环境假设、验证状态、运行记录和失败边界变得显式、结构化、可检查。

更简单地说：

```text
不是“一次描述，到处运行”。
而是“一次描述，运行前可检查，运行后可记录”。
```

## Longer description

AI for Science is producing many useful models, toolkits, and agents, but practical adoption is still blocked by environment setup, model-weight provenance, hardware requirements, HPC execution, unclear citations, license ambiguity, weak run records, and scientific overclaiming.

OpenSciFlow is a lightweight open layer for check-before-run and record-after-run scientific tool execution. It does not replace upstream tools. It packages execution-facing evidence into verified execution capsules: manifests, environment specs, reviewed command templates, smoke tests, run records, verified environment matrices, and known failure records.

## Public links

- Organization: https://github.com/OpenSciFlow
- Verified capsules: https://github.com/OpenSciFlow/verified-capsules
- Landscape map: https://github.com/OpenSciFlow/awesome-ai4s-workflows
- Plugin manifest draft: https://github.com/OpenSciFlow/plugin-manifest
- Workflow templates: https://github.com/OpenSciFlow/workflow-templates
- Reference prototype: https://github.com/OpenSciFlow/biopilot-prototype
- White paper: https://github.com/OpenSciFlow/whitepaper
- Community/outreach: https://github.com/OpenSciFlow/community

## What to ask for

Good asks:

- Correct a project description.
- Review capsule or manifest fields.
- Point to the right citation or license.
- Tell us which outputs users commonly misinterpret.
- Suggest missing safety or limitation notes.
- Suggest smoke tests or known failure cases.
- Suggest required metadata before a model/tool is executed.

Bad asks:

- Asking maintainers to adopt OpenSciFlow immediately.
- Claiming partnership.
- Asking maintainers to integrate with our tooling before the protocol is stable.
- Presenting OpenSciFlow as mature infrastructure.

## Do not say

- "OpenSciFlow partners with X" unless X explicitly agrees.
- "OpenSciFlow validates scientific correctness."
- "OpenSciFlow can autonomously do science."
- "OpenSciFlow makes scientific tools run everywhere."
- "Generated molecules, structures, or trajectories prove biological function, binding, efficacy, or clinical meaning."

## Suggested public post

```text
We are building OpenSciFlow, an early open initiative for AI for Science verified execution capsules.

The current focus is not a general autonomous scientist and not a run-anywhere promise. It is a correction-friendly protocol layer for checking scientific tool requirements before execution and recording what happened after execution.

Feedback welcome, especially on capsule fields, smoke tests, known failures, model-weight metadata, license/citation propagation, and scientific limitation notes:
https://github.com/OpenSciFlow
```

## Suggested maintainer outreach

```text
We listed your project as a related AI for Science tool/model in OpenSciFlow. Could you check whether the description is accurate and tell us what metadata, smoke tests, or known failure cases a local agent should check before executing or citing your tool?

This is not a request for adoption or integration. A short correction comment is enough.
```

## Current positioning

Use:

```text
early open initiative
draft protocol
correction-friendly map
verified execution capsule
check-before-run
record-after-run
reviewed command templates
bounded run records
known failure records
```

Avoid:

```text
standard body
certified ecosystem
official integration
autonomous science platform
run-anywhere system
drug discovery system
clinical decision system
```
