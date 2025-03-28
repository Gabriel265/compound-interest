import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
from datetime import datetime

class CompoundInterestCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Trading Compound Interest Calculator")
        master.geometry("500x650")
        master.configure(bg='#1e1e2e')

        # Custom styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', foreground='white', background='#1e1e2e', font=('Helvetica', 12))
        style.configure('TEntry', font=('Helvetica', 12))
        style.configure('TButton', font=('Helvetica', 12))

        # Input Frame
        input_frame = ttk.Frame(master, style='TFrame')
        input_frame.pack(padx=20, pady=20, fill='x')

        # Initial Amount
        ttk.Label(input_frame, text="Initial Investment Amount ($):", style='TLabel').grid(row=0, column=0, sticky='w', pady=5)
        self.initial_amount = ttk.Entry(input_frame, width=30)
        self.initial_amount.grid(row=0, column=1, pady=5)
        self.initial_amount.insert(0, "1000")

        # Number of Trades
        ttk.Label(input_frame, text="Number of Trades:", style='TLabel').grid(row=1, column=0, sticky='w', pady=5)
        self.num_trades = ttk.Entry(input_frame, width=30)
        self.num_trades.grid(row=1, column=1, pady=5)
        self.num_trades.insert(0, "10")

        # Percentage Gain per Trade
        ttk.Label(input_frame, text="Percentage Gain per Trade (%):", style='TLabel').grid(row=2, column=0, sticky='w', pady=5)
        self.percent_gain = ttk.Entry(input_frame, width=30)
        self.percent_gain.grid(row=2, column=1, pady=5)
        self.percent_gain.insert(0, "2.5")

        # Calculate Button
        calculate_btn = ttk.Button(input_frame, text="Calculate Compound Interest", command=self.calculate)
        calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Results Frame
        self.results_frame = ttk.Frame(master, style='TFrame')
        self.results_frame.pack(padx=20, pady=10, fill='both', expand=True)

        # Results Text with Scrollbar
        results_text_container = tk.Frame(self.results_frame, bg='#2c2c3e')
        results_text_container.pack(fill='both', expand=True)

        # Vertical Scrollbar
        scrollbar = tk.Scrollbar(results_text_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Results Text
        self.results_text = tk.Text(results_text_container, height=15, width=60, 
                                    bg='#2c2c3e', fg='white', 
                                    font=('Courier', 10),
                                    yscrollcommand=scrollbar.set)
        self.results_text.pack(side=tk.LEFT, fill='both', expand=True)

        # Configure scrollbar
        scrollbar.config(command=self.results_text.yview)

        # Export Button
        export_btn = ttk.Button(input_frame, text="Export to CSV", command=self.export_to_csv)
        export_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # Store calculation results for CSV export
        self.calculation_results = []

    def calculate(self):
        try:
            # Parse inputs
            initial = float(self.initial_amount.get())
            trades = int(self.num_trades.get())
            gain_percent = float(self.percent_gain.get())

            # Clear previous results
            self.results_text.delete(1.0, tk.END)
            self.calculation_results = []

            # Calculation
            current_amount = initial
            results = [f"Initial Investment: ${initial:.2f}\n"]
            results.append(f"Trades: {trades}\n")
            results.append(f"Gain per Trade: {gain_percent}%\n\n")
            results.append("Trade-by-Trade Breakdown:\n")
            results.append("Trade\tAmount\t\tGain\n")
            results.append("-" * 40 + "\n")

            # Store header for CSV
            self.calculation_results.append([
                "Trade", "Amount", "Gain"
            ])

            for trade in range(1, trades + 1):
                gain = current_amount * (gain_percent / 100)
                current_amount += gain
                trade_result = f"{trade}\t${current_amount:.2f}\t\t+${gain:.2f}\n"
                results.append(trade_result)

                # Store for CSV
                self.calculation_results.append([
                    trade, f"{current_amount:.2f}", f"{gain:.2f}"
                ])

            # Final results
            results.append("\n" + "-" * 40 + "\n")
            results.append(f"Final Amount: ${current_amount:.2f}\n")
            total_gain_percent = ((current_amount - initial) / initial) * 100
            results.append(f"Total Gain: {total_gain_percent:.2f}%")

            # Display results
            for result in results:
                self.results_text.insert(tk.END, result)

            # Scroll to bottom
            self.results_text.see(tk.END)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")

    def export_to_csv(self):
        if not self.calculation_results:
            messagebox.showwarning("Warning", "No calculation results to export")
            return

        # Generate unique filename
        base_filename = "compound_interest_calculation"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Find a unique filename
        counter = 1
        while True:
            filename = f"{base_filename}_{timestamp}_{counter}.csv"
            if not os.path.exists(filename):
                break
            counter += 1

        # Write to CSV
        try:
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(self.calculation_results)
            
            messagebox.showinfo("Export Successful", f"Results exported to {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Could not export to CSV: {str(e)}")

def main():
    root = tk.Tk()
    app = CompoundInterestCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
