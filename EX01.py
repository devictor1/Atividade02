valor = float(100.00)
taxaDolar = float(5.20)
taxaEuro = float(6.15)


def conversao():
   converter = float(input("Deseja converter de qual moeda? 1 para Dólar e 2 para Euro"))
   if converter == 1:
      print("O valor convertido é:", valor * taxaDolar)
   elif converter == 2:
      print("O valor convertido é:", valor * taxaEuro)
   else:
      print("Escolha uma opção válida!")
      conversao()
conversao()