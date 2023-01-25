INF = 0x3f3f3f3f
LIM = 5000

notas = [2, 5, 10, 20, 50, 100]

memo = []
menor = []
for i in range(len(notas) + 1):
    l = []
    for j in range(LIM + 1):
        l.append(-1)
    menor.append(l.copy())
    memo.append(l)

def dp(pos, rem):
    if rem == 0 and pos == len(notas):
        return 0
    if rem < 0 or pos >= len(notas):
        return INF

    if memo[pos][rem] != -1:
        return memo[pos][rem]

    cnt = 0
    ret = INF
    while rem - cnt * notas[pos] >= 0:

        if ret > dp(pos + 1, rem - cnt * notas[pos]) + cnt:
            ret = dp(pos + 1, rem - cnt * notas[pos]) + cnt           
            menor[pos][rem] = rem - cnt * notas[pos]
 
        cnt += 1
 
    memo[pos][rem] = ret
    return ret

print("Digite o valor inteiro a ser sacado: ")

N = int(input())

if dp(0, N) == INF:
    print("Não é possível realizar este saque")
    exit(0)
print(dp(0, N), "nota(s) no total")

pos = 0
rem = N
while menor[pos][rem] != -1 and pos < len(notas):
    new_rem = menor[pos][rem]
    print("{} notas de {}".format((rem - new_rem) // notas[pos], notas[pos]))

    rem = new_rem
    pos += 1