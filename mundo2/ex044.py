num=int(input('Digite um numero inteiro: '))
print("1.Hexadecimal")
print("2.octal")
print("3.Binario")
usuario=int(input('Escolha a base de conversao: '))
if usuario==1:
   print(f'Hexadecimal: {hex(num)[2:]}')
elif usuario==2:
     print(f'Octal: {oct(num)[2:]}')
elif usuario==3:
     print(f'Binario:{bin(num)[2:]}')
else:
     print('Escolha invalida!')

