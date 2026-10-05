---
id: nextflow-gtf-genes-01
title: Nextflow process wrapping the GTF gene parser
status: draft
target_files:
  - modules/gtf_genes.nf
---

<!--
  BLANK BRIEF — fill this in after gtf-genes-01 (Part 3) is implemented and
  you've checked it works. Do not start this until that function's logic is
  verified; any failure you hit here should be about Nextflow wrapping, not
  about the underlying parser.

  NOTE: there are no in-repo tests for this brief. Verification is
  either manual review of the process or running it outside this repo.
  Whichever you use, record it and its result in the log entry.

  Resolve each prompt into a declarative Requirements bullet, same as you
  did for the Python brief. Delete these prompts once done.
-->

## Context
One or two sentences: what this process does, and that it wraps the
already-verified `gtf_genes` function from `gtf-genes-01`.

## Inputs / Outputs
Process `GTF_GENES` in `modules/gtf_genes.nf`, which calls into
`src/gtf_genes.py`. You are deciding these, not just filling them in:

- **Inputs:** *(what comes in? a path to a GTF? a tuple with a name or
  genome build attached?)*
- **Outputs:** *(what goes out? a TSV of gene_id and gene_name? what is
  it called, and does it have a header row?)*

## Requirements

- *(your resolved requirements go here, one decision per line)*

## Out of Scope / Constraints
- Do not modify `src/gtf_genes.py` or `gtf-genes-01`'s log.
- Do not modify any file outside `target_files`.
- *(add anything else you're deliberately excluding)*

## Acceptance Criteria
- The process has been verified by manual review or by running it outside
  this repo, and the log entry says which method was used.

## Definition of Done
- The log entry records how the process was verified and the result.
- No files outside `target_files` were modified.
- No TODOs, commented-out code, or unused parameters.

## Fix
*(left blank at brief time — filled in only for post-commit discoveries)*
