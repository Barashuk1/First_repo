def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return f"Input error: {str(e)}"
    return wrapper

contacts = {}

@input_error
def user_hello():
    return "How can I help you?"

@input_error
def user_add(command):
    _, name, phone = command.split()
    contacts[name] = int(phone)
    return f"Contact {name} added with phone {phone}"

@input_error
def user_change(command):
    _, name, phone = command.split()
    contacts[name] = int(phone)
    return f"Phone number for {name} changed to {phone}"

@input_error
def user_phone(command):
    _, name = command.split()
    return f"The phone number for {name} is {contacts[name]}"

@input_error
def user_show_all():
    if not contacts:
        return "No contacts found."
    print("{:<15}|{:<15}".format("name", "phone"))
    print("¯" * 15 + "|" + "¯" * 15)
    result = "\n".join(["{:<15}|{:<15}".format(name, phone) for name, phone in contacts.items()])
    return result

def user_help():
    result = ""
    result += "{:<10}|{:>20}".format("add", "add name phone") + '\n'
    result += "{:<10}|{:>20}".format("change", "change name phone") + '\n'
    result += "{:<10}|{:>20}".format("hello", "just hello") + '\n'
    result += "{:<10}|{:>20}".format("phone", "phone name") + '\n'
    result += "{:<10}|{:>20}".format("add", "add name phone") + '\n'
    result += "{:<10}|{:>20}".format("show all", "show all contacts") + '\n'
    result += "{:<10}|{:>20}".format("good bye", "exit") + '\n'
    result += "{:<10}|{:>20}".format("close", "exit") + '\n'
    result += "{:<10}|{:>20}".format("exit", "exit") + '\n'

    return result

def main():
    print("Hello! Enter your command")

    while True:
        user_input = input(">>> ").lower()

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            response = user_hello()
        elif user_input.startswith("add"):
            response = user_add(user_input)
        elif user_input.startswith("change"):
            response = user_change(user_input)
        elif user_input.startswith("phone"):
            response = user_phone(user_input)
        elif user_input == "show all":
            response = user_show_all()
        elif user_input == "help":
            response = user_help()
        else:
            response = "Unknown command. Please try again."

        print(response)

if __name__ == "__main__":
    main()
