# TradingView Report Screenshot Automator

**TradingView Report Screenshot Automator** is a Python-based Tkinter application designed to automate the process of taking screenshots of strategy tester results in TradingView. This tool helps users save time by automating repetitive tasks, such as navigating the TradingView interface and capturing screenshots, with customizable configurations.

## Features

- **Automation**:
  - Automatically navigate the TradingView interface using keyboard inputs.
  - Capture screenshots of strategy tester reports and save them with custom filenames.
- **Configuration**:
  - Set the total number of items to process and specify the coin names in a configuration file.
  - The application will save and reload configurations for future sessions.
- **Folder Management**:
  - Automatically clears the `images` folder at the start of each session to keep files organized.
- **UI**:
  - Simple and interactive user interface built with Tkinter.
  - A log box displays real-time updates during the automation process.

## Prerequisites

Ensure you have the following installed:

- Python 3.9 or higher
- Required Python packages:
  - `pyautogui`
  - `tkinter` (included with Python)

You can install the required packages using the command:

```bash
pip install pyautogui
```

## Folder Structure

The project directory is organized as follows:

```
TradingView-Report-Screenshot-Automator/
│
├── images/                  # Folder to store screenshots
├── main.py                  # Main application script
├── config.txt               # Configuration file (automatically generated)
└── README.md                # Project documentation
```

## How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/<your-username>/TradingView-Report-Screenshot-Automator.git
   cd TradingView-Report-Screenshot-Automator
   ```

2. **Run the Application**:
   Execute the script using Python:

   ```bash
   python main.py
   ```

3. **Configure Settings**:

   - Navigate to the **Config** tab in the application.
   - Enter the **Total List** (number of items to process).
   - Specify coin names as a comma-separated list in the provided text box.
   - Click **Save** to store your settings.

4. **Start Automation**:

   - Go to the **Home** tab.
   - Click the **Start** button to begin the automation process.
   - The application will:
     - Clear the `images/` folder.
     - Capture screenshots of strategy tester results for the specified coin list.
     - Save the screenshots in the `images/` folder.

5. **Stop the Application**:
   - Click the **Stop** button to exit the application.

## Logs

During the automation process, a log box displays real-time updates, such as:

- Current coin being processed.
- Screenshot status (success or error).
- Navigation updates (e.g., returning to the watchlist).

## Configuration File

The `config.txt` file stores the settings for the application:

- `total`: Number of items to process.
- `coins`: Comma-separated list of coin names.

Example:

```
total=10
coins=BTCUSDT,ETHUSDT,SOLUSDT
```

## Example Output

Screenshots are saved in the `images/` folder with filenames based on the coin name:

```
images/
├── BTCUSDT.png
├── ETHUSDT.png
├── SOLUSDT.png
```

## Known Limitations

- The application assumes that the TradingView interface layout remains consistent during automation.
- A 5-second delay is used before starting automation to allow users to set up their screen.

## Contributing

Contributions are welcome! If you find any issues or want to add features:

1. Fork this repository.
2. Create a new branch.
3. Submit a pull request with detailed explanations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyAutoGUI](https://pyautogui.readthedocs.io/) for automation.
- Tkinter for the graphical user interface.

## Contact

For questions or feedback, feel free to open an issue or contact me at `<your-email@example.com>`.
