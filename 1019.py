 #n = segundos
N = int(input())
Hr = int(N // 3600)
Min = int(N%3600)//60
Seg = int(N % 60)

print(f"{Hr}:{Min}:{Seg}")