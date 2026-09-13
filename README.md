# Python Foundations

A practical Python project focused on building strong Python fundamentals and learning a professional development workflow.

## Project Goals

This project covers:

- Python programming fundamentals
- CLI development
- CSV data processing
- Code refactoring
- Type hints and static type checking
- Code quality tools
- Debugging with VS Code
- Git and GitHub workflow
- Environment configuration

## Technologies

- Python 3.12
- VS Code
- Git
- GitHub
- uv
- Ruff
- Black
- Mypy
- python-dotenv



## Installation
Install the project dependencies:
Clone the repository:

```bash
git clone <repository-url>
cd python-foundations

Running the Project
uv sync

Run the CLI application:
uv run python scripts/cli.py


## Running the CLI
The CLI reads a CSV file, validates the required columns, filters the data by status, and displays a summary.
Run the CLI with:

```bash
Example:
uv run python src/main.py data.csv active

