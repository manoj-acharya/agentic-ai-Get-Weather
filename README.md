# agentic-ai-Get-Weather

# Google ADK Tutorials

## 1) Project Overview

This project contains simple Google Agent Development Kit (Google ADK) examples to help you learn how to build and run basic agents.

The workspace includes three example types:

- Declarative: agent defined using YAML
- Hybrid: agent using YAML plus a Python tool
- Imperative: agent created programmatically in Python

The hybrid example also demonstrates a simple weather tool.

## 2) Environment Setup

### Prerequisites

- Python 3.10 or newer
- pip
- Git
- VS Code (recommended)

### Windows

1. Open PowerShell or Command Prompt.
2. Go to the project folder:
   ```powershell
   cd C:\Users\DELL\python_projects\udemy-google-adk\google-adk-tutorials
   ```

3. Create a virtual environment:
   ```powershell
   py -m venv .venv
   ```

4. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

### macOS

1. Open Terminal.
2. Go to the project folder:
   ```bash
   cd /path/to/google-adk-tutorials
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> If you are using VS Code, make sure the selected Python interpreter points to the virtual environment you created.

## 3) Code Execution

### Run the examples

After activating the environment, you can run the agent from the relevant folder.

#### Example: Hybrid agent
```bash
cd hybrid
cd hello_agent
adk run hello_agent
```

#### Optional: Start the web UI
If your setup supports it, you can also start the ADK web interface:

```bash
adk web
```

Then open the local URL shown in the terminal in your browser.

### Project folders

- declarative/hello_agent
- hybrid/hello_agent
- impartive/hello_agent
