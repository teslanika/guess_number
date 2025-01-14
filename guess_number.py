from random import randint
number = randint(1,100)
print ('Угадайте число от 1 до 100')
count = 0
while True:
    guess = int(input('Введите число:'))
    
    if guess < number:
        print ('Ваше число меньше того, что загадано.') 
        count += 1
    elif guess > number:
        print ('Ваше число больше того, что загадано.')
        count += 1
    elif guess == number:
        count += 1
        break
    
print (f'Отличная интуиция! Вы угадали число за {count} попыток :)')
