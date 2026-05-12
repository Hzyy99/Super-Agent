# Super-Agent Backend

This package contains the backend service for the Super-Agent fork. It exposes
the API used by the frontend workspace and orchestrates LangGraph-based agent
workflows, tools, uploads, memory, sandbox execution, and integrations.

## Setup

From the repository root:

```bash
make install
make config
```

Or from this directory:

```bash
uv sync
```

## Run

The recommended local entrypoint is the root Makefile:

```bash
make dev
```

Backend-only development can be run with the scripts and commands defined in
the root `Makefile` and `scripts/` directory.

## Configuration

Runtime configuration is generated from the root `config.example.yaml` into
`config.yaml`.

```bash
make config
```

Use `make doctor` from the repository root to validate the local environment.

## Tests

```bash
uv run pytest
uv run ruff check .
```

## Notes

The large upstream backend documentation directory was removed from this fork.
Keep this README focused on commands and package metadata that are still useful
for development and packaging.
