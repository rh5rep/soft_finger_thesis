# iTex Gloves: Design and In-Home Evaluation of an E-Textile Glove System for Tele-Assessment of Parkinson's Disease

## Metadata

- Paper ID: `DOI:10.3390/s23062877`
- Zotero key: `EUEDBPW7`
- Topic: `T010`
- Status: `shortlist`
- Priority: `high`
- Source: `manual`
- Year: `2023`
- Venue: Sensors
- Authors: Vignesh Ravichandran; Shehjar Sadhu; Daniel Convey; Sebastien Guerrier; Shubham Chomal; Anne-Marie Dupre; Umer Akbar; Dhaval Solanki; Kunal Mankodiya
- DOI: 10.3390/s23062877
- URL: https://www.mdpi.com/1424-8220/23/6/2877
- PDF status: `attached`
- PDF path: /Users/rami/Zotero/storage/323H296W/Ravichandran et al. - 2023 - iTex Gloves Design and In-Home Evaluation of an E-Textile Glove System for Tele-Assessment of Parki.pdf
- Zotero open link: zotero://select/library/items/323H296W

## Audit Status

- Reading stage: quote-verified
- Source verification: checked against PDF on 2026-04-06
- Exact quotes logged: yes
- Last audited: 2026-04-06
- Used in:

## Why This Paper Is In The Queue

This is the clearest wearable assessment paper for the Parkinson finger-tapping track.

## Citation / Bibliographic Notes

- Title: iTex Gloves: Design and In-Home Evaluation of an E-Textile Glove System for Tele-Assessment of Parkinson's Disease
- Authors: Vignesh Ravichandran; Shehjar Sadhu; Daniel Convey; Sebastien Guerrier; Shubham Chomal; Anne-Marie Dupre; Umer Akbar; Dhaval Solanki; Kunal Mankodiya
- Venue: Sensors
- Year: 2023
- DOI: 10.3390/s23062877
- URL: https://pubmed.ncbi.nlm.nih.gov/36991587/
- Tracker question: What does a wearable system for remote Parkinson finger-tapping assessment actually look like?
- Local follow-up question: check whether similar e-textile concepts or materials were previously used in the lab, since that may make this paper more relevant than a generic assessment paper.

## Abstract / Summary

- This paper presents smart textile gloves for tele-assessment of Parkinson motor tasks, including finger tapping.
- It is important because it is not just a phone app or vision system; it is a wearable hand-level sensing platform that tracks fine finger movement.
- It sits very close to your thesis interests conceptually because it is hand-worn, movement-focused, and tied to clinical assessment, even though it is not an exoskeleton.
- For the review, it is probably the strongest example of a `wearable assessment device` for Parkinson finger tapping.
- The system consists of a pair of smart textile gloves connected to an embedded tablet, with flex sensors, IMUs, an onboard microcontroller, and IoT connectivity for wireless data capture.
- At the abstract level, the paper is fundamentally a data-acquisition and tele-assessment platform rather than a movement-assistance or stabilization device.
- One practically relevant result is that the system could distinguish pre-medication and post-medication cases in a majority of patients.
- The study is best understood as a small in-home feasibility and system-deployment paper rather than as a mature clinical-validation paper.

## Model / Mechanism / Validation Details

- System type: wearable e-textile glove system for Parkinson tele-assessment
- Actuation type: none; sensing and data capture only
- Model type: textile glove with embedded sensing and IoT / remote-assessment architecture
- Validation setup: in-home or remote-assessment evaluation of Parkinson movement exams including finger tapping
- Main metrics: feasibility of remote assessment, task capture quality, and movement-exam monitoring capability
- Sensor stack: one 6-DoF IMU per glove plus three flex-sensor channels focused on index finger, middle finger, and thumb-related motion
- Sensor placement: index and middle flex sensors were aligned with their bases over the knuckles; the thumb-related flex sensor was placed between the thumb and index because direct placement on the thumb produced low variation during finger tapping and closed-grip tasks
- Electronics: ESP32-based wearable unit with Wi-Fi, analog front-end using a voltage-divider circuit with 10 kohm resistor, and embedded tablet / Raspberry Pi-based IoT workflow
- Task protocol detail: for finger tapping, participants were instructed to tap the index finger on the thumb 10 times as quickly and as largely as possible
- Signal-processing implication: task windows may include idle or post-task data, so the system uses activity detection / segmentation to isolate the movement portion from the full recording window
- Signal-processing detail: for finger tapping specifically, index flexion is used as the main task signal for activity detection and kinetic feature extraction, while inertial pitch/roll are used more heavily for other movement tasks such as finger-to-nose, hand flip, hold-hands-out, and resting hands
- Feature strategy: the paper does not build one tapping-specific clinical-feature model like the 2026 npj PD paper; instead it extracts a broader engineered feature set for medication-state classification
- Finger-tapping feature family: mean frequency, max frequency, tremor-band energy, dyskinesia-band energy, power spectral density, peak-to-peak and valley-to-valley interval statistics, peak/valley amplitude statistics, RMS, and zero crossing
- Windowing detail: kinetic tasks are split into start / middle / end segments to capture changes over the task; stationary tasks are split into two sections
- Classification target: pre-medication versus post-medication state, not direct MDS-UPDRS score prediction

## What Matters For This Thesis

- This paper shows that the direct Parkinson finger-tapping literature includes serious wearable systems, but they are measurement systems rather than assistive devices.
- It helps bridge the gap between pure assessment apps and exoskeleton hardware by showing what a hand-worn assessment device looks like.
- It supports separating `wearable assessment` from `mechanical assistance`.
- It also shows that the assessment problem is not only about algorithms; sensor placement, user workflow, and home-use deployment are part of the real design problem.
- The glove captures finger tapping more directly than a wrist-only wearable because it includes finger-flexion sensing channels rather than relying on wrist IMU data alone.
- Compared with the 2026 npj PD paper, this paper is less clinically interpretable but more relevant to wearable deployment and sensing architecture.
- It is useful because it shows that a tapping-assessment system can use direct finger-flexion sensing rather than only video landmarks or wrist motion.

## Limitations

- It is not an exoskeleton and provides no actuation or stabilization.
- It is Parkinson-specific and assessment-oriented, which is narrower than the broader movement-assistance part of your review.
- It should be used to define the assessment track, not to answer the hardware-design question.
- The study is small and feasibility-oriented, so conclusions about clinical robustness should be cautious.
- Channel amplitudes should be interpreted carefully because they depend on sensor placement and finger-coupling effects, not just task relevance.
- The paper is oriented toward medication-state classification, not toward the fine-grained clinical decomposition of tapping deficits.

## Decision Impact

- Keep as one of the top 2 to 3 assessment-track papers.
- Use it to show that finger-tapping assessment can already be wearable and home-deployable, even if tapping-assist hardware is sparse.

## Exact Quotes / Evidence Bank

- Quote: "The gloves acquire the sensor data wirelessly to monitor various hand movements such as finger tapping"
- Page: 1
- Section or figure: abstract / system summary
- Why it matters: anchors the paper as a real wearable assessment system rather than only an algorithm paper.
- Reusable in: assessment-device taxonomy

- Quote: "distinguish between pre-medication and post-medication cases in a majority of the participants"
- Page: 1
- Section or figure: abstract / findings
- Why it matters: supports the claim that the system captured clinically meaningful state changes in home use.
- Reusable in: feasibility summary

- Quote: "tap the index finger on the thumb 10 times"
- Page: 7
- Section or figure: task protocol table
- Why it matters: gives the direct task instruction used for finger tapping in this glove system.
- Reusable in: task-protocol comparison

## Claims Safe To Reuse Later

- Claim: iTex Gloves is one of the strongest wearable assessment precedents in the Parkinson finger-tapping literature.
- Support: abstract/system summary p.1 and methods pp.8-11
- Confidence: high

- Claim: The paper is more valuable for deployment and sensing architecture than for clinically interpretable feature modeling.
- Support: p.1 abstract plus note summary of system design and home-use emphasis
- Confidence: medium

## Next Action

Extract the specific feature set and compare its sensing/deployment focus with the more clinically interpretable npj paper.
