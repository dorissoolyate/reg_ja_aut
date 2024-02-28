import random
import string

def gen_password(pikkus=12)->any:
    """Genereerib random salasona mis on 12 sumboli pikk"""
    sumbolid=string.ascii_letters+string.digits+string.punctuation
    return "".join(random.choice(sumbolid) for _ in range(pikkus))

def check_password_strength(password):
    """Kontrollib salasona tugevust."""
    has_digit=any(char.isdigit() for char in password)
    has_lower=any(char.islower() for char in password)
    has_upper=any(char.isupper() for char in password)
    has_special=any(char in string.punctuation for char in password)
    return has_digit, has_lower, has_upper, has_special

def registr(username:any, password:any, usernames:any, passwords:any)->any:
    """Registreerib uue kasutaja"""
    while True:
        if username in usernames:
            print("Kasutajanimi on juba v?etud!")
            username = input("Sisesta uus kasutajanimi: ")
        else:
            if check_password_strength(password):
                usernames.append(username)
                passwords.append(password)
                print("Kasutaja registreeritud edukalt!")
                break
            else:
                print("Parool ei vasta tugevuse n?uetele!")
                password = input("Sisesta uus parool: ")
        
def login(username:any, password:any, usernames:any, passwords:any)->any:
    """Autoriseerib kasutajat"""
    if username in usernames:
        index=usernames.index(username)
        if passwords[index]==password:
            print("Autoriseerimine ?nnestus")
        else:
            print("Vale parool")
    else:
        print("Sellist kasutajat ei eksisteeri")           

def muuda_password(username, vana_password, uus_password, usernames, passwords)->any:
    """Muudab passwordi"""
    if username in usernames:
        index=usernames.index(username)
        if passwords[index]==vana_password:
            if check_password_strength(uus_password):
                passwords[index]=uus_password
                print("Parool on muudetud")
            else:
                print("Uus parool ei vasta tugevuse n?uetele")
        else:
            print("Vale vana parool!")
    else:
        print("Sellist kasutajat ei eksisteeri!")
        
def forgot_password(username, usernames, passwords):
    """Uuendab salasona kuna vana oli unustatud"""
    if username in usernames:
        index=usernames.index(username)
        uus_password=gen_password()
        passwords[index] = uus_password
        print(f"Uus parool kasutajale '{username}': {uus_password}")
    else:
        print("Sellist kasutajat ei eksisteeri!")