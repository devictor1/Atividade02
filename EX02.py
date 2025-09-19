produto = "Camiseta"
precoOriginal = float(50.00)
desconto = float(0.20) # (20% de desconto)
precoComDesconto = precoOriginal * (1 - desconto)

print("O produto sem desconto é de R$", precoOriginal, ", com o desconto aplicado sai no valor de R$", precoComDesconto)