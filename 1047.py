a, b, c, d = map(int, input().split())
H1 = a*60
H2 = c*60
Ti = H1 + b
Tf = H2 + d
if Tf <= Ti:
    midn = (1440 - Ti)
    totalmin = midn + Tf
    horas = (totalmin // 60)
    min = (totalmin % 60)
    print(f"O JOGO DUROU {horas} HORA(S) E {min} MINUTO(S)")

elif Tf > Ti: 
    totalmin = Tf - Ti
    horas = (totalmin // 60)
    min = (totalmin % 60)
    print(f"O JOGO DUROU {horas} HORA(S) E {min} MINUTO(S)")

