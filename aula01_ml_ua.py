# PROG.01
def math():

  nr1 = int(input("Digite o primeiro número: "))
  nr2 = int(input("Digite o primeiro número: "))

  soma = nr1 + nr2
  sub = nr1 - nr2
  mult = nr1 * nr2

  print("")
  print(f"A soma de {nr1} e {nr2} é...........: {soma}")
  print(f"A subtração de {nr1} e {nr2} é......: {sub}")
  print(f"A multiplicação de {nr1} e {nr2} é..: {mult}")

math()

# ********

# PROG.02
def area_circunferencia():

  pi = 3.1416

  raio = int(input("Digite o raio da circunferência: "))

  print(f"O perímetro da circunferência é: {2 * pi * raio}")

area_circunferencia()

# ********

# PROG.03
def conversao_temperatura():

  temperatura = int(input("Digite a tempertatura: "))

  print(f"A temperatura de {temperatura} graus centígrados em Fahrenheit é...: {temperatura * 1.8 + 32}")
  print(f"A temperatura de {temperatura} graus centígrados em Kelvin é.......: {temperatura + 273}")

conversao_temperatura()

# ********

# PROG.05
def imc(): 

  massa = int(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))

  print(f"Seu índice de massa corporal é de {massa / ( altura * altura )}")

imc()
