import tkinter as tk
from tkinter import Entry, Label, Button
from PIL import Image, ImageTk

def show_login():
    for widget in root.winfo_children():
        widget.destroy()
    
    logo_label = Label(root, image=photo, bg="#111")
    logo_label.pack(pady=20)
    Label(root, text="DentiGenius", fg="white", bg="#111", font=("Arial", 16, "bold")).pack()
    Label(root, text="Welcome Back", fg="white", bg="#111", font=("Arial", 12)).pack(pady=10)
    
    Label(root, text="Username", fg="white", bg="#111", font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
    username_entry = Entry(root, bg="#333", fg="white", font=("Arial", 12), relief="flat")
    username_entry.pack(pady=5, padx=40, ipadx=40, ipady=5)
    
    Label(root, text="Password", fg="white", bg="#111", font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
    password_entry = Entry(root, bg="#333", fg="white", font=("Arial", 12), relief="flat", show="*")
    password_entry.pack(pady=5, padx=40, ipadx=40, ipady=5)
    
    Label(root, text="Forgot Password?", fg="#ff0066", bg="#111", font=("Arial", 10)).pack(anchor="w", padx=40, pady=(5,0))
    
    Button(root, text="Login", bg="#ff0066", fg="white", font=("Arial", 12, "bold"), relief="flat").pack(pady=20, ipadx=50, ipady=5)
    
    Label(root, text="Don't have an account?", fg="white", bg="#111", font=("Arial", 10)).pack(side="left", padx=80)
    Button(root, text="Sign Up", fg="#ff0066", bg="#111", font=("Arial", 10, "bold"), relief="flat", command=show_signup).pack(side="right", padx=80)

def show_signup():
    for widget in root.winfo_children():
        widget.destroy()
    
    logo_label = Label(root, image=photo, bg="#111")
    logo_label.pack(pady=20)
    Label(root, text="DentiGenius", fg="white", bg="#111", font=("Arial", 16, "bold")).pack()
    
    Label(root, text="USERNAME", fg="white", bg="#111", font=("Arial", 10, "bold")).pack(anchor="w", padx=40, pady=(20, 0))
    Entry(root, bg="#333", fg="white", font=("Arial", 12), relief="flat").pack(pady=5, padx=40, ipadx=40, ipady=5)
    
    Label(root, text="PHONE NUMBER", fg="white", bg="#111", font=("Arial", 10, "bold")).pack(anchor="w", padx=40, pady=(10, 0))
    Entry(root, bg="#333", fg="white", font=("Arial", 12), relief="flat").pack(pady=5, padx=40, ipadx=40, ipady=5)
    
    Label(root, text="E-mail", fg="white", bg="#111", font=("Arial", 10, "bold")).pack(anchor="w", padx=40, pady=(10, 0))
    Entry(root, bg="#333", fg="white", font=("Arial", 12), relief="flat").pack(pady=5, padx=40, ipadx=40, ipady=5)
    
    Button(root, text="Sign In", bg="#ff0066", fg="white", font=("Arial", 12, "bold"), relief="flat", command=show_login).pack(pady=20, ipadx=50, ipady=5)

root = tk.Tk()
root.title("DentiGenius Login")
root.geometry("350x500")
root.configure(bg="#111")

image = Image.open("Login.png")  # Ensure this image is in the same directory
image = image.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

show_login()
root.mainloop()

