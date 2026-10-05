---
id: nextflow-gtf-download-01
title: Nextflow process that downloads a GTF
status: draft
target_files:
  - modules/gtf_download.nf
---

<!--
  BLANK BRIEF — fill this in at the start of Part 4. Its output becomes the
  input to GTF_GENES (briefs/nextflow-gtf-genes-01.md), so fill the two
  briefs in side by side.

  NOTE: there are no in-repo tests for this brief. Verification is
  either manual review of the process or running it outside this repo.
  Whichever you use, record it and its result in the log entry.

  Resolve each prompt into a declarative Requirements bullet, same as you
  did for the Python briefs. Delete these prompts once done.
-->

## Context
One or two sentences: what this process downloads, from where, and what
uses its output.

## Inputs / Outputs
Process `GTF_DOWNLOAD` in `modules/gtf_download.nf`. You are deciding
these, not just filling them in:

- **Inputs:** *(a full URL? or a species and release number that the
  process turns into a URL?)*
- **Outputs:** *(the GTF file: what is it called, and is it still gzipped
  or decompressed?)*

## Requirements

- *(your resolved requirements go here, one decision per line)*

## Out of Scope / Constraints
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
