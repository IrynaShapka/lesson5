## Ім'я змінної
# text = "-1478542"
# print(type(text))
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.islower())
# print(text.isupper())
# print(text.startswith('d'))
# print(text.endswith('2'))

# # Модифікований калькулятор

# text = input("Want to count? : ")
#
# while text == 'YES':
#     if text == 'YES':
#         number1 = float(input("Enter a number n1: "))
#         number2 = float(input("Enter a number n2: "))
#         action = input("Enter an action: ")
#         n1 = number1
#         n2 = number2
#         a = action
#         if a == '+':
#             print(n1+n2)
#         elif a == '-':
#             print(n1 - n2)
#         elif a == '*':
#             print(n1 * n2)
#         elif a == ':':
#             if number2 != 0:
#                 print(n1 / n2)
#             else:
#                 print("Result / : Error")
#         text = input("Want to count? : ")
# else:
#     print('END')

#hashtag

import string

text = str(input())
print(type(text))
print(text.isalpha())
text1 = text.replace("!",  "").replace("?", "").replace(",", "").replace(".", "")
print(text1)
text2 = text1.title()
print(text2)
text3 = text2.replace(' ', '')
print(text3)
text4 = '#' + text3
print(text4)
print(len(text4))
if len(text4) > 140:
    print("hashtag:", text4[0:140])
else:
    print("hashtag:", text4)


