# Escreva um programa que imprima os números de 1 a 100. Mas para múltiplos de três imprima "Fizz"
# em vez do número e para múltiplos de cinco imprima "Buzz".
# Para números múltiplos de três e cinco, imprima "FizzBuzz".

# x mod 3 = Fizz
# x mod 5 = Buzz
# x mod 15 = FizzBuzz
for x in range(1,101):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
