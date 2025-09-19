idade = int(input("Digite sua idade: "))

if idade <= 15:
    print("Você não pode votar!")
elif idade >= 16 and idade <= 18 or idade > 70:
    print("Você pode votar mas não é obrigado!!")
else:
    print("Você é obrigado à votar!")