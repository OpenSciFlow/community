# OpenSciFlow promotion kit

Use this when introducing OpenSciFlow publicly.

## One-line description

OpenSciFlow is an early open initiative for standardizing AI for Science tool/model manifests, workflow templates, local/HPC execution metadata, and reproducible run records.

## Short description

OpenSciFlow helps scientific tools, models, and agents become easier to inspect, run, cite, validate, and reproduce. It starts with lightweight `opensciflow.yaml` plugin manifests, reusable workflow templates, and a local-first reference prototype called BioPilot.

## Chinese short description

OpenSciFlow 是一个面向 AI for Science 的早期开源倡议，目标不是再造一个万能 AI Scientist，而是先定义一层可检查、可执行、可复现的协议层。

它希望通过 `opensciflow.yaml`、workflow template 和 run record，让科研工具和模型能够被本地 Agent 安全调用、记录、引用，并在本地服务器或 HPC 环境中复现运行。

## Longer description

AI for Science is producing many useful models, toolkits, and agents, but practical lab adoption is still blocked by environment setup, model-weight provenance, hardware requirements, HPC execution, unclear citations, license ambiguity, weak run records, and scientific overclaiming.

OpenSciFlow is a lightweight open layer between scientific tools, workflow engines, model hubs, and local/HPC execution. It does not replace upstream tools. It describes how tools and models should be inspected before execution, how workflows should compose reviewed plugins, and how each run should record inputs, commands, versions, artifacts, citations, and limitations.

## Public links

- Organization: https://github.com/OpenSciFlow
- Landscape map: https://github.com/OpenSciFlow/awesome-ai4s-workflows
- Plugin manifest draft: https://github.com/OpenSciFlow/plugin-manifest
- Workflow templates: https://github.com/OpenSciFlow/workflow-templates
- Reference prototype: https://github.com/OpenSciFlow/biopilot-prototype
- White paper: https://github.com/OpenSciFlow/whitepaper
- Community/outreach: https://github.com/OpenSciFlow/community

## What to ask for

Good asks:

- Correct a project description.
- Review manifest fields.
- Point to the right citation or license.
- Tell us which outputs users commonly misinterpret.
- Suggest missing safety or limitation notes.
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
- "Generated molecules, structures, or trajectories prove biological function, binding, efficacy, or clinical meaning."

## Suggested public post

```text
We are building OpenSciFlow, an early open initiative for AI for Science workflow metadata: plugin manifests, workflow templates, local/HPC execution metadata, citations, limitations, and reproducible run records.

The current focus is not a general autonomous scientist. It is a correction-friendly protocol layer that can help local agents run only reviewed scientific tools and record what happened.

Feedback welcome, especially on manifest fields, model-weight metadata, license/citation propagation, and scientific limitation notes:
https://github.com/OpenSciFlow
```

## Suggested maintainer outreach

```text
We listed your project as a related AI for Science tool/model in OpenSciFlow. Could you check whether the description is accurate and tell us what metadata a workflow runner should record before executing or citing your tool?

This is not a request for adoption or integration. A short correction comment is enough.
```

## Current positioning

Use:

```text
early open initiative
draft protocol
correction-friendly map
local-first execution metadata
reviewed manifests
reproducible run records
```

Avoid:

```text
standard body
certified ecosystem
official integration
autonomous science platform
drug discovery system
clinical decision system
```
