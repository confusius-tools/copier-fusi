# copier-fusi

Copier template for fUSI analysis projects using [ConfUSIus](https://github.com/confusius-tools/confusius).

## Usage

```bash
uvx copier copy gh:sdiebolt/copier-fusi my-project
cd my-project
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
├── config.toml           # local paths (not committed by collaborators)
├── pyproject.toml
└── justfile
```

If `include_docs=true`, the generated project also includes:

```
docs/
zensical.toml
```

## Updating an existing project

```bash
uvx copier update
```

## Extending the config

Add project-specific fields to `PathsConfig` in `src/<package>/config.py` and the
corresponding keys under `[paths]` in `config.toml`. The `load_config()` function in the
same file is where you wire new fields up.

## Documentation

If you generate the project with `include_docs=true`, it comes with a minimal
[Zensical](https://pypi.org/project/zensical/) setup and a `docs/` directory.
