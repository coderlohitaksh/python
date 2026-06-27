import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import json
import os

# ---------------- Appearance ----------------
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# ---------------- Database ----------------
DB_FILE = "users.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump(
            {
                "users": [
                    {
                        "username": "admin",
                        "password": "1234"
                    }
                ],
                "remember": {
                    "enabled": False,
                    "username": ""
                }
            },
            f,
            indent=4
        )


def load_data():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------- Window ----------------
app = ctk.CTk()
app.geometry("430x520")
app.title("Professional Login")
app.resizable(False, False)

# ---------------- Icons ----------------
view_icon = ctk.CTkImage(
    light_image=Image.open("001-view.png"),
    dark_image=Image.open("001-view.png"),
    size=(22,22)
)

hide_icon = ctk.CTkImage(
    light_image=Image.open("002-hide.png"),
    dark_image=Image.open("002-hide.png"),
    size=(22,22)
)

password_visible = False

# ---------------- Login ----------------
def toggle_login_password():

    global password_visible

    if password_visible:
        login_password.configure(show="*")
        login_eye.configure(image=hide_icon)
        password_visible = False
    else:
        login_password.configure(show="")
        login_eye.configure(image=view_icon)
        password_visible = True


def login():

    username = login_username.get().strip()
    password = login_password.get().strip()

    data = load_data()

    for user in data["users"]:

        if user["username"] == username and user["password"] == password:

            if remember_var.get():

                data["remember"]["enabled"] = True
                data["remember"]["username"] = username

            else:

                data["remember"]["enabled"] = False
                data["remember"]["username"] = ""

            save_data(data)

            messagebox.showinfo(
                "Success",
                f"Welcome {username}!"
            )

            show_home(username)
            return

    messagebox.showerror(
        "Login Failed",
        "Invalid Username or Password."
    )


# ---------------- Login Frame ----------------
login_frame = ctk.CTkFrame(
    app,
    corner_radius=18
)
login_frame.pack(
    expand=True,
    padx=25,
    pady=25,
    fill="both"
)

title = ctk.CTkLabel(
    login_frame,
    text="🔐 LOGIN",
    font=("Segoe UI",28,"bold")
)
title.pack(pady=(25,20))

login_username = ctk.CTkEntry(
    login_frame,
    width=300,
    height=42,
    placeholder_text="Username"
)
login_username.pack(pady=10)

password_frame = ctk.CTkFrame(
    login_frame,
    fg_color="transparent"
)
password_frame.pack()

login_password = ctk.CTkEntry(
    password_frame,
    width=250,
    height=42,
    placeholder_text="Password",
    show="*"
)
login_password.pack(side="left")

login_eye = ctk.CTkButton(
    password_frame,
    text="",
    image=hide_icon,
    width=40,
    height=40,
    fg_color="transparent",
    hover_color=("gray85","gray20"),
    command=toggle_login_password
)
login_eye.pack(side="left", padx=5)

remember_var = ctk.BooleanVar()

remember_box = ctk.CTkCheckBox(
    login_frame,
    text="Remember Me",
    variable=remember_var
)
remember_box.pack(
    anchor="w",
    padx=60,
    pady=(10,15)
)

data = load_data()

if data["remember"]["enabled"]:

    login_username.insert(
        0,
        data["remember"]["username"]
    )

    remember_var.set(True)

login_button = ctk.CTkButton(
    login_frame,
    text="Login",
    width=300,
    height=42,
    command=login
)
login_button.pack(pady=15)

signup_button = ctk.CTkButton(
    login_frame,
    text="Create New Account",
    width=300,
    height=42,
    fg_color="gray40",
    hover_color="gray30",
    command=lambda: show_signup()
)
signup_button.pack()

status = ctk.CTkLabel(
    login_frame,
    text="Use your credentials to login."
)
status.pack(pady=20)
# ---------------- Signup ----------------
signup_visible = False

def toggle_signup_password():

    global signup_visible

    if signup_visible:
        signup_password.configure(show="*")
        signup_eye.configure(image=hide_icon)
        signup_visible = False
    else:
        signup_password.configure(show="")
        signup_eye.configure(image=view_icon)
        signup_visible = True


# ---------------- Home Screen ----------------
def show_home(username):

    login_frame.pack_forget()
    signup_frame.pack_forget()

    home_frame.pack(
        expand=True,
        padx=25,
        pady=25,
        fill="both"
    )

    welcome_label.configure(
        text=f"Welcome,\n{username}"
    )


def logout():

    home_frame.pack_forget()
    login_frame.pack(
        expand=True,
        padx=25,
        pady=25,
        fill="both"
    )


# ---------------- Switch Pages ----------------
def show_signup():

    login_frame.pack_forget()

    signup_frame.pack(
        expand=True,
        padx=25,
        pady=25,
        fill="both"
    )


def show_login():

    signup_frame.pack_forget()

    login_frame.pack(
        expand=True,
        padx=25,
        pady=25,
        fill="both"
    )


# ---------------- Register ----------------
def register():

    username = signup_username.get().strip()
    password = signup_password.get().strip()

    if username == "" or password == "":
        messagebox.showwarning(
            "Warning",
            "Please fill all fields."
        )
        return

    data = load_data()

    for user in data["users"]:

        if user["username"] == username:

            messagebox.showerror(
                "Error",
                "Username already exists."
            )
            return

    data["users"].append(
        {
            "username": username,
            "password": password
        }
    )

    save_data(data)

    messagebox.showinfo(
        "Success",
        "Account created successfully!"
    )

    signup_username.delete(0, "end")
    signup_password.delete(0, "end")

    show_login()


# ---------------- Signup Frame ----------------
signup_frame = ctk.CTkFrame(
    app,
    corner_radius=18
)

signup_title = ctk.CTkLabel(
    signup_frame,
    text="📝 SIGN UP",
    font=("Segoe UI",28,"bold")
)
signup_title.pack(pady=(25,20))

signup_username = ctk.CTkEntry(
    signup_frame,
    width=300,
    height=42,
    placeholder_text="Choose Username"
)
signup_username.pack(pady=10)

signup_pass_frame = ctk.CTkFrame(
    signup_frame,
    fg_color="transparent"
)
signup_pass_frame.pack()

signup_password = ctk.CTkEntry(
    signup_pass_frame,
    width=250,
    height=42,
    placeholder_text="Choose Password",
    show="*"
)
signup_password.pack(side="left")

signup_eye = ctk.CTkButton(
    signup_pass_frame,
    text="",
    image=hide_icon,
    width=40,
    height=40,
    fg_color="transparent",
    hover_color=("gray85","gray20"),
    command=toggle_signup_password
)
signup_eye.pack(side="left", padx=5)

create_button = ctk.CTkButton(
    signup_frame,
    text="Create Account",
    width=300,
    height=42,
    command=register
)
create_button.pack(pady=20)

back_button = ctk.CTkButton(
    signup_frame,
    text="← Back to Login",
    width=300,
    height=42,
    fg_color="gray40",
    hover_color="gray30",
    command=show_login
)
back_button.pack()

# ---------------- Home Frame ----------------
home_frame = ctk.CTkFrame(
    app,
    corner_radius=18
)

welcome_label = ctk.CTkLabel(
    home_frame,
    text="Welcome",
    font=("Segoe UI",30,"bold")
)
welcome_label.pack(pady=50)

logout_button = ctk.CTkButton(
    home_frame,
    text="Logout",
    width=220,
    height=42,
    fg_color="#d32f2f",
    hover_color="#b71c1c",
    command=logout
)
logout_button.pack()

# ---------------- Start App ----------------
app.mainloop()