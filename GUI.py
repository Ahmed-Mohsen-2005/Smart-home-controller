import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from thefunctions import Save_user


# Splash Screen
def show_splash():
    splash = tk.Tk()
    splash.geometry("600x400")
    splash.overrideredirect(True)

    # Center the splash screen on the screen
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (400 / 2)
    splash.geometry(f"600x400+{int(x)}+{int(y)}")

    try:
        splash_image = Image.open('splash2.png')
        splash_photo = ImageTk.PhotoImage(splash_image)
        splash_label = tk.Label(splash, image=splash_photo)
        splash_label.image = splash_photo  # Keep a reference to avoid garbage collection
        splash_label.pack(fill='both', expand=True)
    except Exception as e:
        print(f"Error loading image: {e}")
        splash_label = tk.Label(splash, text="Smart Home Controller", font=("Helvetica", 24))
        splash_label.pack(fill='both', expand=True)

    welcome_text = tk.Label(splash, text="Welcome to Smart Home Controller", font=("Helvetica", 24), bg="#000000",
                            fg="white")
    welcome_text.place(relx=0.5, rely=0.8, anchor='center')

    splash.update()

    # Close splash screen after 5 seconds and open the main application
    splash.after(5000, splash.destroy)
    splash.after(5000, main_application)

    splash.mainloop()
    main_application()

# Main Application
def main_application():
    root = tk.Tk()
    root.withdraw()  # Hide the root window initially

    # Initial state of the home
    home_state = {
        "Living Room": {"temperature": "24", "light": "off", "TV": "off", "Air Conditioner": "on", "Fan": "off"},
        "Bedroom": {"temperature": "22", "light": "on", "TV": "off", "Air Conditioner": "off", "Fan": "on"},
        "Kitchen": {"temperature": "20", "light": "on", "water": "off", "gas": "off", "Blender": "off",
                    "Microwave": "on"},
        "Bathroom": {"temperature": "18", "light": "off", "water": "on", "gas": "on", "Heater": "off",
                     "Washing Machine": "off"},
        "Sofra": {"temperature": "21", "light": "off", "Curtains": "open", "Self Vacuum Cleaner": "off"}
    }

    def login_signup_choice():
        choice_window = tk.Toplevel(root)
        choice_window.title("Sign Up or Login")
        choice_window.geometry("300x200")

        # Center the choice window on the screen
        screen_width = choice_window.winfo_screenwidth()
        screen_height = choice_window.winfo_screenheight()
        x = (screen_width / 2) - (300 / 2)
        y = (screen_height / 2) - (200 / 2)
        choice_window.geometry(f"300x200+{int(x)}+{int(y)}")

        def open_signup():
            choice_window.destroy()
            signup_page()

        def open_login():
            choice_window.destroy()
            login_page()

        ttk.Label(choice_window, text="Do you want to Sign Up or Login?", font=("Helvetica", 14)).pack(pady=20)
        ttk.Button(choice_window, text="Sign Up", command=open_signup).pack(pady=10)
        ttk.Button(choice_window, text="Login", command=open_login).pack(pady=10)

        choice_window.mainloop()

    def signup_page():
        root.deiconify()  # Show the root window now

        def validate_password(password):
            """Validates the password based on specific criteria."""
            if len(password) < 8:
                return "Password must be at least 8 characters long!"
            if not any(char.isupper() for char in password):
                return "Password must contain at least one uppercase letter!"
            if not any(char.isdigit() for char in password):
                return "Password must contain at least one digit!"
            if not any(char in "@*/_" for char in password):
                return "Password must contain at least one special character (@, *, /, _)"
            return "valid"

        def signup():
            newusername = username_entry.get()
            newpassword = password_entry.get()
            mode = mode_var.get()

            pass_check = validate_password(newpassword)
            if pass_check == "valid":
                Save_user(newusername, newpassword, mode)
                messagebox.showinfo("Success", "Signed up successfully!")
                root.destroy()
                home_page(mode)
            else:
                messagebox.showerror("Invalid Password", pass_check)

        frame = ttk.Frame(root)
        frame.pack(pady=50)

        ttk.Label(frame, text="Sign Up").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Username:").grid(row=1, column=0, pady=10)
        username_entry = ttk.Entry(frame)
        username_entry.grid(row=1, column=1, pady=10)

        ttk.Label(frame, text="Password:").grid(row=2, column=0, pady=10)
        password_entry = ttk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, pady=10)

        mode_var = tk.StringVar(value="parent")
        ttk.Label(frame, text="Mode:").grid(row=3, column=0, pady=10)
        ttk.Radiobutton(frame, text="Parent", variable=mode_var, value="parent").grid(row=3, column=1, pady=10)
        ttk.Radiobutton(frame, text="Child", variable=mode_var, value="child").grid(row=3, column=2, pady=10)

        signup_button = ttk.Button(frame, text="Sign Up", command=signup)
        signup_button.grid(row=4, column=1, pady=20)

    def login_page():
        root.deiconify()  # Show the root window now

        def login_mode():
            username = username_entry.get()
            user_password = password_entry.get()
            mode = mode_var.get()

            try:
                with open("users.txt", "r") as userfile:
                    users = userfile.readlines()
                    found = False
                    for user in users:
                        user_data = user.split("\t")
                        if len(user_data) >= 3:  # Ensure there are at least 3 elements in the list
                            stored_username = user_data[0].split(": ")[1].strip()
                            stored_password = user_data[1].split(": ")[1].strip()
                            stored_mode = user_data[2].split(": ")[1].strip()

                            if username == stored_username and user_password == stored_password:
                                found = True
                                messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
                                root.destroy()
                                home_page(stored_mode)
                                break
                        else:
                            print(f"Invalid data format: {user_data}")
                    if not found:
                        messagebox.showerror("Login Failed", "Invalid username or password")
            except FileNotFoundError:
                messagebox.showerror("Error", "User database not found!")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        frame = ttk.Frame(root)
        frame.pack(pady=50)

        ttk.Label(frame, text="Login").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Username:").grid(row=1, column=0, pady=10)
        username_entry = ttk.Entry(frame)
        username_entry.grid(row=1, column=1, pady=10)

        ttk.Label(frame, text="Password:").grid(row=2, column=0, pady=10)
        password_entry = ttk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, pady=10)

        mode_var = tk.StringVar(value="parent")
        ttk.Label(frame, text="Mode:").grid(row=3, column=0, pady=10)
        ttk.Radiobutton(frame, text="Parent", variable=mode_var, value="parent").grid(row=3, column=1, pady=10)
        ttk.Radiobutton(frame, text="Child", variable=mode_var, value="child").grid(row=3, column=2, pady=10)

        login_button = ttk.Button(frame, text="Login", command=login_mode)
        login_button.grid(row=4, column=1, pady=20)

    def home_page(mode):
        root = tk.Tk()
        root.title("Smart Home Controller")
        root.geometry("600x400")

        # Load and set the background image
        background_image = Image.open('home.jpg')
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(root, image=background_photo)
        background_label.image = background_photo  # Keep a reference to avoid garbage collection
        background_label.place(relwidth=1, relheight=1)

        ttk.Label(root, text="Smart Home Controller", font=("Helvetica", 18)).pack(pady=20)

        def open_room_controls(room_name, features):
            room_window = tk.Toplevel(root)
            room_window.title(f"{room_name} Controls")
            room_window.geometry("500x500")

            ttk.Label(room_window, text=f"{room_name} Controls", font=("Helvetica", 16)).pack(pady=20)

            feature_states = {feature: tk.StringVar(value=home_state[room_name].get(feature, "off")) for feature in
                              features}
            feature_states["temperature"] = tk.StringVar(value=home_state[room_name].get("temperature", "25"))

            def set_temperature():
                try:
                    temp = int(feature_states["temperature"].get())
                    if temp < 18 or temp > 30:
                        messagebox.showwarning("Warning", "Not Safe: Temperature must be between 18 and 30°C")
                        return
                    home_state[room_name]["temperature"] = str(temp)
                    messagebox.showinfo("Info", f"Temperature set to {temp}°C")
                except ValueError:
                    messagebox.showwarning("Warning", "Please enter a valid number")

            # Temperature Control
            if mode == "parent":
                ttk.Label(room_window, text="Temperature (°C):").pack(pady=10)
                temperature_entry = ttk.Entry(room_window, textvariable=feature_states["temperature"])
                temperature_entry.pack(pady=10)
                ttk.Button(room_window, text="Set Temperature", command=set_temperature).pack(pady=10)

            # Device Controls
            for feature in features:
                frame = ttk.Frame(room_window)
                frame.pack(pady=5)
                ttk.Label(frame, text=f"{feature.capitalize()}: ").pack(side=tk.LEFT)
                ttk.Radiobutton(frame, text="On", variable=feature_states[feature], value="on").pack(side=tk.LEFT)
                ttk.Radiobutton(frame, text="Off", variable=feature_states[feature], value="off").pack(side=tk.LEFT)

            def apply_changes():
                for feature in features:
                    home_state[room_name][feature] = feature_states[feature].get()
                if mode == "parent":
                    home_state[room_name]["temperature"] = feature_states["temperature"].get()
                messagebox.showinfo(f"{room_name} Changes", "Changes applied successfully!")

            ttk.Button(room_window, text="Apply Changes", command=apply_changes).pack(pady=20)

        def show_home_status():
            status = ""
            for room, states in home_state.items():
                status += f"{room}:\n"
                for feature, state in states.items():
                    status += f"{feature.capitalize()}: {state}\n"
                status += "\n"
            messagebox.showinfo("Home Status", status)

        rooms = {
            "Living Room": ["light", "TV", "Air Conditioner", "Fan"],
            "Bedroom": ["light", "TV", "Air Conditioner", "Fan"],
            "Kitchen": ["light", "water", "gas", "Blender", "Microwave"],
            "Bathroom": ["light", "water", "gas", "Heater", "Washing Machine"],
            "Sofra": ["light", "Curtains", "Self Vacuum Cleaner"]
        }

        for room, features in rooms.items():
            if mode == "child" and "gas" in features:
                features.remove("gas")
            if mode == "child" and "temperature" in features:
                features.remove("temperature")

            ttk.Button(root, text=room, command=lambda r=room, f=features: open_room_controls(r, f)).pack(pady=10)

        ttk.Button(root, text="Check Home Status", command=show_home_status).pack(pady=20)

        root.mainloop()

    login_signup_choice()


# Running the Splash Screen and Main Application
if __name__ == "__main__":
    show_splash()