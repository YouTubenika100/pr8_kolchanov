import random

def password():
    n = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    rezultat = ''
    for i in range(11):
        rezultat += random.choice(n)
    return rezultat

d = password()
print('Пароль:',d)
