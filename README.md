# TradingView Report Screenshot Automator

A Python-based Tkinter application that automates capturing **TradingView strategy tester reports**. This tool helps save time by **navigating the interface and taking screenshots automatically**.

## Features

- **Automated Navigation**: Moves through TradingView’s UI and generates reports.
- **Screenshot Capture**: Saves reports with custom filenames in the `images/` folder.
- **Configurable**: Set the number of reports and coin names in `config.txt`.
- **Logs**: Displays real-time progress updates in the UI.

## Installation

Ensure **Python 3.9+** is installed. Then, install dependencies using **Poetry**:

```bash
poetry install
```

## Usage

1. **Run the program**:
   ```bash
   python main.py
   ```
2. **Configure coins** in the "Config" tab and save.
3. Click **Start** to begin automation.
4. Screenshots will be saved in the `images/` folder.
5. Click **Stop** to exit.

### 📌 **How-To Video**

Watch this video for a step-by-step guide:  
🔗 [YouTube Tutorial](https://youtu.be/tAdeDQCjHlE)

## Folder Structure

```
TradingView-Report-Screenshot-Automator/
├── images/       # Screenshots saved here
├── main.py       # Main script
├── config.txt    # Settings file
└── README.md     # This file
```

## Notes

- The script **assumes TradingView’s layout remains the same**.
- A **5-second delay** allows users to prepare the screen before automation starts.
