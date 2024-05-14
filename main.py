import random

modoJogo = input("digite 2 para jogar e 1 para o computador jogar: ")
if modoJogo == "1":
   numeroMaximo = int(input("quantos numeros possiveis: "))
   x = list(range(numeroMaximo))
   y = random.choice(x)
   c = numeroMaximo / 2
   m = numeroMaximo / 4
   valor = int(c)
   if valor > y:
      print("alto demais")
      print(valor)
      c -= m
      valor = int(c)
      m = m / 2
   if valor < y:
      print("baixo demais")
      print(valor)
      c += m
      valor = int(c)
      m = m / 2
   while valor != y:
      if valor > y:
         print("alto demais")
         print(valor)
         c -= m
         valor = int(c)
         m = m / 2
      if valor < y:
         print("baixo demais")
         print(valor)
         c += m
         valor = int(c)
         m = m / 2
   if valor == y:
      print("você ganhou")
      print(valor)
if modoJogo == "2":
   numeroMaximo = int(input("quantos numeros possiveis: "))
   x = list(range(numeroMaximo))
   y = random.choice(x)
   z = int(input("advinhe o numero: "))
   if z == y:
      print("você ganhou")
   if z > y:
      print("alto demais")
   if z < y:
      print("baixo demais")
   while z != y:
      z = int(input("advinhe o numero: "))
      if z == y:
         print("você ganhou")
      if z > y:
         print("alto demais")
      if z < y:
         print("baixo demais")
