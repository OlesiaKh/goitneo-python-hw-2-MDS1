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

