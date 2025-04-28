# Dia 3 - Curso em Vídeo Python - Exercícios 5 a 15

# Exercício 5
n1 = int(input('Digite um número: '))
print('O sucessor é {} e o antecessor é {}'.format(n1+1, n1-1))

# Exercício 6
n1 = int(input('Digite um número: '))
print('O dobro é {}, o triplo é {} e a raiz quadrada é {:.3f}'.format(n1*2, n1*3, n1**(1/2)))

# Exercício 7
n1 = float(input('Digite sua nota de Matemática: '))
n2 = float(input('Digite sua nota de Português: '))
print('A média é {:.1f}'.format((n1+n2)/2))

# Exercício 8
n1 = float(input('Digite um valor em metros: '))
print('São {:.0f} cm e {:.0f} mm'.format(n1*100, n1*1000))

# Exercício 9
n1 = int(input('Digite um número: '))
print('Tabuada de {}'.format(n1))
print('{} x 1 = {}'.format(n1, n1*1))
print('{} x 2 = {}'.format(n1, n1*2))
print('{} x 3 = {}'.format(n1, n1*3))
print('{} x 4 = {}'.format(n1, n1*4))
print('{} x 5 = {}'.format(n1, n1*5))
print('{} x 6 = {}'.format(n1, n1*6))
print('{} x 7 = {}'.format(n1, n1*7))
print('{} x 8 = {}'.format(n1, n1*8))
print('{} x 9 = {}'.format(n1, n1*9))
print('{} x 10 = {}'.format(n1, n1*10))

# Exercício 10
n1 = float(input('Quantos reais você tem na carteira? '))
print('Com R${} você pode comprar US${:.2f} na cotação atual.'.format(n1, n1/5.69))

# Exercício 11
n1 = float(input('Qual a largura da parede? '))
n2 = float(input('Qual é a altura? '))
s = n1 * n2
print('A área é de {:.2f}m² e você vai precisar de {:.2f} litros de tinta.'.format(s, s/2))

# Exercício 12
n1 = float(input('Digite o preço do produto: '))
desconto = n1 * 5 / 100
print('O produto com 5% de desconto fica R${:.2f}'.format(n1 - desconto))

# Exercício 13
n1 = float(input('Digite seu salário: '))
aumento = n1 * 15 / 100
print('O seu salário com aumento de 15% fica R${:.2f}'.format(n1 + aumento))

# Exercício 14
n1 = float(input('Qual a temperatura em °C? '))
c1 = (n1 * 9/5) + 32
print('A temperatura em Fahrenheit é {:.2f}°F'.format(c1))

# Exercício 15
n1 = int(input('Quantos dias o carro foi alugado? '))
n2 = float(input('Quantos km ele rodou? '))
r1 = n1 * 60
r2 = n2 * 0.15
r3 = r1 + r2
print('O total a pagar é R${:.2f}'.format(r3))
