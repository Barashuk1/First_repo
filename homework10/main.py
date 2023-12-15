from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.value = phone
        else:
            raise ValueError("Номер телефону повинен містити 10 цифр")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_str = str(phone)
        for ph in self.phones:
            if str(ph.value) == phone_str:
                self.phones.remove(ph)
                break
        else:
            raise ValueError(f"Телефон {phone} не знайдено у записі.")

    def edit_phone(self, prev_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone.value) == str(prev_phone):
                self.phones[i] = Phone(new_phone)
                break
        else:
            raise ValueError(f"Телефон {prev_phone} не знайдено у записі.")
        
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def __str__(self):
        return f"Контакт: {self.name.value}, телефони: {'; '.join(str(p.value) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, value):
        self.data[value.name.value] = value

    def find(self, name):
        for record in self.data.values():
            if record.name.value == name:
                return record

    def delete(self, name):
        keys_to_delete = [key for key, record in self.data.items() if record.name.value == name]
        for key in keys_to_delete:
            self.data.pop(key)

