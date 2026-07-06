# Contribution queue

OpenSciFlow needs small corrections more than broad endorsement.

Use this queue to pick focused work that can be reviewed quickly.

## Good first corrections

These are small and useful:

- Correct one project description in `awesome-ai4s-workflows`.
- Add the canonical citation for a listed project.
- Add missing license or model-weight metadata to one manifest.
- Fill one R3 dry-run evidence field for `mdanalysis-trajectory-analysis`.
- Fill one sample-data metadata field for the first BioPilot demo candidate.
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

R3 evidence template:

- https://github.com/OpenSciFlow/plugin-manifest/blob/main/docs/r3-evidence-template.md

## Workflow review queue

Current priority:

| Workflow | Goal | Useful feedback |
|---|---|---|
| `md-stability-analysis` | First BioPilot demo workflow | Example dataset, artifact handoff, report limitations |
| `protein-ligand-stability` | Clarify non-claims | Fallback-specific artifact handoff and binding-evidence boundaries |
| `mutation-impact-analysis` | Tighten task boundary | Avoid claims about pathogenicity or functional proof |
| `ptm-dynamics-analysis` | Clarify input requirements | Paired structure/trajectory assumptions |
| `conformational-ensemble-generation` | Avoid overbroad generation claims | Sampling limits and validation needs |

Artifact handoff rules:

- https://github.com/OpenSciFlow/workflow-templates/blob/main/docs/artifact-handoff-validation.md

Sample-data metadata template:

- https://github.com/OpenSciFlow/biopilot-prototype/blob/main/examples/protein-md-stability/sample-data-metadata-template.md

## Protocol review queue

Current questions for v0.2:

- Which command-template placeholders are safe enough for local execution?
- How should optional workflow branches and fallback tools declare artifacts?
- Which run-record fields are mandatory for dry runs, smoke tests, and full workflow runs?
- What model-weight checksum and license fields are mandatory before execution?
- Which local-agent refusal rules should become required behavior?

RFC outline:

- https://github.com/OpenSciFlow/docs/blob/main/reference/v0.2-rfc-outline.md

Protocol status:

- https://github.com/OpenSciFlow/docs/blob/main/reference/protocol-status.md

## Public issue prompts

Good issue titles:

```text
[manifest correction] MDAnalysis output fields
[workflow review] md-stability-analysis report limitations
[workflow validation] fallback artifact handoff for protein-ligand-stability
[hpc metadata] GROMACS Slurm requirements
[safety] DiffDock output interpretation boundary
[protocol review] v0.2 command template placeholders
[sample data] MDAnalysisData license and citation metadata
[landscape correction] canonical citation for <project>
```

## What not to do

- Do not open broad "please collaborate" requests.
- Do not claim upstream projects have adopted OpenSciFlow.
- Do not add impressive-looking workflows without clear inputs, outputs, and limitations.
- Do not ask maintainers to integrate before the protocol is stable.
