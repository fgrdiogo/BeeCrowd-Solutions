peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = float(peso/(altura **2))
imcR = round(imc, 2)

if imc < 18.5:
  print("Seu IMC é: " + str(imcR) + " Baixo Peso")
elif 18.5 <= imc <= 24.99:
  print("Seu IMC é: " + str(imcR) + " Normal")
elif 25 <= imc <= 29.99:
  print("Seu IMC é: " + str(imcR) + " Sobrepeso")
elif 30 <= imc: 
  print("Seu IMC é: " + str(imcR) + " obesidade") 