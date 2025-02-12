# from database2 import cards

# print("==============WELCOME TO ATM==============")
# while True:
#     user_or_admin = int(input("1.User\n2.Admin\n0.Exit\n>>:"))
#     if user_or_admin == 1:
            
#         card_number = int(input("Enter card number: "))
#         card_password = int(input("Enter card password: "))

#         card = cards.get(card_number)
#         if card:
#             password = card.get("password")
#             if password == card_password:
#                 while True:
#                     choice = int(input("1.Pul yechish💸\n2.Pul o'tkazish\n3.Parolni o'zgartirish\n4.Show balance\n0.Exit\n>>:"))
#                     if choice == 1:
#                         price = int(input("Enter price: "))
#                         if card['balance']>= price:
#                             card['balance'] -= price
#                             print("Withdrawal successful✅")
#                         else:
#                             print("Insufficient funds❌")
#                     elif choice == 2:
#                         pass
#                     elif choice == 3:
#                         old_password = int(input("Enter old password: "))
#                         if old_password == password:
#                             new_password = int(input("Enter new password: "))
#                             card['password'] = new_password
#                             print("Password changed successfully✅")
#                     elif choice == 4:
#                         print(f"Balance: {card['balance']}")
#                     elif choice == 0:
#                         break
#             else:
#                 print("Password incorrect❌")
                
#         else:
#             print("Card not found❌")

#     elif user_or_admin == 2:
#         print("==============ADMIN PANEL==============")
#     elif user_or_admin == 0:
#         print("Goodbye👋")
#         break
    
    
# function

# def salom():
#     return "Salom Ketmon"

# s = salom()
# print(s)

# def salom(ism: str):
#     print(f"Salom {ism}")

# name = input("enter name: ")
# salom(name)



# def daraja(son: int):
#     son = son ** 2

# a = 5
# daraja(son=a)
# print(a)




# def summa(a,b):
#     print(a+b)


# a = int(input("Enter son1: "))
# b = int(input("Enter son2: "))
# summa(a,b)