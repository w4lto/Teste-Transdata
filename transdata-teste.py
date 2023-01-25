#O codigo abaixo considera o valor de 1 real como moeda, sendo assim desconsiderei

print("Digite o valor inteiro a ser sacado:")

N = int(input())

notas = [100,50,20,10,5,2]
print ("R$ %d:"%(N))
for x in notas:
    if(N%x!=1):
        print ("O valor sacado sera dividido nas seguintes notas %i nota(s): de R$ %.2f"%((N/x),x))
        N %= (x)

#O codgio abaixo considera o valor de 1 real como cedula, sendo assim foi considerado

"""
print("Digite o valor a ser sacado")

N = int(input())

notas = [100,50,20,10,5,2,1]
print ("R$ %d:"%(N))
for x in notas:
    print ("O valor sacado sera dividido nas seguintes notas %i nota(s) de R$ %.2f"%((N/x),x))
    N %= (x)
"""
