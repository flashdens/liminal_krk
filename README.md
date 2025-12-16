# liminal_krk

WHAT IS IT? TODO

## Setup
Pre-requisite: `python3.9` or higher installed

1. Create the virtual environment.
```
python3 -m venv .venv
```
2. Activate venv.
```
source .venv/bin/activate # Linux/MacOS
venv\Scripts\activate.ps1 # Windows
```
3. Install required packages.
```
pip install -r requirements.txt
```
4. Run the application.
```
python3 app.py run 
```
By default app runs on port `8000`, this behaviour can be modified in `app.py`.

If you're using Visual Studio Code, you can run by selecting `Run > Run Without Debugging` from the menu bar. If you want to start with a debugger attached, select `Run > Start Debugging`.

Any modifications to VS Code run settings need to be applied in `.vscode/launch.json`
