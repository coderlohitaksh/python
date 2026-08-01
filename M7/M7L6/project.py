import tkinter as tk
from tkinter import ttk, messagebox


class StationeryOrderManagement:

    def __init__(self, root):
        self.root = root
        self.root.title("Stationery Order Management App")

        self.stationery_items = {
            "Notebook": 3,
            "Pen": 1,
            "Pencil": 0.5,
            "Eraser": 0.75,
            "Marker": 2
        }

        self.exchange_rate = 82

        self.setup_background(root)

        self.frame = ttk.Frame(root, padding=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        heading = ttk.Label(
            self.frame,
            text="Stationery Order Management",
            font=("Arial", 18, "bold")
        )

        heading.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10
        )

        self.item_labels = {}
        self.item_quantities = {}

        for row, (item, price) in enumerate(
            self.stationery_items.items(),
            start=1
        ):

            label = ttk.Label(
                self.frame,
                text=f"{item} - ${price:.2f}"
            )

            label.grid(
                row=row,
                column=0,
                padx=10,
                pady=5,
                sticky="w"
            )

            entry = ttk.Entry(
                self.frame,
                width=10
            )

            entry.grid(
                row=row,
                column=1,
                padx=10,
                pady=5
            )

            self.item_labels[item] = label
            self.item_quantities[item] = entry

        row += 1

        ttk.Label(
            self.frame,
            text="Currency:"
        ).grid(
            row=row,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.currency_var = tk.StringVar(
            value="USD"
        )

        currency_box = ttk.Combobox(
            self.frame,
            textvariable=self.currency_var,
            values=["USD", "INR"],
            state="readonly",
            width=10
        )

        currency_box.grid(
            row=row,
            column=1,
            padx=10,
            pady=10
        )

        self.currency_var.trace_add(
            "write",
            self.update_prices
        )

        row += 1

        order_button = ttk.Button(
            self.frame,
            text="Place Order",
            command=self.place_order
        )

        order_button.grid(
            row=row,
            column=0,
            columnspan=2,
            pady=10
        )

        row += 1

        self.total_label = ttk.Label(
            self.frame,
            text="Total Price: $0.00",
            font=("Arial", 12, "bold")
        )

        self.total_label.grid(
            row=row,
            column=0,
            columnspan=2,
            pady=10
        )

    def setup_background(self, root):

        self.canvas = tk.Canvas(
            root,
            width=800,
            height=600
        )

        self.canvas.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        try:

            bg = tk.PhotoImage(
                file="background.png"
            )

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
    def update_prices(self, *args):

        currency = self.currency_var.get()

        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, usd_price in self.stationery_items.items():

            converted_price = usd_price * rate

            self.item_labels[item].config(
                text=f"{item} - {symbol}{converted_price:.2f}"
            )

    def place_order(self):

        total_cost = 0

        order_summary = "Stationery Order Summary\n\n"

        currency = self.currency_var.get()

        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.item_quantities.items():

            quantity = entry.get()

            if quantity.isdigit():

                quantity = int(quantity)

                if quantity > 0:

                    price = self.stationery_items[item] * rate

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

    app = StationeryOrderManagement(root)

    root.mainloop()