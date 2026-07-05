# First outreach wave

Goal: ask for correction and focused feedback, not partnership.

## Message framing

Use this framing:

> We listed your project as a related project in an early AI for Science workflow landscape. Could you check whether the description is accurate and tell us what metadata a workflow system should record before running or citing your tool?

Avoid:

- claiming partnership;
- asking maintainers to join an ecosystem immediately;
- implying OpenSciFlow replaces their project;
- sending a broad marketing pitch.

## Priority 1 targets

| Target | Why contact | Ask |
|---|---|---|
| BioBB | Closest match to biomolecular workflow building blocks | Review protein workflow template fields and manifest assumptions |
| BioSimSpace | Molecular simulation interoperability | Review simulation plugin/workflow metadata |
| MDAnalysis | Core MVP analysis dependency | Review trajectory-analysis manifest and report outputs |
| OpenMM | Python-friendly simulation toolkit | Review local execution/environment fields |
| Nextflow | Mature workflow engine | Comment on how OpenSciFlow should interoperate rather than duplicate |
| Snakemake | Mature workflow engine | Comment on workflow-template boundaries and environment metadata |
| Galaxy | Mature biomedical workflow platform | Comment on UX/reproducibility fields |
| AiiDA | Provenance-focused workflow system | Comment on run metadata and provenance gaps |
| BioImage Model Zoo | Strong manifest precedent | Comment on model/tool metadata design |
| DiffDock | Example AI docking model | Review model weights, GPU, and license fields |
| ChemCrow | Science-agent precedent | Comment on tool-use metadata and agent boundaries |
| Biomni | Biomedical agent project | Comment on biomedical task/plugin interoperability |

## First-wave checklist

1. Open a small initial batch of correction-request issues/discussions before scaling up.
2. Track each outreach in a table with date, target, channel, status, and response.
3. If maintainers correct a description, update `awesome-ai4s-workflows` quickly.
4. If a maintainer objects to inclusion, revise or remove the entry immediately.
5. Summarize accepted corrections in the first monthly update.

## Tracking table

| Date | Target | Channel | Link | Status | Notes |
|---|---|---|---|---|---|
| 2026-07-05 | BioBB | GitHub issue | https://github.com/bioexcel/biobb/issues/25 | sent | Asked for biomolecular workflow feedback |
| 2026-07-05 | BioSimSpace | GitHub issue | https://github.com/OpenBioSim/biosimspace/issues/526 | sent | Asked for simulation interoperability feedback |
| 2026-07-05 | MDAnalysis | GitHub discussion | https://github.com/MDAnalysis/mdanalysis/discussions/5417 | sent | Asked for trajectory-analysis feedback; follow-up added with manifest link |
| 2026-07-05 | OpenMM | GitHub discussion | https://github.com/openmm/openmm/discussions/5333 | sent | Asked for local execution/environment feedback |
| TBD | Nextflow | GitHub/discussion | TBD | planned | Ask for interop boundary feedback |
| TBD | Snakemake | GitHub/discussion | TBD | planned | Ask for template/environment feedback |
| TBD | Galaxy | GitHub/community | TBD | planned | Ask for reproducibility/UX feedback |
| TBD | AiiDA | GitHub/community | TBD | planned | Ask for provenance feedback |
| 2026-07-05 | BioImage Model Zoo | GitHub discussion | https://github.com/bioimage-io/spec-bioimage-io/discussions/763 | sent | Asked for metadata design feedback |
| TBD | DiffDock | GitHub issue/discussion | TBD | planned | Deferred until a concrete DiffDock plugin manifest draft exists |
| 2026-07-05 | ChemCrow | GitHub issue | https://github.com/ur-whitelab/chemcrow-public/issues/61 | sent | Asked for agent/tool metadata feedback |
| 2026-07-05 | Biomni | GitHub issue | https://github.com/snap-stanford/Biomni/issues/305 | sent | Asked for biomedical-agent interoperability feedback |
