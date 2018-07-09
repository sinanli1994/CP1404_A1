import operator  # import the operator
import csv  # import the csv file


def main():
    file_opener = open("list.csv")  # Open the file
    file_reader = csv.reader(file_opener)  # Read the file

    items_list = sorted(file_reader, key=operator.itemgetter(2))
    # Import items of the file to the list and sort the list with the priority of items

    user_name = input("Please enter your name: ")
    print("Welcome! {}".format(user_name))
    # Display a welcome message with the user name
    print("Shopping List 1.0 - by Lindsay Ward\n3 items loaded from items.csv")

    menu = """
    Menu:
    R - List required items
    C - List completed items
    A - Add new item
    M - Mark an item as completed
    Q - Quit
    """

    while True:
        print(menu)
        # Display a menu for the user to choose from
        user_choice = input(">>>").upper()
        # Let user enter the choice, convert it to the upper case
        # Call different functions when user enter different choice
        if user_choice == "R":
            required(items_list)
        elif user_choice == "C":
            completed(items_list)
        elif user_choice == "A":
            add_new(items_list)
        elif user_choice == "M":
            mark(items_list)
        elif user_choice == "Q":
            quit(items_list)
            break
        else:
            print("Invalid menu choice")
            # Error check

    print("Have a nice day :)")


def required(items_list):  # Function when user want to check the required items
    count = 0
    total = 0

    required_list = sorted(items_list, key=operator.itemgetter(2))
    # sorting the list with the priority of items

    for item in required_list:  # using for loop to separate to required list
        if "r" in item[3]:  # When "r" in item 3, then count, calculate and print the required items
            count += 1
            total += float(item[1])
            if count == 1:
                print("Required items:")
                print("{}.{:40} $\t{:5}({})".format(count - 1, item[0], item[1], item[2], item[3]))
            else:
                print("{}.{:40} $\t{:5}({})".format(count - 1, item[0], item[1], item[2], item[3]))
    if count == 0:  # If total count = 0, then means no required item
        print("No required items")
    else:  # Else print total price of required items
        print("Total expected price for {} items: ${}".format(count, total))


def completed(items_list):  # Function when user want to check the completed items
    count = 0
    total = 0

    completed_list = sorted(items_list, key=operator.itemgetter(2))
    # sorting the list with the priority of items

    for item in completed_list:  # using for loop to separate to completed list
        if "c" in item[3]:  # When "c" in item 3, then count, calculate and print the completed items
            count += 1
            total += float(item[1])
            if count == 1:
                print("Completed items:")
                print("{}.{:40} $\t{:5}({})".format(count - 1, item[0], item[1], item[2], item[3]))
            else:
                print("{}.{:40} $\t{:5}({})".format(count - 1, item[0], item[1], item[2], item[3]))
    if count == 0:  # If total count = 0, then means no completed item
        print("No completed items")
    else:
        print("Total expected price for {} items: ${}".format(count, total))
        # Else print total price of completed items


def add_new(items_list):  # Function when user want to add new item
    item_name = input("Item name:")
    # Let user enter the item name
    while item_name == "":
        print("Input can not be blank")
        item_name = input("Item name:")
    # Error check
    while True:
        try:
            price = float(input("Price: $"))  # Let user enter the price of item
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            if price <= 0:
                print("Price must be >= $0")
            else:
                break
    # Error check
    while True:
        try:
            priority = int(input("Priority: "))  # Let user enter the price of item
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            if priority == 1 or priority == 2 or priority == 3:
                break
            else:
                print("Priority must be 1, 2 or 3")
    # Error check

    new_item = [item_name, str(price), str(priority), "r"]  # Create a list with new item
    items_list.append(new_item)  # Appending the new list to the item list

    print("{}, ${} (priority {}) added to shopping list".format(item_name, price, priority))
    # Display the added item data


def mark(items_list):  # Function when user want to mark the required item to completed item
    count = -1
    count1 = -1
    total = 0

    required_list = sorted(items_list, key=operator.itemgetter(2))
    # sorting the list with the priority of items

    for item in required_list:  # using for loop to separate to required list
        if "r" in item[3]:  # When "r" in item 3, then count, calculate and print the required items
            count += 1
            total += float(item[1])
            if count == 0:
                print("Required items:")
                print("{}.{:40} $\t{:5}({})".format(count, item[0], item[1], item[2], item[3]))
            else:
                print("{}.{:40} $\t{:5}({})".format(count, item[0], item[1], item[2], item[3]))
    if count == -1:  # If total count = 0, then means no required item
        print("No required items")
    else:  # Else print total price of required items
        print("Total expected price for {} items: ${}".format(count + 1, total))
        print("Enter the number of an item to mark as completed")
        while True:
            try:  # Let user enter the item number which user want to mark as completed item
                user_input = int(input(">>>"))
            except ValueError:
                print("Invalid input; enter a number")
            else:
                if count >= user_input >= 0:
                    for item2 in required_list:  # Find and mark the item in the list, then print the completed item
                        if "r" in item2[3]:
                            count1 += 1
                            if count1 == user_input:
                                item2[3] = "c"  # Using "c" instead of "r" in the list when user chooses the item
                                print("{} marked as completed".format(item2[0]))
                                # Display the marked item
                    break
                else:
                    print("Invalid item number")
                    # Error check


def quit(items_list):  # Function when user want to quit
    file_writer = open("list.csv", "a")
    # Open the file with the correct format
    count = 0

    for item in items_list:  # Find the completed items and save to the csv file
        if "c" in item[3]:
            count += 1
            if count == 1:
                file_writer2 = open("list.csv", "w")
                file_writer2.writelines(item[0] + "," + item[1] + "," + item[2] + "," + "c")
                file_writer2.close()
            else:
                file_writer.writelines("\n" + item[0] + "," + item[1] + "," + item[2] + "," + "c")
        else:
            file_writer.writelines("")
    if count == 0:
        file_writer2 = open("list.csv", "w")
        file_writer2.close()

    print("{} items saved to items.csv".format(count))
    # Display how many items which add to the file
    file_writer.close()
    # Close the file


main()
