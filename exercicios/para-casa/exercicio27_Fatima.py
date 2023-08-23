# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

peso_do_morango = float(input("quantos kg de morango"))
peso_da_maca = float(input("quantos kg de maçã"))


if peso_do_morango > 5:
    valor_do_kg_do_morango = 2.20
else: 
    valor_do_kg_do_morango = 2.50


if peso_da_maca > 5:
    valor_do_kg_da_maca = 1.50
else:
    valor_do_kg_da_maca = 1.80 


# calculo do valor total da compra

valor_total_da_compra = (peso_do_morango * valor_do_kg_do_morango) + (peso_da_maca * valor_do_kg_da_maca)

if (peso_do_morango + peso_da_maca) > 8 or valor_total_da_compra > 25:
    valor_total_da_compra = valor_total_da_compra * 0.9

print(f"o total da sua compra deu {valor_total_da_compra:,.2f}")