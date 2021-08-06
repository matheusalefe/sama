print('=-'*50)
print('Bem vindo ao S.A.M.A! Sistema de Atividades Matheus Alefe')
print('=-'*50)
escolha = int(input('''Qual tipo de atividade gostaria de registrar?
[0] Horária
[1] Profissional
[2] Estudantil
[3] Doméstica
[9] Cancelar Operação
:'''))
if escolha not in(0, 1, 2, 3, 9):
    while escolha not in(0, 1, 2, 3, 9):
        escolha = int(input('''Resposta inválida. Qual tipo de atividade gostaria de registrar?
        [0] Horária
        [1] profissional
        [2] Estudantil
        [3] Doméstica
        [9] Cancelar Operação
        :'''))
elif escolha == 9:
    print('Obrigado por usar o nosso sistema!')