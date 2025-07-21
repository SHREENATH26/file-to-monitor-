## Real-Time File Monitoring and Event Logging System using Watchdog
This project presents a real-time file monitoring and logging tool built in Python using the Watchdog library. It continuously observes a target directory and detects any file system events such as creation, modification, deletion, and movement. The goal of this project is to ensure data integrity, enable behavioral analysis, and support use cases like automatic backup, version tracking, and system auditing.

## 🧩 Need for the Project
As the volume of digital data grows, so does the need to monitor and protect it. Whether in enterprise systems, IoT environments, or local development setups, unauthorized or accidental changes to files can lead to data loss, corruption, or breaches.

Manual tracking is inefficient and error-prone. This project solves the problem by providing a lightweight, automated solution for detecting and logging file system events in real-time, reducing the risk of unnoticed changes and enabling timely responses.

## ✅ Features & Workflow
✔ Features
Monitors specified directory for real-time file events.

Detects:

File/folder creation

File modifications

File/folder deletion

File/folder movement/renaming

Logs detailed event information including path, event type, and timestamp.

Cross-platform compatibility (Windows, Linux, macOS).

Easily extendable for actions like alerts, backups, or syncs.

## 🔁 Workflow
vbnet
Copy
Edit
Problem Analysis & Use Case ↓
Python Environment Setup ↓
Watchdog Observer & Handler Setup ↓
Custom Event Logging Implementation ↓
Testing Across File Operations ↓
Output Formatting & Result Analysis ↓
Documentation & Extension Suggestions
📚 Literature Survey & Problem Identification
What: Investigated common challenges in data safety, system monitoring, and automation related to file changes.
Why: Identified that many existing solutions are resource-heavy, difficult to configure, or lack real-time capabilities for simple tasks.
How: Reviewed file system APIs, real-time logging tools, and Python's Watchdog documentation to build an optimized solution.

🧠 Design & Implementation
## 📁 Directory Monitoring Using Watchdog
What: Used Python’s Watchdog Observer and FileSystemEventHandler classes.

Why: Enables efficient and reliable event-based monitoring.

How: Implemented a custom handler to define behavior on on_created, on_modified, on_deleted, and on_moved.

🧾 Event Logger
What: Logs every event to the console with event type, path, and timestamp.

Why: Provides clarity and traceability of all file system activities.

How: Used Python’s logging module for formatted output.

## ⚙️ System Setup
Language: Python 3.x

Library Used: watchdog

Installation:

nginx
Copy
Edit
pip install watchdog
Execution Command:

bash
Copy
Edit
python monitor.py
🧪 Testing and Verification
What: Simulated file operations (create, modify, delete, move) within the monitored directory.
Why: To validate that all events are detected accurately.
How: Used test folders and files. Verified logs in console output.

## 📊 Test Results
Test Action	Result Detected	Timestamp Logged	Status
File Created	✅ on_created	✅ Yes	✅ Pass
File Modified	✅ on_modified	✅ Yes	✅ Pass
File Deleted	✅ on_deleted	✅ Yes	✅ Pass
File Moved/Renamed	✅ on_moved	✅ Yes	✅ Pass
Folder Operations	✅ All supported	✅ Yes	✅ Pass

## 📌 Application Target
IoT gateways (monitoring config files)

DevOps pipelines (detect config changes)

Security tools (detect suspicious activity)

Academic or teaching projects (event-driven systems)

## 🛠 Tools Used
🐍 Python 3.x

🔍 Watchdog library

📄 VS Code / PyCharm

📁 Test environment: Windows and Linux directories

📈 Observed Output Sample
bash
Copy
Edit
[2025-07-21 14:33:02] File created: testfile.txt
[2025-07-21 14:33:05] File modified: testfile.txt
[2025-07-21 14:33:10] File deleted: testfile.txt
[2025-07-21 14:33:15] File moved: testfile_old.txt → testfile_new.txt
📑 Learning Outcomes
Mastery of event-driven programming in Python.

Practical understanding of real-time file system monitoring.

Improved logging and automation techniques.

Foundation for building advanced tools (e.g., intrusion detection, live backup, file sync).

## 🔄 Future Enhancements
📤 Email/Slack alert integration for critical events.

💾 Save logs to database or CSV.

📈 Visual dashboard for event visualization.

🧠 AI-based anomaly detection on event patterns.
