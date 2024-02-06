from abc import ABC, abstractmethod

class User_Interface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass
    
    @abstractmethod
    def display_notes(self, notes):
        pass
    
    @abstractmethod
    def display_commands(self, commands):
        pass

class Console_User_Interface(User_Interface):
    def display_contacts(self, contacts):
        for account in contacts:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)
    
    def display_notes(self, notes):
        for note in notes:
            print(f"Note: {note}")
    
    def display_commands(self, commands):
        print("Available commands:")
        for command in commands:
            print(command)

class Web_User_Interface(User_Interface):
    def display_contacts(self, contacts):
        # Логіка виведення контактів на веб-сторінці
        pass
    
    def display_notes(self, notes):
        # Логіка виведення нотаток на веб-сторінці
        pass
    
    def display_commands(self, commands):
        # Логіка виведення команд на веб-сторінці
        pass