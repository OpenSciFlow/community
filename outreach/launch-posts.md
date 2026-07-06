# Launch posts

These are deliberately plain. OpenSciFlow should sound like an early public project asking for review, not a finished AI platform.

## LinkedIn / GitHub Discussion

```text
I am working on OpenSciFlow, an early open initiative around AI for Science workflow metadata.

The starting point is small:

- a curated map of related AI for Science tools and workflow systems
- a draft plugin manifest for scientific tools and models
- reusable workflow templates
- a local-first reference prototype plan for protein MD analysis

The goal is not to build a general "AI scientist". The near-term goal is more modest: make scientific tools easier to inspect before execution, easier to cite, and easier to reproduce afterwards.

Feedback is useful, especially on manifest fields, model-weight metadata, citation/license propagation, local/HPC execution assumptions, and scientific limitation notes.

GitHub: https://github.com/OpenSciFlow
```

## 中文公开帖

```text
我最近在做 OpenSciFlow，一个很早期的 AI for Science 开源项目。

它不是“全自动科学家”，也不是想替代现有科研软件。

我想先解决一个更小的问题：现在科研模型、工具和工作流越来越多，但真正跑起来的时候，经常卡在环境、权重来源、许可证、引用、HPC、日志、结果归档和复现这些细节上。

所以 OpenSciFlow 先做三件事：

1. 用 `opensciflow.yaml` 描述一个工具或模型该怎么被检查和调用。
2. 用 workflow template 描述一个科研任务的固定步骤，而不是让 Agent 自由发挥。
3. 用 run record 记录一次运行到底发生了什么。

项目还很早期，最需要的是挑错：

- 哪些字段不合理？
- 哪些模型/工具应该优先支持？
- 本地 Agent 在执行科研命令前应该检查什么？
- 哪些结果最容易被误读？

GitHub: https://github.com/OpenSciFlow
```

## Xiaohongshu caption

```text
我最近在做一个很小、但可能有用的开源项目：OpenSciFlow。

不是再做一个“自动科学家”，也不是说现在就能替代科研软件。

我想先解决一个很具体的问题：
AI for Science 的模型和工具越来越多，但真正想在本地电脑、服务器或 HPC 上跑起来，经常卡在环境、权重来源、许可证、引用、日志、结果归档这些细节。

所以我先做三类标准化文件：

1. opensciflow.yaml
让一个模型/工具在运行前把输入、输出、环境、权重、引用、限制说清楚。

2. workflow template
把一个科研任务拆成可检查的步骤，而不是让 Agent 自由发挥。

3. run record
记录这次到底跑了什么命令、用了什么版本、生成了哪些文件、哪些结论不能乱说。

现在项目还很早期，最需要的不是夸奖，而是挑错。

GitHub 搜：OpenSciFlow
```

## Short reply when someone asks "what is this for?"

```text
It is a small protocol layer for AI for Science workflows: describe tools, constrain local agents, record runs, and carry citations/limitations forward.
```

## Avoid

- Do not say OpenSciFlow already has partners.
- Do not say it validates scientific correctness.
- Do not say it can autonomously complete scientific research.
- Do not lead with "revolution", "颠覆", "闭环生态", "全自动科研", or "AI scientist platform".
