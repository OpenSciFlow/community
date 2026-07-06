# Xiaohongshu post draft

Use this as a more personal, less polished launch note for Xiaohongshu.

## Caption

```text
我把 OpenSciFlow 的第一版 GitHub 组织建起来了。

它不是一个成熟平台，也不是一个万能 AI Scientist。
更准确地说，它是一个很早期的 AI for Science 本地 Agent 开放协议草案。

我想解决的问题是：

现在 AI for Science 模型和工具越来越多，但真正跑起来仍然很痛苦：
环境装不上，模型权重和版本说不清，GPU/HPC 要求不透明，license/citation 容易漏，跑完之后结果也很难复现。

所以 OpenSciFlow 先不做“自动发现科学真理”。
我们先做更底层的一件事：

让科学模型和工具能被 Agent 安全调用、完整记录、本地复现。

目前开源了几部分：

1. plugin-manifest
设计 `opensciflow.yaml` 草案，让每个模型/工具声明自己的输入、输出、环境、权重、许可证、引用和硬件要求。

2. workflow-templates
从蛋白质计算工作流开始，整理可复用 workflow template。

3. awesome-ai4s-workflows
整理 79+ 个 AI for Science agents、workflow engines、model hubs、HPC/local execution 和 reproducibility 相关项目。

4. biopilot-prototype
作为第一个本地蛋白质计算 workflow reference prototype。

5. local agent contract
规定本地 Agent 不能随便执行 LLM 生成的 shell 命令，只能执行 manifest 里审阅过的命令模板，并记录 run record。

目前我们最需要的不是点赞，而是纠错：

协议字段够不够？
哪些模型/工具应该优先支持？
HPC / Slurm 还缺哪些字段？
本地 Agent 权限应该怎么限制？
哪些结果最容易被用户误解？

如果你做计算生物、分子模拟、蛋白设计、材料模型、HPC、科学工作流或开源工具维护，欢迎来 GitHub 提 issue。

GitHub 搜：OpenSciFlow

先求被纠错，再求被使用。
```

## Hashtags

```text
#AIforScience #开源项目 #科研工具 #本地Agent #计算生物学 #分子模拟 #蛋白设计 #HPC #GitHub
```

## Avoid

- Do not say OpenSciFlow already has partners.
- Do not say it validates scientific correctness.
- Do not say it can autonomously complete scientific research.
- Do not lead with "revolution", "颠覆", "闭环生态", or "全自动科研".
