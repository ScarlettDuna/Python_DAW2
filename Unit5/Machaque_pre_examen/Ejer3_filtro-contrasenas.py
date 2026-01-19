passwords = ["123456", "password", "admin", "qwerty", "python2024", "123"]
pass_5mas = [passw[::-1].upper() for passw in passwords if len(passw) > 5]
print(pass_5mas)
