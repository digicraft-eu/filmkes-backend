# Running locally
## Install `uv`
- Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

(Or see docs here: https://docs.astral.sh/uv/getting-started/installation/)

## Install Python
`uv python install 3.12`

## Run project
`make dev`  
Or, if make isn't installed: `uv run fastapi dev --port 3000`