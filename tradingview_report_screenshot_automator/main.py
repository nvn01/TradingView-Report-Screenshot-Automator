# main.py
import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import os

CONFIG_FILE = "config.txt"

# Function to log messages to the log box
def log_message(log_box, message):
    log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)
    log_box.update_idletasks()  # Ensure UI updates immediately

# Function to save configuration to a file
def save_config(total, coin_list):
    with open(CONFIG_FILE, "w") as config_file:
        config_file.write(f"total={total}\n")
        config_file.write(f"coins={','.join(coin_list)}\n")

# Function to load configuration from a file
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            lines = config_file.readlines()
            total = int(lines[0].strip().split("=")[1])
            coin_list = lines[1].strip().split("=")[1].split(",")
            return total, coin_list
    return 10, ["BTCUSDT", "ETHUSDT", "SOLUSDT"]  # Default values

# Function to take screenshots
def take_screenshot(file_path):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)
        return "Screenshot saved: " + file_path
    except Exception as e:
        return "Error taking screenshot: " + str(e)

# Function to clear the images folder
def clear_images_folder(image_folder, log_box):
    if os.path.exists(image_folder):
        for file in os.listdir(image_folder):
            file_path = os.path.join(image_folder, file)
            try:
                os.remove(file_path)
                log_message(log_box, f"Deleted: {file_path}")
            except Exception as e:
                log_message(log_box, f"Error deleting {file_path}: {e}")
    else:
        os.makedirs(image_folder)
        log_message(log_box, f"Created images folder: {image_folder}")

# Function to automate key presses and screenshot taking
def automate_screenshots(total, coin_list, image_folder, log_box):
    log_message(log_box, "Starting automation process...")
    time.sleep(5)  # Initial delay to ensure focus on the first watchlist item
    log_message(log_box, "Pressing the first watchlist item. Countdown: 5s")

    for index, coin in enumerate(coin_list[:total]):
        log_message(log_box, f"Processing {coin} ({index + 1}/{total})")

        # Navigate to "Generate Report" button
        for i in range(7):
            pyautogui.press("tab")
            time.sleep(0.5)  # Delay for each tab press

        # Generate the report
        pyautogui.press("enter")
        log_message(log_box, "Generate report clicked. Waiting for 5s...")
        time.sleep(5)  # Wait for the report to generate

        # Take the screenshot
        filename = f"{coin}.png"
        file_path = os.path.join(image_folder, filename)
        screenshot_status = take_screenshot(file_path)
        log_message(log_box, screenshot_status)

        # Navigate back to the watchlist
        log_message(log_box, "Returning to watchlist section...")
        for i in range(7):
            pyautogui.keyDown("shift")
            time.sleep(0.2)
            pyautogui.press("tab")
            time.sleep(0.2)
            pyautogui.keyUp("shift")

        pyautogui.press("space")  # Select the next item
        log_message(log_box, "Ready for the next item.")

    log_message(log_box, "Automation process completed!")

# Main Application
def main():
    total, coin_list = load_config()

    # Create Tkinter window
    root = tk.Tk()
    root.title("TradingView Report Screenshot Automator")
    root.attributes('-topmost', True)  # Keep the window always on top

    # Tab Control
    tab_control = ttk.Notebook(root)
    home_tab = ttk.Frame(tab_control)
    config_tab = ttk.Frame(tab_control)
    tab_control.add(home_tab, text="Home")
    tab_control.add(config_tab, text="Config")
    tab_control.pack(expand=1, fill="both")

    # Home Tab
    progress = ttk.Progressbar(home_tab, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)

    log_box = tk.Text(home_tab, height=10, width=50)
    log_box.pack(pady=10)

    def start_process():
        # Clear images folder before starting
        clear_images_folder("images", log_box)
        # Ensure images folder exists
        if not os.path.exists("images"):
            os.makedirs("images")
        automate_screenshots(total, coin_list, "images", log_box)

    start_button = tk.Button(home_tab, text="Start", command=start_process)
    start_button.pack(pady=5)

    stop_button = tk.Button(home_tab, text="Stop", command=root.quit)
    stop_button.pack(pady=5)

    # Config Tab
    tk.Label(config_tab, text="Total List:").pack(pady=5)

    total_entry = tk.Entry(config_tab)
    total_entry.insert(0, str(total))
    total_entry.pack(pady=5)

    tk.Label(config_tab, text="List Name (comma-separated):").pack(pady=5)

    coin_text = tk.Text(config_tab, height=5, width=50)
    coin_text.insert(tk.END, ",".join(coin_list))
    coin_text.pack(pady=5)

    def save_config_and_update():
        nonlocal total, coin_list
        total = int(total_entry.get())
        coin_list = coin_text.get("1.0", tk.END).strip().split(",")
        save_config(total, coin_list)
        log_message(log_box, "Configuration saved!")

    reset_button = tk.Button(config_tab, text="Reset", command=lambda: [total_entry.delete(0, tk.END), coin_text.delete("1.0", tk.END)])
    reset_button.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(config_tab, text="Save", command=save_config_and_update)
    save_button.pack(side=tk.RIGHT, padx=5)

    # Run Tkinter loop
    root.mainloop()

if __name__ == "__main__":
    main()
