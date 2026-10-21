import qrcode
import tkinter as tk
from tkinter import messagebox

# ---------------- CLI FUNCTION ----------------
def generate_qr_cli():
    data = input("Enter data for QR Code: ")
    if not data:
        print("No data entered!")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("cli_qr.png")

    print("QR Code generated and saved as cli_qr.png")


# ---------------- GUI FUNCTION ----------------
def generate_qr_gui():
    data = entry.get()
    if data == "":
        messagebox.showerror("Error", "Please enter some data")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")
    img.save("gui_qr.png")

    messagebox.showinfo("Success", "QR Code saved as gui_qr.png")


# ---------------- GUI SETUP ----------------
def start_gui():
    global entry
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("300x150")

    label = tk.Label(root, text="Enter data:")
    label.pack(pady=5)

    entry = tk.Entry(root, width=35)
    entry.pack(pady=5)

    btn = tk.Button(root, text="Generate QR", command=generate_qr_gui)
    btn.pack(pady=10)

    root.mainloop()


# ---------------- MAIN MENU ----------------
def main():
    print("QR Code Generator")
    print("1. Generate using CLI")
    print("2. Generate using GUI")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        generate_qr_cli()
    elif choice == "2":
        start_gui()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()