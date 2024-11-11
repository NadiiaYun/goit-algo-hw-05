from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().casefold()
    return cmd, *args

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:            
            return func(*args, **kwargs)
        
        except ValueError:  
            return "Enter the argument for the command"
        
        except KeyError:               
            return f'There is no contact with the name "{args[0][0]}"'

        except IndexError:            
            return "Enter 1 argument (name) for the command"        
        
    return inner

@input_error
def add_contact(args, contacts):           
    name, phone = args      
    contacts[name] = phone            
    return "Contact added"

@input_error
def change_contact(args, contacts):
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
        return f'{name}: {phone}'
    else:
        raise KeyError    


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
            for key, value in contacts.items():
                print(key+":", value)
            print("All contacts showed")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
