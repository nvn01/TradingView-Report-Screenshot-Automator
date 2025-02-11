# main.py
import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import os
import platform
if platform.system() == "Windows":
    import winsound
import threading
from tkinter import messagebox

CONFIG_FILE = "config.txt"

# Function to log messages to the log box
def log_message(log_box, message):
    log_box.config(state='normal')
    log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)
    log_box.config(state='disabled')
    log_box.update_idletasks()

# Function to wait for a pixel color at (x, y) to change from an initial_color
# Waits indefinitely until the color changes
def wait_for_pixel_change(x, y, initial_color, log_box):
    while True:
        current_color = pyautogui.pixel(x, y)
        if current_color != initial_color:
            log_message(log_box, f"Pixel at ({x},{y}) changed color from {initial_color} to {current_color}.")
            return True
        time.sleep(0.5)

# Function to save configuration to a file
def save_config(coin_list):
    with open(CONFIG_FILE, "w") as config_file:
        config_file.write(f"chart={','.join(coin_list)}\n")

# Function to load configuration from a file
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            lines = config_file.readlines()
            coin_list = lines[0].strip().split("=")[1].split(",")
            total = len(coin_list)  # Automatically count items
            return total, coin_list
    return 3, ["BTCUSDT", "ETHUSDT", "SOLUSDT"]  # Default values

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
        log_message(log_box, "Generate report clicked. Waiting for the pixel (820, 305) to change from (255, 255, 255)...")

        # Wait until the pixel changes color
        changed = wait_for_pixel_change(99, 997, (255, 255, 255), log_box)
        
        # Add 2-second delay after pixel change
        log_message(log_box, "Pixel changed, waiting 2 seconds before taking screenshot...")
        time.sleep(2)

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
    make_beep()  # Add beep sound

def make_beep():
    if platform.system() == "Windows":
        for _ in range(2):
            winsound.Beep(1000, 500)  # 1000Hz for 500ms
            time.sleep(0.1)
    else:
        # For Unix systems
        for _ in range(2):
            os.system('echo -n "\a"')
            time.sleep(0.1)

def increase_font_size(log_box):
    current_font = log_box.cget("font")
    if isinstance(current_font, str):
        family = current_font
        size = 10
    else:
        family, size = current_font.split()
        size = int(size)
    log_box.configure(font=(family, size + 5))

def decrease_font_size(log_box):
    current_font = log_box.cget("font")
    if isinstance(current_font, str):
        family = current_font
        size = 10
    else:
        family, size = current_font.split()
        size = int(size)
    if size > 6:  # Prevent font from becoming too small
        log_box.configure(font=(family, size - 5))

# Main Application
def main():
    total, coin_list = load_config()

    # Create Tkinter window
    root = tk.Tk()
    root.title("TradingView Report Screenshot Automator")
    root.geometry("800x600")  # Set initial window size
    root.minsize(400, 300)    # Set minimum window size

    # Tab Control
    tab_control = ttk.Notebook(root)
    home_tab = ttk.Frame(tab_control)
    config_tab = ttk.Frame(tab_control)
    tab_control.add(home_tab, text="Home")
    tab_control.add(config_tab, text="Config")
    tab_control.pack(expand=1, fill="both")

    # Home Tab
    # Create a frame to contain the log box
    log_frame = ttk.Frame(home_tab)
    log_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

    # Create the log box with initial font size and make it read-only
    log_box = tk.Text(log_frame, height=10, width=50, font=("TkDefaultFont", 10), state='disabled')
    log_box.pack(fill=tk.BOTH, expand=True)

    # Add scrollbar
    scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=log_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    log_box.configure(yscrollcommand=scrollbar.set)

    # Modify the log_message function to handle the disabled state
    def log_message(log_box, message):
        log_box.config(state='normal')
        log_box.insert(tk.END, message + "\n")
        log_box.see(tk.END)
        log_box.config(state='disabled')
        log_box.update_idletasks()

    # Modify key bindings for continuous font size changes
    def handle_font_size(event, increase=True):
        if increase:
            increase_font_size(log_box)
        else:
            decrease_font_size(log_box)
        return "break"  # Prevent default handling

    root.bind('<Control-plus>', lambda e: handle_font_size(e, True))
    root.bind('<Control-equal>', lambda e: handle_font_size(e, True))  # For keyboards where + requires shift
    root.bind('<Control-minus>', lambda e: handle_font_size(e, False))

    def start_process():
        if hasattr(start_process, 'running') and start_process.running:
            messagebox.showwarning("Warning", "Process is already running!")
            return
        
        start_process.running = True
        start_button.config(state='disabled')
        
        def run_automation():
            try:
                clear_images_folder("images", log_box)
                if not os.path.exists("images"):
                    os.makedirs("images")
                automate_screenshots(total, coin_list, "images", log_box)
            except Exception as e:
                log_message(log_box, f"Error: {str(e)}")
            finally:
                start_process.running = False
                root.after(0, lambda: start_button.config(state='normal'))
        
        thread = threading.Thread(target=run_automation)
        thread.daemon = True
        thread.start()

    # Create a frame for buttons to place them side by side
    button_frame = ttk.Frame(home_tab)
    button_frame.pack(pady=10)

    start_button = tk.Button(button_frame, text="Start", command=start_process, width=15, height=2)
    start_button.pack(side=tk.LEFT, padx=5)

    stop_button = tk.Button(button_frame, text="Stop", command=root.quit, width=15, height=2)
    stop_button.pack(side=tk.LEFT, padx=5)

    # Config Tab
    tk.Label(config_tab, text="List Name (comma-separated):").pack(pady=5)

    coin_text = tk.Text(config_tab, height=5, width=50)
    coin_text.insert(tk.END, ",".join(coin_list))
    coin_text.pack(pady=5)

    def save_config_and_update():
        nonlocal total, coin_list
        coin_list = coin_text.get("1.0", tk.END).strip().split(",")
        total = len(coin_list)  # Update total based on list length
        save_config(coin_list)
        log_message(log_box, f"Configuration saved! Total items: {total}")

    reset_button = tk.Button(config_tab, text="Reset", command=lambda: coin_text.delete("1.0", tk.END))
    reset_button.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(config_tab, text="Save", command=save_config_and_update)
    save_button.pack(side=tk.RIGHT, padx=5)

    # Run Tkinter loop
    root.mainloop()

if __name__ == "__main__":
    main()
