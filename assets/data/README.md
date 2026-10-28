# DAT 5668 practice data

Real public business sources. No employer files. Do not paste confidential text into a public model.

| File | Source | What the agent uses |
| --- | --- | --- |
| `cfpb-credit-card-tickets.csv` | [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/) (CC0). Snapshot of credit-card tickets pulled 2026-10-27. | Session 3: walk complaint 9999983 (Chase) through agent / environment / s / a / r / s′, then the rest of the queue. |
| `fx-usd-sleeves.csv` | [Frankfurter](https://www.frankfurter.app/) daily USD rates, 2024 Q1. No auth. | Session 4: action = which overnight FX sleeve (EUR, GBP, JPY). Reward = that day's return. |
| `supermarket-sales.csv` | Public supermarket invoice file used in business analytics courses ([selva86/datasets](https://github.com/selva86/datasets)). Invoice-level sales, 2019. | Session 5+: empirical daily demand for the inventory MDP. |

Class notebooks try the live API first (Frankfurter, CFPB search API), then fall back to these files so Colab still runs if a host blocks the request.
