# DAT 5668 practice data

Real public business sources. No employer files. Do not paste confidential text into a public model.

| File | Source | What the agent uses |
| --- | --- | --- |
| `cfpb-credit-card-tickets.csv` | [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/) (CC0). Snapshot of credit-card tickets pulled 2026-10-27. | Session 3: walk complaint 9999983 (Chase) through agent / environment / s / a / r / s′, then the rest of the queue. |
| `fx-usd-sleeves.csv` | [Frankfurter](https://www.frankfurter.app/) daily USD rates, 2024 Q1. No auth. | Optional FX example / project data. |
| `amazon-fba-restock-daily.csv` | Built from `supermarket-sales.csv` product lines → ASIN-HOME / ASIN-ELEC / ASIN-SPORT daily totals, 2019 Q1. | Session 4: action = which ASIN gets the Amazon FBA restock-priority slot. Reward = that day's contribution. |
| `supermarket-sales.csv` | Public supermarket invoice file used in business analytics courses ([selva86/datasets](https://github.com/selva86/datasets)). Invoice-level sales, 2019. | Session 4 source for ASIN days; Session 5+: empirical daily demand for the inventory MDP. |
| `inventory_dataset_full.csv` | Course inventory desk (Electronics / Clothing / Food / Furniture / Books). | Session 8: **Electronics** Q-learning. Homework 4: **Clothing** Q-learning (same columns, new product filter). |

Session 4 loads `amazon-fba-restock-daily.csv` first, or rebuilds the same table from `supermarket-sales.csv` if needed. CFPB notebooks may try a live search API, then fall back to the course CSV.
