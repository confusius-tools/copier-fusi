# copier-fusi

Copier template for fUSI analysis projects using [ConfUSIus](https://github.com/your-org/confusius).

## Usage

```bash
copier copy gh:sdiebolt/copier-fusi my-project
cd my-project
uv sync
uv run pre-commit install
```

## What you get

```
my-project/
├── src/my_project/
│   ├── config.py         # load_config() + CONFIG singleton
│   ├── io/               # data loading utilities
│   ├── preprocessing/    # signal preprocessing
│   └── analysis/         # analysis functions
├── scripts/
│   └── 00_example.py     # minimal script showing CONFIG import
├── results/              # gitignored output directory
├── tests/
├── config.toml           # local paths (not committed by collaborators)
├── pyproject.toml
└── justfile
```

## Updating an existing project

```bash
copier update
```

## Extending the config

Add project-specific fields to `PathsConfig` in `src/<package>/config.py` and the
corresponding keys under `[paths]` in `config.toml`. The `load_config()` function
in the same file is where you wire new fields up.
