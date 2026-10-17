# Course figures

Diagrams for DAT 5668. Notebooks in `Students/`, `Teaching/`, and `Instructor/` load them with `../../assets/<file>.png`. `Students/Two-Agent-Families.md` uses `../assets/`.

The source for each figure is a Mermaid file in `mermaid/`. Redraw the PNGs with:

```
python assets/render_mermaid.py
```

That uses Mermaid CLI (`npx @mermaid-js/mermaid-cli`) at 2x on a white background. The PNG names stay the same so the notebooks do not need new links. `build_assets.py` is the older matplotlib set and does not overwrite these files unless you pass `--matplotlib`.

| File | Used in |
| --- | --- |
| `agent-loop.png` | Week 1 Monday, the two-families note |
| `two-families.png` | Week 1 Monday, Week 3 Wednesday, Week 7 |
| `llm-tool-loop.png` | Week 1 Wednesday |
| `rag-handoff.png` | Week 2 Monday |
| `bandit.png` | Week 2 Wednesday |
| `mdp-inventory.png` | Week 3 Monday |
| `bellman.png` | Week 4 Monday |
| `q-update.png` | Week 4 Wednesday |
| `dqn.png` | Week 5 Monday and Wednesday |
| `hybrid.png` | Week 6 Monday |
| `scorecard.png` | Week 6 Wednesday |

The old lecture decks in `Contents/` are the previous deep-RL course. Their pictures are stock art or screenshots, so they are not copied into this folder.
