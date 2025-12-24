# Elastic Detection as Code CI Pipeline

This repository provides a skeleton for managing Elastic Detection Rules as code.

## Directory Structure

- `rules/`: Contains detection rules in JSON format.
- `scripts/`: Automation scripts for validation and deployment.
- `tests/`: Unit tests for automation logic.
- `.github/workflows/`: CI/CD pipeline definitions.

## Getting Started

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure Credentials**:
    Set your Kibana URL and API key as environment variables:
    ```bash
    # Linux/macOS
    export KIBANA_URL="https://your-kibana-url"
    export KIBANA_API_KEY="your-api-key"

    # Windows (PowerShell)
    $env:KIBANA_URL="https://your-kibana-url"
    $env:KIBANA_API_KEY="your-api-key"
    ```
3.  **Add a Rule**:
    Place your `.json` rule files in the `rules/` directory.
4.  **Validate Rules**:
    ```bash
    python scripts/validate_rules.py
    ```

## CI/CD Pipeline

- **Validation**: Every Pull Request triggers a validation check to ensure rule integrity.
- **Deployment**: Merges to the `main` branch automatically deploy the rules to the configured Kibana environment.
