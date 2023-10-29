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
