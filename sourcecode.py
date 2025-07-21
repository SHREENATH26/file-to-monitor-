import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class LatestItemMonitorHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.file_states = {}  # Tracks the state of all text files

    def _read_last_line(self, file_path):
        """Reads the last line of the file."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return lines[-1].strip() if lines else None
        except Exception as e:
            print(f"Error reading file '{file_path}': {e}")
            return None

    def _process_file(self, file_path):
        """Processes a modified file to identify the latest line added."""
        last_line = self._read_last_line(file_path)
        previous_last_line = self.file_states.get(file_path)

        # Check if a new line has been added
        if last_line and last_line != previous_last_line:
            print(f"Latest item added in '{file_path}': {last_line}")
            self.file_states[file_path] = last_line

    def on_modified(self, event):
        if event.is_directory:
            return  # Ignore directory modifications
        if event.src_path.endswith('.txt'):  # Only process .txt files
            self._process_file(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return  # Ignore directory creations
        if event.src_path.endswith('.txt'):  # Only process .txt files
            print(f"New text file created: {event.src_path}")
            last_line = self._read_last_line(event.src_path)
            if last_line:
                print(f"Latest item in new file '{event.src_path}': {last_line}")
                self.file_states[event.src_path] = last_line

def monitor_all_folders(base_directory):
    if not os.path.exists(base_directory):
        print(f"Error: The directory '{base_directory}' does not exist.")
        return

    event_handler = LatestItemMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=base_directory, recursive=True)  # Recursive monitoring
    observer.start()
    print(f"Monitoring all .txt files in: {base_directory} and its subdirectories")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopping the directory monitor...")

    observer.join()

if __name__ == "__main__":
    base_directory = ("location of the file")  # Update this path
    monitor_all_folders(base_directory)

## install Watchdog libraries 
