# > Operações Matemáticas (Aritméticas)

"""
    - SOMA: +
    - SUBTRAÇÃO: -
    - MULTIPLICAÇÃO: *
    - DIVISÃO: /
    - DIVISÃO INTEIRA: // 
    - RESTO DA DIVISÃO: %
    - POTÊNCIA: **
""" 

numero1 = 10
numero2 = 20

print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 // numero2) #UMA DIVISÃO INTEIRA RESULTA EM ZERO, POIS ELA IGNORA A PARTE DECIMAL, O RESULTADO SERIA 0.5
print(20 % 3)
print(2 ** 3)


#OPERADORES BOOLEANOS

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade2)          # false
print(idade1 <= idade2)         # true
print('Python' == 'python')     # false
print('banana' != 'abacaxi')    # true
print(altura1 >= altura2)       # true
print(altura2 > altura3)        # false
