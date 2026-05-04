# Search Topic Template

Use one row in `refs/SEARCH_TOPICS.csv` per recurring literature question.

## Column Guide

- `topic_id`: stable identifier such as `T001`
- `topic_name`: short label
- `priority`: `high`, `medium`, or `low`
- `keywords_any`: semicolon-separated synonyms or related phrases
- `keywords_all`: semicolon-separated anchor terms that must stay central
- `exclude_terms`: semicolon-separated drift terms to filter out
- `primary_sources`: where to search first
- `cadence`: `weekly`, `biweekly`, or `monthly`
- `last_checked`: latest manual or automated search date
- `status`: `active` or `paused`
- `notes`: search intent and guardrails

## Example

`T006,Reduced-order actuator-finger models,high,"reduced-order finger model; tendon-driven finger model; finger joint stiffness model","finger; rehabilitation","full hand; surgical planning","crossref; semantic_scholar",weekly,2026-03-19,active,"Support the first simulation abstraction decision."`
