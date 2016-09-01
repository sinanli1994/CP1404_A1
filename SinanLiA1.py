def main():
    user_name = input("Please enter your name: ")
    print("Welcome! {}".format(user_name))
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
        user_choice = input(">>>").upper()
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
            print("Invalid input")

    print("Have a nice day :)")


def required():
    file_reader = open("list.csv", "r")

    count = 0
    total = 0

    for line in file_reader:
        char = line.split(",")
        if "r" in char[3]:
            count += 1
            total += float(char[1])
            print("{}.{:40} $\t{:5}({})".format(count - 1, char[0], char[1], char[2], char[3]))
    if count == 0:
        print("No required items")
    else:
        print("Total expected price for {} items: ${}".format(count, total))

    file_reader.close()


def completed():
    file_reader = open("list.csv", "r")

    count = 0
    total = 0

    for line in file_reader:
        char = line.split(",")
        if "c" in char[3]:
            count += 1
            total += float(char[1])
            print("{}.{:40} $\t{:5}({})".format(count - 1, char[0], char[1], char[2], char[3]))
    if count == 0:
        print("No completed items")
    else:
        print("Total expected price for {} items: ${}".format(count, total))

    file_reader.close()


def add_new():
    file = open("list.csv", "a")

    item_name = input("Item name:")

    while item_name == "":
        print("Input can not be blank")
        item_name = input("Item name:")

    while True:
        try:
            price = float(input("Price: $"))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            if price <= 0:
                print("Price must be >= $0")
            else:
                break

    while True:
        try:
            priority = int(input("Priority: "))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            if priority == 0 or priority == 1 or priority == 2:
                break
            else:
                print("Priority must be 1, 2 or 3")

    file.write("\n" + item_name + "," + str(price) + "," + str(priority) + "," + "r")

    file.close()

    print("{}, ${} (priority {}) added to shopping list".format(item_name, price, priority))


def mark():
    file_reader = open("list.csv", "r")
    file_writer = open("list.csv", "a")

    count = -1
    count1 = -1
    total = 0

    for line in file_reader:
        char = line.split(",")
        if "r" in char[3]:
            count += 1
            total += float(char[1])
            print("{}.{:40} $\t{:5}({})".format(count, char[0], char[1], char[2], char[3]))
    if count == 0:
        print("No required items")
    else:
        print("Total expected price for {} items: ${}".format(count, total))
        while True:
            try:
                user_input = int(input("Enter the number of an item to mark as completed\n>>>"))
            except ValueError:
                print("Invalid input; enter a number")
            else:
                if count >= user_input >= 0:
                    file_reader.seek(0)
                    for line2 in file_reader:
                        char2 = line2.split(",")
                        if "r" in char2[3]:
                            count1 += 1
                            if count1 == user_input:
                                file_writer2 = open("list.csv", "w")
                                file_writer2.writelines(line2.replace(char2[3], "c").strip())
                                print("{} marked as completed".format(char2[0]))
                                file_writer2.close()
                            else:
                                print(line2)
                                file_writer.writelines("\n" + line2.strip())
                        else:
                            file_writer.writelines("\n" + line2.strip())
                    break
                else:
                    print("Invalid item number")

    file_reader.close()
    file_writer.close()


def quit():
    file_reader = open("list.csv", "r")
    file_writer = open("list.csv", "a")

    count = 0

    for line in file_reader:
        char = line.split(",")
        if "r" in char[3]:
            file_writer2 = open("list.csv", "w")
            file_writer2.writelines(line.replace(line, "").strip())
            file_writer2.close()
        else:
            count += 1
            file_writer.writelines(line)
    print("{} items saved to items.csv".format(count))

    file_reader.close()
    file_writer.close()


main()
