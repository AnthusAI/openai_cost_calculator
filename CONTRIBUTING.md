# Contributing to the Project

## Local Setup
### Pre-requisites
1. `uv` install in your local machine
2. `Python` version 3.13

### Installing Requirements
1. Fork the repository by running the command
```
git clone https://github.com/AnthusAI/openai_cost_calculator.git
```
2. Create and activate virtual environment in the root directory
```
uv venv .venv --python 3.13
source .venv/bin/activate
```
> If you are running in Windows, you can activate the virtual environment by running `.venv/scripts/Activate.ps1`
3. Install all required python dependencies 
```
uv sync --all-extras
```

## Running Tests

To ensure the reliability of the cost calculations, unit tests are provided. You can run these tests using the following command:

```bash
make test
```

For a detailed coverage report, use:

```bash
make coverage
```

This will generate a coverage report in both terminal and HTML format, allowing you to see which parts of the code are covered by tests.