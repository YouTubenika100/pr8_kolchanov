import random

def password():
    n = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    I = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rezultat = ''
    for i in range(11):
        rezultat += random.choice(n+I)
    return rezultat

d = password()
print('Пароль:',d)
