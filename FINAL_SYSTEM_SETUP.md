# AKTA AI SYSTEM - FINAL PRODUCTION SETUP

This file contains the final instructions and files required to run the AI legal investigation system.

## 1. Run locally

``b
git clone https://github.com/adrian1520/akta-ai-system
cd akta-ai-system
pip install -r requirements.txt
python run_investigation.py cases/example_case
```

## 2. GitHub Actions Issue Workflow
Create file: .github/workflows/issue_investigation.yml

```yaml
name: AI Legal Investigation

on:
  issues:
    types: [opened]

jobs:
  investigate:
    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - run: pip install -r requirements.txt

      - run: python run_investigation.py cases/example_case

```

## 3. Issue Format

Text to place in GitHub issue:
```
case: example_case
action: investigate
```

## 4. GPT Integration Idea
GPT performs:

1. Parse images or PDF.
2. Save documents to cases/<case>/documents/
3. Create a GitHub issue.
4. GitHub Actions run the investigation.
5. Report is posted back to the issue.

## 5. System Capabilities

- Document parsing
- Timeline reconstruction
- Testimony contradiction detection
- Procedural error detection
- Legal reasoning graph
- Litigation strategy generation
- Autonomous investigation report
