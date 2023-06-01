import tkinter as tk
from tkinter import messagebox
from Trigger import *

class RuleEngineApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rule Engine")
        self.engine = RuleEngine()
        self.create_trigger_section()
        self.create_action_section()
        self.create_output_section()

    def create_trigger_section(self):
        self.trigger_frame = tk.Frame(self.window)
        self.trigger_frame.pack(pady=10)

        self.trigger_label = tk.Label(self.trigger_frame, text="Trigger:")
        self.trigger_label.grid(row=0, column=0)

        self.trigger_variable_label = tk.Label(self.trigger_frame, text="Variable:")
        self.trigger_variable_label.grid(row=0, column=1)

        self.trigger_variable_dropdown_var = tk.StringVar()
        self.trigger_variable_dropdown = tk.OptionMenu(self.trigger_frame, self.trigger_variable_dropdown_var, *self.engine.variables.keys())
        self.trigger_variable_dropdown.grid(row=0, column=2)

        self.trigger_operator_label = tk.Label(self.trigger_frame, text="Operator:")
        self.trigger_operator_label.grid(row=0, column=3)

        self.trigger_operator_dropdown_var = tk.StringVar()
        self.trigger_operator_dropdown = tk.OptionMenu(self.trigger_frame, self.trigger_operator_dropdown_var, "equals", "greater", "greater_equals", "less", "less_equals")
        self.trigger_operator_dropdown.grid(row=0, column=4)

        self.trigger_value_label = tk.Label(self.trigger_frame, text="Value:")
        self.trigger_value_label.grid(row=0, column=5)

        self.trigger_value_entry = tk.Entry(self.trigger_frame)
        self.trigger_value_entry.grid(row=0, column=6)

        self.trigger_button = tk.Button(self.trigger_frame, text="Evaluate Trigger", command=self.handle_trigger)
        self.trigger_button.grid(row=0, column=7)

    def create_action_section(self):
        self.action_frame = tk.Frame(self.window)
        self.action_frame.pack(pady=10)

        self.action_label = tk.Label(self.action_frame, text="Action:")
        self.action_label.grid(row=0, column=0)

        self.action_dropdown_var = tk.StringVar()
        self.action_dropdown = tk.OptionMenu(self.action_frame, self.action_dropdown_var, "copy", "arithmetic", "graph", command=self.handle_action_selection)
        self.action_dropdown.grid(row=0, column=1)

        self.action_source_label = tk.Label(self.action_frame, text="Source Variable:")
        self.action_source_label.grid(row=0, column=2)

        self.action_source_dropdown_var = tk.StringVar()
        self.action_source_dropdown = tk.OptionMenu(self.action_frame, self.action_source_dropdown_var, *self.engine.variables.keys())
        self.action_source_dropdown.grid(row=0, column=3)

        self.arithmetic_operator_label = tk.Label(self.action_frame, text="Operator:")
        self.arithmetic_operator_label.grid(row=0, column=4)

        self.arithmetic_operator_dropdown_var = tk.StringVar()
        self.arithmetic_operator_dropdown = tk.OptionMenu(self.action_frame, self.arithmetic_operator_dropdown_var, "+", "-", "*", "/")
        self.arithmetic_operator_dropdown.grid(row=0, column=5)

        self.arithmetic_value_label = tk.Label(self.action_frame, text="Value:")
        self.arithmetic_value_label.grid(row=0, column=6)

        self.arithmetic_value_entry = tk.Entry(self.action_frame)
        self.arithmetic_value_entry.grid(row=0, column=7)

        self.action_button = tk.Button(self.action_frame, text="Apply Action", command=self.handle_action)
        self.action_button.grid(row=0, column=8)

    def create_output_section(self):
        self.output_frame = tk.Frame(self.window)
        self.output_frame.pack(pady=10)

        self.output_text = tk.Text(self.output_frame, width=40, height=10)
        self.output_text.pack()

        self.run_button = tk.Button(self.output_frame, text="Run Engine", command=self.handle_run_engine)
        self.run_button.pack()

    def handle_trigger(self):
        trigger_variable = self.trigger_variable_dropdown_var.get()
        operator = self.trigger_operator_dropdown_var.get()
        value = self.trigger_value_entry.get()
        
        self.engine.evaluate_trigger(trigger_variable, operator, value)
        messagebox.showinfo("Trigger Configured", "Trigger configured successfully!")

    def handle_action_selection(self, action):
        if action == "arithmetic":
            self.arithmetic_operator_label.grid(row=0, column=4)
            self.arithmetic_operator_dropdown.grid(row=0, column=5)
            self.arithmetic_value_label.grid(row=0, column=6)
            self.arithmetic_value_entry.grid(row=0, column=7)
        else:
            self.arithmetic_operator_label.grid_forget()
            self.arithmetic_operator_dropdown.grid_forget()
            self.arithmetic_value_label.grid_forget()
            self.arithmetic_value_entry.grid_forget()

    def handle_action(self):
        action = self.action_dropdown_var.get()
        source_variable = self.action_source_dropdown_var.get()
        
        if action == "copy":
            destination_variable = self.action_destination_dropdown_var.get()
            self.engine.copy_variable(source_variable, destination_variable)
        elif action == "arithmetic":
            operator = self.arithmetic_operator_dropdown_var.get()
            value = self.arithmetic_value_entry.get()
            self.engine.perform_arithmetic_action(source_variable, operator, value)
        elif action == "graph":
            destination_variable = self.action_destination_dropdown_var.get()
            self.engine.draw_graph(source_variable, destination_variable)
        
        messagebox.showinfo("Action Applied", "Action applied successfully!")

    def handle_run_engine(self):
        output = ""
        for variable, value in self.engine.variables.items():
            output += f"{variable}: {value}\n"
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = RuleEngineApp()
    app.run()