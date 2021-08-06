def profissional(): #Dados relacionados ao emprego na iPlace
    atividade = int(input('''Qual tipo de atividade vocês gostaria de realizar?:
    [0] Organização horária
    [1] Relatório de vendas comissionadas
    :'''))
    if atividade not in(0, 1, 2):
        while atividade not in(0, 1, 2):
            atividade = int(input('''Resposta inválida. Qual tipo de atividade vocês gostaria de realizar?:
                [0] Organização horária
                [1] Relatório de vendas comissionadas
                :'''))
    elif atividade == 0:
        #Cadastro de horários
        turno = str(input('Qual seu turno atual? [M/I/N]: ')).upper().strip()
        if turno not in('M', 'I', 'N'): #M = 10:00-18:20, I = 12:00 - 20:20, N = 13:40 - 22:00
            while turno not in('M', 'I', 'N'):
                turno = str(input('Resposta Inválida. Qual seu turno atual? [M/I/N]: ')).upper().strip()
        print('Turno cadastrado com sucesso!')
    elif atividade == 1:
        #Cadastro de vendas
        produto = int(input('''Qual o tipo do produto a ser cadastrado?
        [0] Apple
        [1] Acessórios (iPlace ou Outras marcas que não Apple)
        [2] Serviço
        :'''))
#Continuar sistema de vendas comissionadas
