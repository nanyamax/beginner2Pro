from cryptography.fernet import Fernet
 
key_generated = False

def write_key():
  global key_generated
  if not key_generated:
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
      key_file.write(key)
    key_generated = True

write_key()

def load_key():
  file = open('key.key', 'rb')
  key = file.read()
  file.close()
  return key


key = load_key()
fer = Fernet(key)

def view():
  with open("passwords.txt", 'r') as f: 
    for line in f.readlines():
      data = (line.rstrip())
      user, passw = data.split("|")
      print('User: ',user, '| Password: ', fer.decrypt(passw.encode()).decode())


def add():
  name = input("Account name: ")
  pwd = input("Password: ")
  with open("passwords.txt", 'a') as f: 
    f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
  mode = input("Would you like to add new password or view existing password (view or add or q to quit)? ").lower()
  if mode == 'q':
    break
  if mode == 'view':
    view()
  elif mode == 'add':
    add()
  else:
    print("invalid mode.")
    continue





  # opening a file in a mode eg with open("passwords.txt", 'a') as f: this will write to the file at the end of the line if it exists or create a new new file if the file doesn't exist .
  # 'w' will create a file or overwrite the file it does exist.
  # 'r' will open the file in read mode. you can read in this mode, you cannot make any changes to the file.                    
