import tkinter as tk
from tkinter import ttk, messagebox


class RestaurantOrderManagement:

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        self.menu_items = {
            "Pizza": 12,
            "Burger": 8,
            "Pasta": 10,
            "Sandwich": 6,
            "Coffee": 4
        }

        self.exchange_rate = 82

        self.setup_background(root)

        self.frame = ttk.Frame(root, padding=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        heading = ttk.Label(
            self.frame,
            text="Restaurant Order Management",
            font=("Arial", 18, "bold")
        )
        heading.grid(row=0, column=0, columnspan=2, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        row = 1

        for item, price in self.menu_items.items():
            label = ttk.Label(
                self.frame,
                text=f"{item} - ${price:.2f}"
            )
            label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

            entry = ttk.Entry(self.frame, width=10)
            entry.grid(row=row, column=1, padx=10, pady=5)

            self.menu_labels[item] = label
            self.menu_quantities[item] = entry

            row += 1

        ttk.Label(
            self.frame,
            text="Currency:"
        ).grid(row=row, column=0, padx=10, pady=10, sticky="w")

        self.currency_var = tk.StringVar(value="USD")

        currency_box = ttk.Combobox(
            self.frame,
            textvariable=self.currency_var,
            values=["USD", "INR"],
            state="readonly",
            width=10
        )
        currency_box.grid(row=row, column=1, padx=10, pady=10)

        self.currency_var.trace_add("write", self.update_menu_prices)

        row += 1

        order_button = ttk.Button(
            self.frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(row=row, column=0, columnspan=2, pady=10)

        row += 1

        self.total_label = ttk.Label(
            self.frame,
            text="Total Price: $0.00",
            font=("Arial", 12, "bold")
        )
        self.total_label.grid(row=row, column=0, columnspan=2, pady=10)

    def setup_background(self, root):
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        try:
            bg = tk.PhotoImage(file="background.png")
            bg = bg.subsample(2, 2)

            self.canvas.create_image(
                0,
                0,
                image=bg,
                anchor="nw"
            )

            self.canvas.image = bg

        except:
            self.canvas.create_text(
                400,
                300,
                text="Background Image Not Found",
                font=("Arial", 20),
                fill="gray"
            )
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()

        if currency == "INR":
            symbol = "₹"
            rate = self.exchange_rate
        else:
            symbol = "$"
            rate = 1

        for item, usd_price in self.menu_items.items():
            converted_price = usd_price * rate
            self.menu_labels[item].config(
                text=f"{item} - {symbol}{converted_price:.2f}"
            )

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary\n\n"

        currency = self.currency_var.get()

        if currency == "INR":
            symbol = "₹"
            rate = self.exchange_rate
        else:
            symbol = "$"
            rate = 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()

            if quantity.isdigit():
                quantity = int(quantity)

                if quantity > 0:
                    price = self.menu_items[item] * rate
                    item_cost = price * quantity
                    total_cost += item_cost

                    order_summary += (
                        f"{item} x {quantity} = "
                        f"{symbol}{item_cost:.2f}\n"
                    )

        self.total_label.config(
            text=f"Total Price: {symbol}{total_cost:.2f}"
        )

        if total_cost > 0:
            order_summary += (
                f"\nTotal Cost: {symbol}{total_cost:.2f}"
            )

            messagebox.showinfo(
                "Order Placed",
                order_summary
            )
        else:
            messagebox.showerror(
                "No Order",
                "Please order at least one item."
            )


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = RestaurantOrderManagement(root)
    root.mainloop()
    