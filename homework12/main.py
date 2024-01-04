from collections import UserDict
from datetime import datetime, timedelta
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

class Birthday(Field):
    def __init__(self, birthday):
        try:
            self.value = datetime.strptime(birthday, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Невірний формат дня народження. Використовуйте формат 'YYYY-MM-DD'.")

class Phone(Field):
    def __init__(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.value = phone
        else:
            raise ValueError("Номер телефону повинен містити 10 цифр")

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday

        if birthday:
            self.birthday = Birthday(birthday)

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

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
            
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()

            days_left = (next_birthday - today).days
            return days_left
        else:
            return None

    def __str__(self):
        phones_str = '; '.join(str(p.value) for p in self.phones)
        birthday_str = f", День народження: {self.birthday.value}" if self.birthday else ""
        return f"Контакт: {self.name.value}, телефони: {phones_str}{birthday_str}"

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

    def iterator(self, amount):
        keys = list(self.data.keys())
        num_keys = len(keys)
        start = 0

        while start < num_keys:
            end = min(start + amount, num_keys)
            yield [self.data[key] for key in keys[start:end]]
            start = end

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            # Якщо файл не знайдено, можна ігнорувати помилку
            pass
        except Exception as e:
            print(f"Помилка при завантаженні з файлу: {e}")
    
    def search(self, search_string):
        results = []
        for record in self.data.values():
            if (search_string.lower() in record.name.value.lower() or
                    any(search_string in phone.value for phone in record.phones)):
                results.append(record)
        return results
    



record1 = Record("John Doe", "1990-05-15")
record1.add_phone("1234567890")

record2 = Record("Jane Smith")
record2.add_phone("9876543210")


address_book = AddressBook()
address_book.add_record(record1)
address_book.add_record(record2)


address_book.save_to_file('address_book.pkl')

new_address_book = AddressBook()
new_address_book.load_from_file('address_book.pkl')

results = new_address_book.search('1234567890')
for result in results:
    print(result)