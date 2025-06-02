# 🏠 Smart Home Controller

A Python-based Smart Home Controller application with both CLI and GUI components to simulate control over various rooms and their devices such as lights, gas, water, air conditioning, and temperature.

## 📁 Project Structure

```
SmartHomeController/
├── GUI.py                # GUI implementation using Tkinter
├── thefunctions.py       # Core backend logic (authentication, device control, etc.)
├── users.txt             # Stores user login credentials
├── temperature.txt       # Stores temperature settings
├── light.txt             # Stores light statuses
├── water.txt             # Stores water statuses
├── gas.txt               # Stores gas statuses
├── device.txt            # Stores device statuses
├── splash2.png           # Optional splash screen image
├── home.jpg              # Optional GUI background image
└── README.md             # Project documentation
```

## 🚀 Features

### 🔐 User Authentication
- Sign-up and login system with password strength validation.
- Parent and child modes with different control privileges.

### 🧠 Modes
- **Parent Mode**: Full control over all systems (temperature, lights, water, gas, and devices).
- **Child Mode**: Limited control (lights, water, and devices only).

### 🖥️ GUI Interface (GUI.py)
- Splash screen with an optional welcome image.
- Login/Sign-up flow.
- Room-wise control panel with device toggles and temperature settings.
- Real-time status display for all rooms.

### 🧪 CLI Interface (thefunctions.py)
- Functions for device management, lighting, water, gas, temperature, and user handling.
- Timer system for auto-closing devices.
- Password validation with specific constraints (uppercase, digit, special character).

## 🛠️ Requirements

- Python 3.x
- `tkinter` (comes with Python)
- `Pillow` for image handling in the GUI:
  ```
  pip install Pillow
  ```

## 📦 How to Run

1. **Start the GUI Application**
   ```bash
   python GUI.py
   ```

2. **Use the CLI (Optional Testing / Debug)**
   ```bash
   python thefunctions.py
   ```

## 📌 Notes

- This project uses simple text files for data storage, which can be replaced with a database in the future.
- Ensure `splash2.png` and `home.jpg` are in the same directory for proper UI rendering.

## 👨‍👩‍👧‍👦 Authors
- Ahmed Mohsen
- [@Jana-Ahmed-20005](https://github.com/Jana-Ahmed-20005)
- Mostafa Magdy
- Developed as part of the university smart home simulation project.
