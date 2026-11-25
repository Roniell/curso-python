# if / elif / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print('Aqui você esta')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar ou sair.')

print('FORA DOS BLOCOS')