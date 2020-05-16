print('=' * 5, 'AULA_009a', '=' * 5)
frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase.split())
dividido = frase.split()
print(dividido[3])
print(dividido[2][0])

print("""Este é um exemplo de texto longo,
 onde há excedente de linhas. Bem mais 
 prático do que fazer PRINT a cada nova linha.""")
