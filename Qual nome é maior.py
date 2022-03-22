"""8-Leia dois nomes pelo teclado e imprima:
 O maior entre eles(Sem considerar espaços), se forem do mesmo tamanho imprima uma mensagem.
 Quem tem o ultimo nome menor, se forem do mesmo tamanho imprima uma mensagen.
 Nome do meio ao contrario
 """

nome1 = str(input("Insira o nome 1\n"))
nome2 = str(input("Insira o nome 2\n"))

if (len(nome1) - nome1.count(' ')) > (len(nome2) - nome2.count(' ')):
    print(f"Nome 1 ({nome1}) é maior que o nome 2 ({nome2})")
elif (len(nome1) - nome1.count(' ')) == (len(nome2) - nome2.count(' ')):
    print(f"Os nomes são do mesmo tamanho")
else:
    print(f"O nome 1 ({nome1}) é menor que o nome 2 ({nome2})")

nome1_1 = nome1.split()
nome2_2 = nome2.split()

if (len(nome1_1[len(nome1_1)-1])) < (len(nome2_2[len(nome2_2)-1])):
    print(f"O último sobrenome do nome 1 é menor que o último sobrenome do nome 2")
elif (len(nome2_2[len(nome2_2)-1])) < (len(nome1_1[len(nome1_1)-1])):
    print(f"O último sobrenome do nome 2 é menor que o último sobrenome do nome 1")
else:
    print(f"Os últimos sobrenomes são do mesmo tamanho")

print(f"nome 1 {nome1.split()[len(nome1.split())-1]} e nome 2 {nome2.split()[len(nome2.split())-1]}")