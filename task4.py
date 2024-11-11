from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().casefold()
    return cmd, *args

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            #print(f"Викликається функція: {func.__name__}: {args}")
            return func(*args, **kwargs)
        
        except ValueError:
            msg = "Enter 2 arguments for the command. "

            if func.__name__ == "add_contact":
                msg += "The right command format: add name phone"

            if func.__name__ == "change_contact":
                msg += "The right command format: change name phone"            

            return msg
        
        except KeyError:               
            return f'There is no contact with the name "{args[0][0]}"'

        except IndexError:            
            return "Enter just 1 argument for the command. The right command format: phone name"
        
        except TypeError:
            return 'The name cannot be a number'
        
        except RuntimeError:
            msg = "RuntimeError"
            if func.__name__ == "add_contact":
                msg = f'Contact with the name "{args[0][0]}" already exists'
            return msg
    return inner

@input_error
def add_contact(args: list, contacts: dict) -> str: 
    if len(args) != 2:
        raise ValueError
        
    name, phone = args   
    
    if name.isdigit():
        raise TypeError
    
    if name in contacts: 
        raise RuntimeError
    else: 
        contacts[name] = phone            
        return "Contact added"    

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    
    name, phone = args
    
    if name in contacts:
        contacts[name] = phone            
        return "Contact updated"
    else: 
        raise KeyError

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    
    name = args[0]   

    if name in contacts:
        phone = contacts.get(name) 
        return f'The phone number for the contact "{name}" is {phone}'
    else:
        raise KeyError
    
def show_all(contacts):
    for key, value in contacts.items():
        print(key+":", value)
    #print(contacts)
    return "All contacts showed"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)        

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args,contacts))

        elif command == "change":
            print(change_contact(args,contacts))

        elif command == "phone":
            print(show_phone(args,contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()