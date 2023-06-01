import matplotlib.pyplot as plt

class RuleEngine:
    def __init__(self):
        self.variables = {
            "Username": "Himanshu",
            "Age": 21,
            "Weight": 60,
            "RunningKms": 2,
            "WaterIntake": 8
        }

    def set_variable(self, variable, value):
        self.variables[variable] = value

    def copy_variable(self, source_variable, destination_variable):
        if source_variable in self.variables:
            self.variables[destination_variable] = self.variables[source_variable]

    def perform_arithmetic_action(self, source_variable, operator, value):
        if source_variable in self.variables:
            try:
                value = float(value)
                if operator == "+":
                    self.variables[source_variable] += value
                elif operator == "-":
                    self.variables[source_variable] -= value
                elif operator == "*":
                    self.variables[source_variable] *= value
                elif operator == "/":
                    self.variables[source_variable] /= value
            except ValueError:
                messagebox.showerror("Error", "Invalid value for arithmetic operation.")

    def draw_graph(self, source_variable, destination_variable):
        if source_variable in self.variables and destination_variable in self.variables:
            x = self.variables[source_variable]
            y = self.variables[destination_variable]

            plt.plot(x, y)
            plt.xlabel(source_variable)
            plt.ylabel(destination_variable)
            plt.title(f"Graph of {destination_variable} vs {source_variable}")
            plt.show()
        else:
            messagebox.showerror("Error", "Invalid variables for graph drawing.")

    def evaluate_trigger(self, trigger_variable, operator, value):
        if trigger_variable in self.variables:
            try:
                value = float(value)
                if operator == "equals":
                    return self.variables[trigger_variable] == value
                elif operator == "greater_than":
                    return self.variables[trigger_variable] > value
                elif operator == "greater_than_or_equals":
                    return self.variables[trigger_variable] >= value
                elif operator == "less_than":
                    return self.variables[trigger_variable] < value
                elif operator == "less_than_or_equals":
                    return self.variables[trigger_variable] <= value
            except ValueError:
                return False
        return False



