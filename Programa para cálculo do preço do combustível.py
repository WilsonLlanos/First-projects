"""1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool
Até 25 litros, desconto de 2% por litro
Acima de 25 litros, desconto de 4% por litro

Gasolina
Até 25 litros, desconto de 3% por litro
Acima de 25 litros, desconto de 5% por litro

Escreva um programa que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma:
A para álcool e G para gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 5,89 e o preço do litro do álcool é R$ 4,39."""



descontoA1 = 0.02
descontoA2 = 0.04
descontoG1 = 0.03
descontoG2 = 0.05

a=4.39
g=5.89

combustível = str(input("Vai abastecer com álcool ou gasolina?\n"))
print(f"você escolheu \n{combustível}")

litros = float(input("Quantos litros deseja abastecer?\n"))
print(f"Você quer abastecer {litros} litros de {combustível}")



if combustível == "alcool":
    if litros <= 25:
        print(f"Seu desconto é de 2% por litro")
        precofinal = a*litros-(a*litros*descontoA1)
        print(f"O preço cheio é de R${a*litros:.2f}, com com o desconto fica R${precofinal:.2f}")
    else:
        print("Seu desconto é 4% por litro")
        precofinal = a*litros-(a*litros*descontoA2)
        print(f"O preço cheio é de R${a * litros:.2f}, com com o desconto fica R${precofinal:.2f}")
else:
    if litros <= 25:
        print(f"Seu desconto é de 3% por litro")
        precofinal = g*litros-(g*litros*descontoG1)
        print(f"O preço cheio é de R${g*litros:.2f}, com com o desconto fica R${precofinal:.2f}")
    else:
        print("Seu desconto é 5% por litro")
        precofinal = g*litros-(g*litros*descontoG2)
        print(f"O preço cheio é de R${g * litros:.2f}, com com o desconto fica R${precofinal:.2f}")