N = float(input())

resto = int(round(N * 100))

print(f"NOTAS:")
N100 = resto // 10000
resto = resto % 10000
print(f"{int(N100)} nota(s) de R$ 100.00")

N50 = resto // 5000 
resto = resto % 5000
print(f"{int(N50)} nota(s) de R$ 50.00")

N20 = resto // 2000 
resto = resto % 2000
print(f"{int(N20)} nota(s) de R$ 20.00")

N10 = resto // 1000
resto = resto % 1000
print(f"{int(N10)} nota(s) de R$ 10.00")

N05 = resto // 500
resto = resto % 500
print(f"{int(N05)} nota(s) de R$ 5.00")

N02 = resto // 200
resto = resto % 200
print(f"{int(N02)} nota(s) de R$ 2.00")

#MOEDAS
print(f"MOEDAS:")

N01 = resto // 100
resto = resto % 100
print(f"{int(N01)} moeda(s) de R$ 1.00")

N005 = resto // 50
resto = resto % 50
print(f"{int(N005)} moeda(s) de R$ 0.50")

N0025 = resto // 25
resto = resto % 25
print(f"{int(N0025)} moeda(s) de R$ 0.25")

N0010 = resto // 10
resto = resto % 10
print(f"{int(N0010)} moeda(s) de R$ 0.10")

N0005 = resto // 5
resto = resto % 5
print(f"{int(N0005)} moeda(s) de R$ 0.05")

N0001 = resto // 1
resto = resto % 1
print(f"{int(N0001)} moeda(s) de R$ 0.01")