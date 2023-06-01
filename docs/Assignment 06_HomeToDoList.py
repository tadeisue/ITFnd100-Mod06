# ------------------------------------------------- #
# Title: Assignment_06_HomeToDoList
# Description: Learning to work with functions, global and local variables, and classes
# ChangeLog: (Who, When, What)
# Susan Tadei Dev,05/24/2023,Created Script
# ------------------------------------------------- #

# -- Data --#
fltV1 = 0.0
fltV2 = 0.0
# Declare variables and constants
#objFileName = "ToDoList.txt" # An object that represents a file
#strData = "" # A row of text data from the file
#dicRow = {} # A row of data separated into elements of a dictionary {Task,Priority}
#lstTable = [] # A dictionary that acts as a 'table' of rows
#strChoice = "" # Capture the user option selection
#row = ""

#--Processing--#

    #def read_data_from_file(file_name, list_of_rows):
     #   """ Reads data from a file into a list of dictionary rows
     #   :param file_name: (string) with name of file:
     #   :param list_of_rows: (list) you want filled with file data:
     #   :return: (list) of dictionary rows
     #   """
     #   list_of_rows.clear()  # clear current data
     #   file = open(ToDoList.txt, "r")
     #   for line in file:
     #       task, priority = line.split(",")
      #      row = {"Task": task.strip(), "Priority": priority.strip(), "Number": number.strip()}
      #      list_of_rows.append(row)
      #  file.close()
      #  return list_of_rows

    #@staticmethod
    #def add_data_to_list(task, priority, list_of_rows):
      #  """ Adds data to a list of dictionary rows

     #   :param task: (string) with name of task:
      #  :param priority: (string) with name of priority:
      #  :param list_of_rows: (list) you want to add more data to:
      #  :return: (list) of dictionary rows
      #  """
        #row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        #if strChoice.strip() == '1':
         #   print("The current items ToDo are: ")
         #   for row in lstTable:
          #      print(row["Task"] + "(" + row["Priority"] + ")")
         #   continue
        #
        #return list_of_rows

    #@staticmethod
    #def remove_data_from_list(task, list_of_rows):
     #   """ Removes data from a list of dictionary rows

     #   :param task: (string) with name of task:
     #   :param list_of_rows: (list) you want filled with file data:
     #   :return: (list) of dictionary rows
      #  """
        #
        #return list_of_rows

   # @staticmethod
   # def write_data_to_file(file_name, list_of_rows):
    #    """ Writes data from a list of dictionary rows to a File

    #    :param file_name: (string) with name of file:
     #   :param list_of_rows: (list) you want filled with file data:
     #   :return: (list) of dictionary rows
     #   """
        #
     #   return list_of_rows
     #   objFile = open(objFileName, "r")
     #   for line in objFile:
        #strData = line.split(",")
      #      dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip(), "Number": strData[2].strip()}
      #  lstTable.append(dicRow)
      #  objFile.close()

    # Main Body of Script  ------------------------------------------------------ #

    # Step 1 - When the program starts, Load data from ToDoFile.txt.
    #Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data

    # Step 2 - Display a menu of choices to the user
    #while (True):
     #   print("""
    #    Menu of Options
     #   1) Show current data.
     #   2) Add a new item.
     #   3) Remove an existing item)
     #   4) Save Data to File)
     #   5) Exit Program
    #""")
     #   strChoice = str(input("Which option would you like to perform? [1 to 4]: "))
     #   print()
        # Step 3 Show current data
        #IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
        #IO.output_menu_tasks()  # Shows menu
        #choice_str = IO.input_menu_choice()  # Get menu option

        # Step 4 - Process user's menu choice
        #if strChoice.strip() == '1':
          #  print("The current items #ToDo are: ")
         #   for row in lstTable:
                #print(row["Task"] + "(" + row["Priority"] + ")" row["Number"] + ")")
          #      continue
            #choice_str.strip() == '1':  # Add a new Task
            #task, priority = IO.input_new_task_and_priority()
            #table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
            #continue  # to show the menu

        #elif choice_str == '2':  # Remove an existing Task
          #  strKeyToRemove = input("Which TASK would you like removed? - ")
          #  blnItemRemoved = False
          #  intRowNumber = 0
          #  for row in lstTable:
           #     task, priority = dict(row).values()
           #     if task == strKeyToRemove:
            #        del lstTable[intRowNumber]
             #       blnItemRemoved = True
           #     intRowNumber += 1
           # if (blnItemRemoved == True):
           #     print("The task was removed.")
           # else:
           #     print("I'm sorry, but I could not find that task.")
            #    print("The current items ToDo are: ")
            #    for row in lstTable:
                   # print(row["Task"] + ")" + row["Priority"] + ")" row["Number"] + ")")
              #          continue
            #task = IO.input_task_to_remove()
            #table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
            #continue  # to show the menu

       # elif choice_str == '3':  # Save Data to File
        #    print("The current items ToDo are: ")
        #   for row in lstTable:
         #       print(row["Task"] + "(" + row["Priority"] + ")")
         #   if "y" == str(input("Save this data to file? (y/n) -")).strip().lower():
         #       objFile = open(objFileName, "w")
          #  for dicRow in lstTable:
        #     #objFileName.write(lstRow["Task"] + "," + lstRow["Priority"] + "\n")
           #         objFile.close()
           #         input("Data saved to file! Press the [Enter] key to return to the menu.")
            #        continue
            #table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
            #print("Data Saved!")
            #continue  # to show the menu

        #elif choice_str == '4':  # Exit Program
         #   print("Goodbye!")
         #   break  # by exiting loop
