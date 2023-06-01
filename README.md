# Springwood_code_test

## Problem Statement
The goal of the Rule Engine is to provide the following functionalities:
1.  Configure trigger conditions based on predefined templates.
2.  Choose and apply actions to variables when trigger conditions are met.
3.  View the updated variable values after running the rule engine.

## How to Run the Application
-> Install Python 3 on your system.
Windows: Tkinter is usually included with the default Python installation,if it throws an error you need to reinstall Python and make sure to select the option to install Tcl/Tk and IDLE during the installation process.
linux: sudo apt-get install python3-tk 
Install the required dependencies by running the command: pip3 install -r requirements.txt.
Run the application: python3 app.py.

## About GUI
The GUI window will open, allowing you to interact with the Rule Engine.
Select the trigger variable, operator, and value from the dropdowns.
Click the "Evaluate Trigger" button to configure the trigger condition.
Choose the desired action from the dropdown and provide the necessary inputs.
Click the "Apply Action" button to perform the action on the variables.
To view the updated variable values, click the "Run Engine" button.
The output will be displayed in the output section of the GUI.
