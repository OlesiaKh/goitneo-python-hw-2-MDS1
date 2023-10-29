USERS = {}
 
 
def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user with given name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
    return inner
 
 
def exit_handler(_):
    return
 
 
def unknown_cmd(_):
    return "Unknown command"
 
 
def hello_handler(_):
    return "How can I help you?"
 
 
@error_handler
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f"User {name} added"
 
 
@error_handler
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f"{name}'s phone number is {phone}. The previous phone number was: {old_phone}"
 
 
@error_handler
def show_number(args):
    user = args[0]
    phone = USERS[user]
    result = f"{user}: {phone}"
    return result
 
 
def show_all(_):
    result = ""
    for name, phone in USERS.items():
        result += f"{name}: phone\n"
    return result
 
 
HANDLERS = {
    "hello": hello_handler,
    "good bye": exit_handler,
    "close": exit_handler,
    "exit": exit_handler,
    u"add": add_user,
    u"change": change_phone,
    u"show all": show_all,
    u"phone": show_number
 
}
 
 
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lstrip()
    try:
        handler = HANDLERS[cmd.lower()]
    except KeyError:
        if args:
            cmd = cmd + " " + args[0]
            args = args[1:]
        handler = HANDLERS.get(cmd.lower(), unknown_cmd)
    return handler, args
 
 
def main():
    while True:
        user_input = input(">")
        handler, *args = parse_input(user_input)
        result = handler(*args)
        if not result:
            print("Good bye!")
            break
        print(result)
 
 
if __name__ == "__main__":
    main()



HW2/part 2





from collections import UserDict


class Field:
    """Fields: name, phone"""
 
    def __init__(self, value):
        self.value = value
 
 
class Name(Field):
    pass
 
 
class Phone(Field):
    """Phone """
 
    def __eq__(self, other: object) -> bool:
        return self.value == other.value
 
    def __str__(self):
        return f"Phone:{self.value}"
 
 
class Record:
    """Records.
    Name is unique, more than one phone is possible"""
 
    def __init__(self, name: str, phones: list[str] = None) -> None:
        if phones is None:
            self.phones = []
        else:
            self.phones = [Phone(p) for p in phones]
        self.name = Name(name)
 
    def add_phone(self, phone_number: str) -> None:
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)
 
    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
 
    def delete_phone(self, phone: str) -> None:
        phone_to_delete = self.find_phone(phone)
        self.phones.remove(phone_to_delete) if phone_to_delete else None
 
    def edit_phone(self, old_phone, new_phone) -> None:
        new_phone = Phone(new_phone)
        phone_to_remove = self.find_phone(old_phone)
        if phone_to_remove:
            self.phones.remove()
            self.phones.append(new_phone)
 
    def __str__(self):
        return f"Name: {self.name.value}, phone {'; '.join(p.value for p in self.phones)}"
 
    def __repr__(self) -> str:
        return (
            f"Name: {self.name.value}, phone {[p.value for p in self.phones]}"
        )
 
 
class AddressBook(UserDict):
    """All contacts"""
 
    def add_record(self, rec: Record) -> None:
        # new_record = Record(record[0], record[1:])
        self.data[rec.name.value] = rec
 
    def find_record(self, value: str):
        return self.data.get(value)
 
    def delete_record(self, value: str) -> None:
        self.data.pop(value)
 
    def __str__(self):
        return str(self.data)
 
 
def main():
    book = AddressBook()
    rec = Record("Andrew")
    book.add_record(Record("Daniel", ("999 77 77 77",)))
    book.add_record(Record("John", ("999 99 99 99", "999 888 88 88")))
    book.add_record(rec)
    print(book)
    record = book.find_record("John")
    book.delete_record("Daniel")
 
    print("#" * 10)
    print(book)
    print(record)
    print("\n")
    print("#" * 10)
    record.delete_phone("999 99 99 99")
    record.edit_phone("999 77 77 77", "111 77 77 77")
    record.add_phone(" 000 00 00 00")
    record.add_phone("111 11 11 11")
    print(record)
 
 
if __name__ == "__main__":
    main()
