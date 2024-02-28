from regautmodul import *

usernames=["user1", "user2"]
passwords=["password1", "password2"]
while True:
    print("\nВыберите действие: \n1. Регистрация\n2. Авторизация \n3. Изменение пароля \n4. Забыл пароль \n5. Выход")
    vastus=int(input())
    if vastus==1:
        username=input("Sisesta username: ")
        password_valik=input("Kasutaja loob passwordi ise voi automaatse parooli genereerimise (ise/auto): ")
        if password_valik.lower() == "ise":
            password = input("Sisesta password: ")
        elif password_valik.lower() == "auto":
            password = gen_password()
            print(f"Genereeritus passowrd: {password}")
        else:
            print("Vale valik!")
        registr(username, password, usernames, passwords)
    elif vastus==2:
        username=input("Sisesta username: ")
        password=input("Sisesta password: ")
        login(username, password, usernames, passwords)
    elif vastus==3:
        username = input("Sisesta username: ")
        old_password = input("Sisesta vana password: ")
        new_password = input("Sisesta uus password: ")
        muuda_password(username, old_password, new_password, usernames, passwords)
    elif vastus==4:
        username = input("Sisesta username: ")
        forgot_password(username, usernames, passwords)

    elif vastus==5:
        print("Too lopp.")
        break

    else:
        print("Vale valik")    