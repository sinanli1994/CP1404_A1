def main():
    user_name = input("Please enter your name: ")
    print("Welcome! {}".format(user_name))
    # Display a welcome message with the name in it
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
            required()
        elif user_choice == "C":
            completed()
        elif user_choice == "A":
            add_new()
        elif user_choice == "M":
            mark()
        elif user_choice == "Q":
            quit()
            break
        else:
            print("Invalid menu choice")
            # Error check

    print("Have a nice day :)")


def required():  # Function when user want to check the required items
    import operator
    # import the operator
    file_reader = open("list.csv", "r")
    # Open the file with the correct format
    count = 0
    total = 0

    sorted_item = sorted(file_reader, key=operator.itemgetter(2))
    # sorting the file with the item 2
    for line in sorted_item:  # using for loop to separate to sorted file
        item = str(line).split(",")  # separate to the different items
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

    file_reader.close()
    # Close the file


def completed():  # Function when user want to check the completed items
    import operator
    # import the operator
    file_reader = open("list.csv", "r")
    # Open the file with the correct format
    count = 0
    total = 0

    sorted_item = sorted(file_reader, key=operator.itemgetter(2))
    # sorting the file with the item 2
    for line in sorted_item:  # using for loop to separate to sorted file
        item = str(line).split(",")  # separate to the different items
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
    file_reader.close()
    # Close the file


def add_new():  # Function when user want to add new item
    file = open("list.csv", "a")
    # Open the file with the correct format
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
    file.write("\n" + item_name + "," + str(price) + "," + str(priority) + "," + "r")
    # Add the item into the file
    file.close()
    # Close the file
    print("{}, ${} (priority {}) added to shopping list".format(item_name, price, priority))
    # Display the added item data


def mark():  # Function when user want to mark the required item to completed item
    file_reader = open("list.csv", "r")
    file_writer = open("list.csv", "a")
    # Open the file with the correct format
    count = -1
    count1 = -1
    total = 0

    import operator
    # import the operator
    sorted_item = sorted(file_reader, key=operator.itemgetter(2))
    # sorting the file with the item 2

    for line in sorted_item:  # using for loop to separate to sorted file
        item = str(line).split(",")  # separate to the different items
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
        print("Total expected price for {} items: ${}".format(count, total))
        print("Enter the number of an item to mark as completed")
        while True:
            try:  # Let user enter the item number which user want to mark as completed item
                user_input = int(input(">>>"))
            except ValueError:
                print("Invalid input; enter a number")
            else:
                if count >= user_input >= 0:
                    file_reader.seek(0)
                    for line2 in sorted_item:  # Find the number and change the key words
                        item2 = str(line2).split(",")
                        if "r" in item2[3]:
                            count1 += 1
                            if count1 == user_input:
                                file_writer2 = open("list.csv", "w")
                                file_writer2.writelines(line2.replace(item2[3], "c").strip())
                                print("{} marked as completed".format(item2[0]))
                                file_writer2.close()
                            else:
                                file_writer.writelines("\n" + line2.strip())
                        else:
                            file_writer.writelines("\n" + line2.strip())
                    break
                else:
                    print("Invalid item number")
                    # Error check
    file_reader.close()
    file_writer.close()
    # Close the file


def quit():  # Function when user want to quit
    file_reader = open("list.csv", "r")
    file_writer = open("list.csv", "a")
    # Open the file with the correct format
    count = 0

    for line in file_reader:  # Find the completed items the delete the required items
        char = line.split(",")
        if "c" in char[3]:
            count += 1
            if count == 1:
                file_writer2 = open("list.csv", "w")
                file_writer2.writelines(line.strip())
                file_writer2.close()
            else:
                file_writer.writelines("\n" + line.strip())
        else:
            file_writer.writelines(line.replace(line, "").strip())

    print("{} items saved to items.csv".format(count))
    #Display how many items which add to the file
    file_reader.close()
    file_writer.close()
    #Close the file

main()
