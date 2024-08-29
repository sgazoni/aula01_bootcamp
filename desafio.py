
valor_acrescimo = 1000

# 1) Solicita ao usuário que digite o seu nome.
nome = input('Digite seu nome.: ')

# 2) Solicita ao usuário que digite o seu salário.
salario = float(input('Digite o seu salário.: '))

# 3) Solicita ao usuário que digite o valor do bonus recebido.
bonus = float(input('Digite o valor do bonus.: '))

# 4) Calcule o valor do bonus final.
valor_do_bonus = valor_acrescimo + salario * bonus

# 5) Imprima uma mensagem personaliza para o usuario.
print(f' O usuário.: {nome} possui o bonus de {valor_do_bonus} ')