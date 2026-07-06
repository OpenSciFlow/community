# Contribution queue

OpenSciFlow needs small corrections more than broad endorsement.

Use this queue to pick focused work that can be reviewed quickly.

## Good first corrections

These are small and useful:

- Correct one project description in `awesome-ai4s-workflows`.
- Add the canonical citation for a listed project.
- Add missing license or model-weight metadata to one manifest.
- Point out one output that users may misinterpret.
- Add an HPC/Slurm requirement that is missing from a manifest or workflow.
- Suggest one narrow workflow template, with inputs and expected artifacts.

## Manifest review queue

Current priority:

| Manifest | Goal | Useful feedback |
|---|---|---|
| `mdanalysis-trajectory-analysis` | Move toward `R3 dry-run ready` | Dry-run command, package versions, report outputs |
| `gromacs-md-stability` | Improve HPC/local execution metadata | Slurm options, modules, output conventions |
| `diffdock-docking` | Keep safety boundaries precise | Model weights, output interpretation, docking non-claims |
| `proteinmpnn-sequence-design` | Improve sequence-design boundaries | Weight sources, output artifacts, design limitations |
| `mace-interatomic-potential` | Improve atomistic-model metadata | Model file provenance, applicability domain, hardware |

## Workflow review queue

Current priority:

| Workflow | Goal | Useful feedback |
|---|---|---|
| `md-stability-analysis` | First BioPilot demo workflow | Example dataset, artifact handoff, report limitations |
| `protein-ligand-stability` | Clarify non-claims | Distinguish trajectory metrics from binding evidence |
| `mutation-impact-analysis` | Tighten task boundary | Avoid claims about pathogenicity or functional proof |
| `ptm-dynamics-analysis` | Clarify input requirements | Paired structure/trajectory assumptions |
| `conformational-ensemble-generation` | Avoid overbroad generation claims | Sampling limits and validation needs |

## Public issue prompts

Good issue titles:

```text
[manifest correction] MDAnalysis output fields
[workflow review] md-stability-analysis report limitations
[hpc metadata] GROMACS Slurm requirements
[safety] DiffDock output interpretation boundary
[landscape correction] canonical citation for <project>
```

## What not to do

- Do not open broad "please collaborate" requests.
- Do not claim upstream projects have adopted OpenSciFlow.
- Do not add impressive-looking workflows without clear inputs, outputs, and limitations.
- Do not ask maintainers to integrate before the protocol is stable.
