import tkinter as tk
from tkinter import messagebox
from logic.billing import Billing

billing_system = Billing()
billing_system.create_table()

def generate_bill():
    name = entry_name.get().strip()
    mobile = entry_mobile.get().strip()
    amount = entry_amount.get().strip()

    if not (name and mobile and amount.isdigit()):
        messagebox.showerror("Error", "Invalid input. Please fill all fields correctly.")
        return

    filepath = billing_system.generate_bill_file(name, mobile, float(amount))
    messagebox.showinfo("Success", f"Bill generated and saved at:\n{filepath}")

def delete_bill():
    bill_id = entry_delete.get().strip()
    if not bill_id.isdigit():
        messagebox.showerror("Error", "Enter valid Bill ID.")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete?")
    if confirm:
        billing_system.delete_bill(int(bill_id))
        messagebox.showinfo("Deleted", "Bill deleted successfully.")

# Tkinter GUI Layout
app = tk.Tk()
app.title("Billing System GUI")
app.geometry("400x400")

tk.Label(app, text="Customer Name").pack()
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Mobile Number").pack()
entry_mobile = tk.Entry(app)
entry_mobile.pack()

tk.Label(app, text="Amount").pack()
entry_amount = tk.Entry(app)
entry_amount.pack()

tk.Button(app, text="Generate Bill", command=generate_bill).pack(pady=10)

tk.Label(app, text="Enter Bill ID to Delete").pack()
entry_delete = tk.Entry(app)
entry_delete.pack()

tk.Button(app, text="Delete Bill", command=delete_bill).pack(pady=5)

tk.Button(app, text="Exit", command=app.destroy).pack(pady=20)

app.mainloop()
