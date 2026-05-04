# Software Stack For This Thesis

## Core Tools

### Python

Main language for:

- reusable model code
- analysis scripts
- numerical experiments

### Jupyter Notebooks

Main use:

- exploratory modeling
- quick plots
- parameter sweeps
- documenting intermediate reasoning

### Obsidian

Main use:

- meeting prep
- background notes
- working knowledge base
- literature synthesis outside the formal thesis docs

### Zotero

Main use:

- reference and PDF management
- source-of-truth bibliographic metadata

### Git

Main use:

- version control for notes, scripts, and modeling artifacts

## Python Libraries Most Likely Needed

### Immediate

- `numpy`
  - arrays, vectorized math
  - official docs: [NumPy user guide](https://numpy.org/doc/stable/user/)
- `scipy`
  - ODE solving, optimization, signal processing
  - official docs: [SciPy user guide](https://docs.scipy.org/doc/scipy-1.15.2/tutorial/index.html)
- `matplotlib`
  - plotting
  - official docs: [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- `pandas`
  - small tabular datasets, experiment summaries
  - official docs: [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)

### Likely Useful

- `sympy`
  - symbolic derivations and sanity checks
  - official docs: [SymPy intro tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html)
- `scipy.signal`
  - filtering and repeated-motion analysis
- `scipy.optimize`
  - parameter estimation

### Maybe Later

- `control`
  - if the thesis moves into transfer functions or state-space control analysis
  - docs: [python-control documentation](https://python-control.readthedocs.io/)
- `statsmodels`
  - if the statistical analysis becomes more formal

## Software Habits To Keep

- Use notebooks for exploration, but move stable functions into `.py` files when they stop changing often.
- Keep one notebook per modeling question rather than one giant notebook.
- Save figures reproducibly from code rather than manually.
- Treat Zotero as bibliography truth and the tracker as thesis triage.
- Keep meeting prep and background notes in `notes/`, not in the repo root.

## Current Repo Workflow

- thesis framing and decisions: `docs/`
- working notes and meetings: `notes/`
- references and tracker: `refs/`
- scripts: `scripts/`
- modeling notebooks: `simulation_modeling/notebooks/`
