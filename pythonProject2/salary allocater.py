import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import os

class SalaryAllocatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Salary Allocator")

        self.salary_label = tk.Label(master, text="Enter your salary:")
        self.salary_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.salary_entry = tk.Entry(master)
        self.salary_entry.grid(row=0, column=1, padx=10, pady=5)

        self.allocate_button = tk.Button(master, text="Allocate", command=self.allocate_salary)
        self.allocate_button.grid(row=1, columnspan=2, padx=10, pady=5)

        self.savings_label = tk.Label(master, text="Savings:")
        self.savings_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.spending_label = tk.Label(master, text="Spending:")
        self.spending_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.charity_label = tk.Label(master, text="Charity:")
        self.charity_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.total_savings_label = tk.Label(master, text="Total Savings:")
        self.total_savings_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.savings_var = tk.StringVar()
        self.spending_var = tk.StringVar()
        self.charity_var = tk.StringVar()
        self.total_savings_var = tk.StringVar()

        self.savings_display = tk.Label(master, textvariable=self.savings_var)
        self.savings_display.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.spending_display = tk.Label(master, textvariable=self.spending_var)
        self.spending_display.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.charity_display = tk.Label(master, textvariable=self.charity_var)
        self.charity_display.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.total_savings_display = tk.Label(master, textvariable=self.total_savings_var)
        self.total_savings_display.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.history_label = tk.Label(master, text="Transaction History:")
        self.history_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.history_text = tk.Text(master, height=10, width=60)
        self.history_text.grid(row=7, columnspan=2, padx=10, pady=5)

        self.clear_button = tk.Button(master, text="Clear History", command=self.clear_transaction_history)
        self.clear_button.grid(row=8, column=0, padx=10, pady=5)

        self.clear_last_button = tk.Button(master, text="Clear Last Transaction", command=self.clear_last_transaction)
        self.clear_last_button.grid(row=8, column=1, padx=10, pady=5)

        self.total_savings_button = tk.Button(master, text="Total Savings", command=self.show_total_savings_popup)
        self.total_savings_button.grid(row=8, columnspan=2, padx=10, pady=5)

        self.display_transaction_history()

    def allocate_salary(self):
        try:
            salary = float(self.salary_entry.get())
            savings = salary * 0.65
            spending = salary * 0.30
            charity = salary * 0.05

            self.savings_var.set(f"${savings:.2f}")
            self.spending_var.set(f"${spending:.2f}")
            self.charity_var.set(f"${charity:.2f}")

            previous_total_savings = self.calculate_total_savings()
            total_savings = previous_total_savings + savings
            self.total_savings_var.set(f"${total_savings:.2f}")

            self.update_transaction_history(salary, savings, spending, charity)

        except ValueError:
            self.savings_var.set("Invalid input")
            self.spending_var.set("")
            self.charity_var.set("")

    def update_transaction_history(self, salary, savings, spending, charity):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        transaction = {
            "Timestamp": timestamp,
            "Salary": salary,
            "Savings": savings,
            "Spending": spending,
            "Charity": charity
        }

        with open("transaction_history.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=transaction.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(transaction)

        self.display_transaction_history()

    def display_transaction_history(self):
        self.history_text.delete("1.0", tk.END)
        total_savings = 0
        with open("transaction_history.csv", "r") as file:
            reader = csv.DictReader(file)
            self.history_text.insert(tk.END, "Timestamp | Salary | Savings | Spending | Charity | Total Savings\n")
            for row in reader:
                total_savings += float(row['Savings'])
                self.history_text.insert(tk.END, f"{row['Timestamp']} | ${row['Salary']} | ${row['Savings']} | ${row['Spending']} | ${row['Charity']} | ${total_savings:.2f}\n")

    def show_total_savings_popup(self):
        total_savings = self.calculate_total_savings()
        messagebox.showinfo("Total Savings", f"Total Savings: ${total_savings:.2f}")

    def calculate_total_savings(self):
        total_savings = 0
        with open("transaction_history.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_savings += float(row['Savings'])
        return total_savings

    def clear_transaction_history(self):
        with open("transaction_history.csv", "w", newline=""):
            pass
        self.history_text.delete("1.0", tk.END)

    def clear_last_transaction(self):
        lines = list()
        with open("transaction_history.csv", "r") as file:
            lines = file.readlines()
        with open("transaction_history.csv", "w") as file:
            file.writelines(lines[:-1])
        self.display_transaction_history()


def main():
    root = tk.Tk()
    app = SalaryAllocatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
