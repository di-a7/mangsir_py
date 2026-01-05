# todo:
# Accounting program
# create a dictionary with username and password where username is key and password is value
# create a dictionary with username and bank_balance where username is key and bank_balance is value
# get user ko username and password 
# check if the username exists and the password matches . if yes print login successful else print login failed
# if login is successful, show 2 options, 1. Show user details, 2. Add Balance
# if user choice 1, show user details (username and bank balance)
# if user choice 2, get amount to add from user, add the amount to bank balance and show updated bank balance

users = {"arun": "1234", "sita": "4321", "ram": "1111"}
balances = {"arun": 5000, "sita": 3000,  "ram": 7000}

def show_user_detail(username):
   blc = balances[username]
   print(f"""Name: {username}
Balance: {blc}""")

def add_balance(username):
   amt = int(input("Enter amount: "))
   init = balances[username]
   total = amt + init
   return total

def login(username, password):
   if username in users and password == users[username]:
      print("Login Successful.")
      while True:
         choice = input("""1. Show user detail
   2. Add balance
   3. Exit""")
         if choice == "1":
            show_user_detail(username)
         elif choice == "2":
            total = add_balance(username)
            print(f"Your New Balance: {total}")
         elif choice == "3":
            print("Exiting....")
            break
         else:
            print("Invalid choice")
   else:
      print("Invalid Credentials")

# Start Program
name = input("Enter username: ")
passkey = input("Enter password: ")

login(name,passkey)