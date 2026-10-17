# Course figures

Diagrams for DAT 5668. Notebooks in `Students/`, `Teaching/`, and `Instructor/` load them with `../../assets/<file>.png`. `Students/Two-Agent-Families.md` uses `../assets/`.

The source for each figure is a Mermaid file in `mermaid/`. Redraw the PNGs with:

```
python assets/render_mermaid.py
```

That uses Mermaid CLI (`npx @mermaid-js/mermaid-cli`) at 2x on a white background. The PNG names stay the same so the notebooks do not need new links. `build_assets.py` is the older matplotlib set and does not overwrite these files unless you pass `--matplotlib`.

| File | Used in |
| --- | --- |
| `agent-loop.png` | Session 1, the two-families note |
| `two-families.png` | Sessions 1, 6, and 13 |
| `llm-tool-loop.png` | Session 2 |
| `rag-handoff.png` | Session 3 |
| `bandit.png` | Session 4 |
| `mdp-inventory.png` | Session 5 |
| `bellman.png` | Session 7 |
| `q-update.png` | Session 8 |
| `dqn.png` | Sessions 9 and 10 |
| `hybrid.png` | Session 11 |
| `scorecard.png` | Session 12 |

The old lecture decks in `Contents/` are the previous deep-RL course. Their pictures are stock art or screenshots, so they are not copied into this folder.
