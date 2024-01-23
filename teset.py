# Valor original
valor_original = "R$ 1,200.50"

# Realiza a substituição
valor_convertido = valor_original.replace(",", "t").replace(".", ",").replace("t", ".")

# Exibe o valor convertido
print(valor_convertido)