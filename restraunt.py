import tkinter as tk
from tkinter import ttk, messaegbox

class RestrauntOrderManegement:

    def __init__(self, root):
        self.root = root
        self.root.title(
            "restraunt management app")
        
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER MEAL": 2.5,
            "DRINKS": 1,
        }

    self.exchange_rate = 82

    self.setup_background(root)

    frame = ttk.Frame(root)
    frame.place(relx=0.5, rely=0.5,
                anchor=tk.CENTER)
    
    ttk.Label(frame,
              text="restraunt order management",
              font=("arial", 20, "bold")).grid(row=0,
                                               collumspan=3,
                                               padx=10,
                                               pady=10)

self.menu_quantities = {}

for i, (item, price) in enumerate(self.menu_items(), start=1):
    label = ttk.Label(frame,
                      text=f"{item} (${price}):",
                      font=("ariel", 12))
    label.grid(row=1, column=0, padx=10, pady=5)
    self.menu_labels[item] = label

    quantity_entry = ttk.Entry(frame, width=5)
    quantity_entry.grid(row=i, column=1, padx=10, pady=5)
    self.menu_quantities[item] = quantity_entry

self.currency_var = tk.StringVar()
ttk.Label(frame, text="currency:",
          front=("arial", 12)).grid(row=len(self.menu_items) + 1,
                                    column=0,
                                    padx=10,
                                    pady=5)

currency_dropdown = ttk.Combobox(frame,
                                 textvariable=self.menu_var,
                                 state="readonly",
                                 width=18,
                                 values=('USD', 'INR'))
currency_dropdown.grid(row=len(self.menu_items) + 1,
                       column=1,
                       padx=10,
                       pady=5)
currency_dropdown.current(0)

self.currency_var.trace_add('w', self.update_menu_prices)

order_button = ttk.Button