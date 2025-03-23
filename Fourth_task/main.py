def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Please provide only name and phone."
    name = args[0]
    if name in contacts:
        return f"The {name}'s contact is already exists please try another name"
    else:
        name, phone = args
        contacts[name] = phone
        return "Contact added."

def find_contact(args, contacts):
    if len(args) != 1:
        return "Invalid arguments. Please provide only name to find the phone number."
    name = args[0]
    if name in contacts:
        return f"{name}'s number us {contacts[name]}"
    else:
        return f"{name}'s number wasn't found"
    
def update_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Please provide name and phone."
    name = args[0]
    new_number = args[1]
    if name in contacts:
        contacts[name] = new_number
        return "Contact updated"
    else:
        return f"{name} was't found"

def show_all(contacts, all_contacts):
    if len(contacts) >= 1:
        for contact in contacts:
            all_contacts += str(f"Name: {contact}, number: {contacts[contact]}") + "\n"
        return all_contacts.rstrip('\n') #remove the last new line.
    else:
        return "No contacts have been added yet"




def main():
    contacts = {}
    print("""
            _____             .___    .__              _____   
  /     \   ____   __| _/_ __|  |   ____     /  |  |  
 /  \ /  \ /  _ \ / __ |  |  \  | _/ __ \   /   |  |_ 
/    Y    (  <_> ) /_/ |  |  /  |_\  ___/  /    ^   / 
\____|__  /\____/\____ |____/|____/\___  > \____   |  
        \/            \/               \/       |__|  
  ________ ________  .______________                  
 /  _____/ \_____  \ |   \__    ___/                  
/   \  ___  /   |   \|   | |    |                     
\    \_\  \/    |    \   | |    |                     
 \______  /\_______  /___| |____|                     
        \/         \/                                 
          
    """)
    print("Welcome to the assistant bot!")
    print("""
Please use the following commands:
1. Hello
2. Add
3. Phone
4. Update
5. All
6. Close or Exit
""")
    while True:
        user_input = input("Enter a command: ")
        all_contacts = ""
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(find_contact(args, contacts))
        elif command == "update":
            if update_contact(args,contacts):
                print(update_contact(args, contacts))
            else:
                print("")
            
        elif command == "all":
            print(show_all(contacts, all_contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()