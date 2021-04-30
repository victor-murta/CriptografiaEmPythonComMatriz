
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '!', '#']
numeros = [0, 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

palavra = str(input('Digite a palavra: ')).strip().upper()
palavra.replace(' ', '#')


if len(palavra) % 2 != 0:
    palavra += '#'

numero_palavra = [[],[]]
ct = 0
for p in range(len(palavra)):
    ct += 1
    if ct > len(palavra) // 2:
        numero_palavra[1].append(numeros[letras.index(palavra[p])])
    else:
        numero_palavra[0].append(numeros[letras.index(palavra[p])])


matriz_multiplicar = [
    [3, 1],
    [2, 1]
]
matriz_final = [[],[]]
ct1 = 0

print(numero_palavra)

for a in range(2):
    for b in range(len(palavra)):
        calc = matriz_multiplicar[a][b]
        print(calc)
        # calc = matriz_multiplicar[a][b] * numero_palavra[a][b] + matriz_multiplicar[a][b+1] * numero_palavra[a+1][b]
        
        ct += 1
        if ct1 > len(palavra) // 2:
            matriz_final[1].append(calc)
        else:
            matriz_final[0].append(calc)



print(matriz_final[0])
print(matriz_final[1])
print(palavra)


