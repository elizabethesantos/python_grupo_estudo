# Definir mensalidade atual
mensalidade_atual = 650.00

# Criar lista de alunos com as informações necessárias
alunos = []

# Para cada aluno na lista de 1200 alunos
for aluno in range(1, 1201):
    # Ler número da inscrição, nome do aluno e quantidade de questões acertadas
    numero_inscricao = int(input("Digite o número da inscrição do aluno: "))
    nome_aluno = input("Digite o nome do aluno: ")
    quantidade_questoes_acertadas = int(input("Digite a quantidade de questões acertadas pelo aluno: "))
    
    # Calcular porcentagem de desconto com base na quantidade de questões acertadas
    if quantidade_questoes_acertadas >= 45:
        porcentagem_desconto = 90
    elif quantidade_questoes_acertadas >= 35:
        porcentagem_desconto = 65
    elif quantidade_questoes_acertadas >= 25:
        porcentagem_desconto = 45
    else:
        porcentagem_desconto = 20
    
    # Calcular mensalidade com desconto
    mensalidade_com_desconto = mensalidade_atual * (100 - porcentagem_desconto) / 100
    
    # Adicionar informações do aluno à lista de alunos
    aluno_info = [numero_inscricao, nome_aluno, quantidade_questoes_acertadas, porcentagem_desconto, mensalidade_com_desconto]
    alunos.append(aluno_info)
    
    # Se o aluno obteve 90% de desconto, parabenizá-lo
    if porcentagem_desconto == 90:
        print("Parabéns,", nome_aluno, "você obteve 90% de desconto na mensalidade!")

# Escrever relatório com as informações dos alunos
print("Relatório dos Alunos:")
for aluno in alunos:
    print("Número da Inscrição:", aluno[0])
    print("Nome do Aluno:", aluno[1])
    print("Quantidade de Questões:", aluno[2])
    print("Porcentagem de Desconto:", aluno[3], "%")
    print("Mensalidade com Desconto:", aluno[4])