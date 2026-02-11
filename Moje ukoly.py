registrovani = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

user = input("username: ")
password = input("password: ")

print(registrovani.get("ann"))