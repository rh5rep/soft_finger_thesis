# Objective assessment of bradykinesia in Parkinson's disease using evolutionary algorithms: clinical validation

## Metadata

- Paper ID: `DOI:10.1186/s40035-018-0124-x`
- Zotero key: ``
- Topic: `T010`
- Status: `screening`
- Priority: `medium`
- Source: `manual`
- Year: `2018`
- Venue: Translational Neurodegeneration
- Authors: Chao Gao; Stephen Smith; Michael Lones; Stuart Jamieson; Jane Alty; Jie Chen; Ping Zhang; Jingjing Liu; Jianjing Du; Shuoqi Cui; Yuchen Chen; Huifang Zhou
- DOI: 10.1186/s40035-018-0124-x
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6094893/
- PDF status: `missing`
- PDF path: _not attached_
- Zotero open link: _missing_

## Why This Paper Is In The Queue

This is a strong sensor-based example of direct Parkinson finger-tapping assessment.

## Citation / Bibliographic Notes

- Title: Objective assessment of bradykinesia in Parkinson's disease using evolutionary algorithms: clinical validation
- Authors: Chao Gao; Stephen Smith; Michael Lones; Stuart Jamieson; Jane Alty; Jie Chen; Ping Zhang; Jingjing Liu; Jianjing Du; Shuoqi Cui; Yuchen Chen; Huifang Zhou
- Venue: Translational Neurodegeneration
- Year: 2018
- DOI: 10.1186/s40035-018-0124-x
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6094893/
- Tracker question: What direct sensor-based systems exist for standard Parkinson finger-tapping evaluation?

## Abstract / Summary

- This paper evaluates a direct finger-tapping assessment setup using two electromagnetic tracking sensors attached to the thumb and index finger.
- It is clinically stronger than many proof-of-concept papers because it includes a large cohort: Parkinson's disease, essential tremor, and normal controls.
- The output system, called PD-Monitor, aims to quantify bradykinesia objectively from the standard finger-tapping task.
- This is a good paper to keep because it shows that direct task instrumentation already exists with stronger clinical grounding than most exoskeleton papers.

## Model / Mechanism / Validation Details

- System type: sensor-based objective Parkinson finger-tapping assessment system
- Actuation type: none; two electromagnetic tracking sensors on thumb and index finger
- Model type: signal-analysis / evolutionary-algorithm scoring system
- Validation setup: 107 PD, 41 ET, and 49 normal controls performing a standard finger-tapping task
- Main metrics: device output score for bradykinesia severity and comparison with MDS-UPDRS finger-tapping ratings

## What Matters For This Thesis

- This paper is useful because it reminds you that the direct PD tapping literature is strongest on quantification, not exoskeleton assistance.
- It defines a sensor-based benchmark for what "direct tapping device" can mean without actuation.
- It can help justify why your hardware review must be complemented by an assessment track.

## Limitations

- It is not wearable in the exoskeleton sense and not assistive.
- The technical emphasis is on scoring bradykinesia rather than on hand-device design.
- It supports the clinical task-definition side, not the mechanism side.

## Decision Impact

- Keep as a secondary assessment-track paper.
- Use it if you want one stronger clinical-validation example beyond apps and computer vision.

## Quotes / Data To Reuse Later

- The study includes PD, essential tremor, and control cohorts, which makes it stronger than many small prototype studies.

## Next Action

Add to Zotero and extract the exact task protocol and variables used to compare against hardware-side movement measures.
