from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def add():
    username = input('Enter the username\n')
    pwd=input('Enter the password\n')
    with open('passwords.txt','a') as f:
        f.write(username+" | "+fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())

        
while True:
    mode = input("Enter the mode u wanna open the file in\npress q to exit\n").lower()
    if mode=='q':
        break
    if mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print("Invalid mode")
        continue
