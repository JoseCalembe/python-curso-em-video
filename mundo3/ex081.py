tupla=("zero","um","dois", "tres ","Quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezaseis","dezasete","dezoito","dezanove","vinte")
while True:
     num = int(input("Digite um numero de 0 a 20:"))
     while num<0 or num>20:
           num=int(input("Digite um numero de 0 a 20:"))

     if num >= 0 and num <= 20:
         print(tupla[num])
         break
print("Fim do programa")


