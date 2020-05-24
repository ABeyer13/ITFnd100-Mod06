# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# ABeyer, 5.22.2020, Modified code to complete assignment 6
# ABeyer, 5.23.2020, Continued to modify code, watched RRoot's video
# ABeyer, 5.24.2020, Watched David's video, finished assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
strKeyToRemove = ""


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        lstTable.clear()  # clear current data
        file = open(strFileName, "r")
        for line in file:
            strTask, strPriority = line.split(",")
            row = {"Task": strTask.strip(), "Priority": strPriority.strip()}
            lstTable.append(row)
        file.close()
        return lstTable, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        strTask, strPriority = IO.input_new_task_and_priority()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        return lstTable, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        strKeyToRemove = IO.input_task_to_remove()
        for dicRow in lstTable:
            if dicRow["Task"].lower() == strKeyToRemove.lower():
                lstTable.remove(dicRow)
        return strKeyToRemove, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        objFile = open(strFileName, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        return lstTable, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        return strTask, strPriority

    @staticmethod
    def input_task_to_remove():
        strKeyToRemove = input("Which TASK would you like removed? - ")
        return strKeyToRemove


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        Processor.remove_data_from_list(strKeyToRemove, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName,lstTable)
            IO.input_press_to_continue("Data saved!")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable.clear()  # clear current data
            file = open(strFileName, "r")
            for line in file:
                strTask, strPriority = line.split(",")
                row = {"Task": strTask.strip(), "Priority": strPriority.strip()}
                lstTable.append(row)
            file.close()
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
