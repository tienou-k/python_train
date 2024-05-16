n = 10
i = 1
sum = 0
while i<=n :
    try:
        num = int(input('Entrer un entier:'))
        sum = num + sum
        i = i+1
    except:
        print('Vous devez entrer un entier')
        break