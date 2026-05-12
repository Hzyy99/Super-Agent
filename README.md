# Super-Agent

This repository is a cleaned fork of DeerFlow. It keeps the runnable backend,
frontend, Docker setup, scripts, configuration examples, and skills, while
removing upstream documentation, demo content, static docs/blog pages, and
repository-maintenance files that are not needed for local development.

## What Is Kept

- `backend/`: FastAPI/LangGraph backend service.
- `frontend/`: Next.js workspace UI.
- `docker/`: Docker and compose-related runtime support.
- `scripts/`: setup, config, doctor, and service scripts.
- `skills/`: public and custom skills. This directory is intentionally kept.
- `config.example.yaml`: full application configuration template.

## Prerequisites

- Python 3.12+
- `uv`
- Node.js and `pnpm`
- Docker, if you want container-based sandboxing or Docker deployment

## Quick Start

```bash
make install
make config
make dev
```

The development server starts the backend and frontend together. Use
`make doctor` to check local configuration and required tools.

## Common Commands

```bash
make setup          # interactive setup wizard
make doctor         # diagnose local environment
make config         # generate config.yaml from config.example.yaml
make config-upgrade # merge new example config fields into config.yaml
make dev            # start local development services
make start          # start production-mode local services
make stop           # stop running services
make clean          # remove generated runtime state
```

## Docker

Docker support is intentionally preserved.

```bash
make docker-init
make docker-start
make docker-logs
make docker-stop
```

Production Docker commands:

```bash
make up
make down
```

## Configuration

Create `config.yaml` from the example:

```bash
make config
```

Then edit `config.yaml` for model providers, sandbox mode, tools, memory,
authentication, and related runtime settings. Environment examples live in
`.env.example`, `backend/.env.example`, and `frontend/.env.example` when
applicable.

## Development Notes

- The static docs/blog site and public demo data were removed.
- Nextra dependencies were removed from the frontend.
- Mock API routes for the static website demo were removed.
- `skills/` is not cleaned automatically because it is part of the retained
  runtime behavior.

## License

This fork keeps the original project license. See `LICENSE`.
