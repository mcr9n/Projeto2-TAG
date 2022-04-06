arquivo = open('projeto2.txt', 'r')
alunos = {}
projetos = {}
lista_de_pares = []
#leitura dos projetos --> nome do projeto: [numero de vagas, requisito de nota, lista_de_alunos]
for i in range(30):
    linha = arquivo.readline()
    info_projeto = linha.split(',')
    nome_do_projeto = info_projeto[0][1:]
    numero_de_vagas = int(info_projeto[1][1:])
    requisito_de_nota = int(info_projeto[2][1])
    lista_de_alunos_com_nota = []
    projetos[nome_do_projeto] = [numero_de_vagas,requisito_de_nota, lista_de_alunos_com_nota]
#leitura dos alunos --> nome do aluno: [preferencias, nota, condição]
for i in range(100):
    linha = arquivo.readline()
    info_aluno = linha.split(')')
    nome_do_aluno = info_aluno[0][1:]
    preferencias = (info_aluno[1][2:]).split(', ')
    nota = int(info_aluno[2][2])
    pareado = 0
    verificado = 0
    alunos[nome_do_aluno] = [preferencias,nota,pareado,verificado]

#definirá um emparelhamento estável e máximo
alunos_livres = [aluno for aluno in list(alunos.keys())]  #lista de alunos livres
todos_alunos = [aluno for aluno in list(alunos.keys())]   #todos os alunos

def stableMatch():
    '''
    algoritmo de emparelhamento estável máximo, seguindo modelo visto em aula.
    '''
    while len(alunos_livres) > 0:
        for aluno in todos_alunos:
            if aluno in alunos_livres:
                begin_matching(aluno)

def begin_matching(aluno):
    '''
    A função recebe um estudante e emparelha ele com um projeto
    '''
    
    #lista_de_projetos_do_aluno = alunos[aluno][0]
    #nota_do_aluno = alunos[aluno][1]
    #projeto_que_o_aluno_ta = alunos[aluno][2]
    #lista_de_alunos_no_projeto = projetos[projeto][2]
    
    for projeto in alunos[aluno][0]:
        alunos[aluno][3] += 1
        if projetos[projeto][0]>=1:
            projeto_tem_vaga = 1
        else:
            projeto_tem_vaga = 0
            
        if projetos[projeto][1]<=alunos[aluno][1]:
            projeto_disponivel = 1
        else:
            projeto_disponivel = 0
            
        #se o projeto tem vagas e o aluno tem a nota minima:
        if projeto_disponivel and projeto_tem_vaga:
            alunos[aluno][2] = projeto
            alunos_livres.remove(aluno)
            projetos[projeto][0] -= 1
            projetos[projeto][2].append((aluno,alunos[aluno][1]))
            
            break
        #se o aluno tem a nota mínima porém o projeto não tem mais vagas, decidiremos quem fica no projeto pela melhor nota.
        elif projeto_disponivel and not projeto_tem_vaga:
            projetos[projeto][2] = sorted(projetos[projeto][2], key=lambda student: student[1])
            
            aluno_atual_com_menor_nota = projetos[projeto][2][0][1]
            aluno_potencial = alunos[aluno][1]
            '''
            Compara a nota dos alunos
            '''
            if aluno_potencial > aluno_atual_com_menor_nota:
                print(f"{aluno} é melhor que {projetos[projeto][2][0][0]}")
                print(f"desemparelha {projetos[projeto][2][0][0]} e {projeto}. Agora, {aluno} será emparelhado com {projeto}")

                #o aluno é pareado e o aluno com nota menor que ele é devolvido à lista de alunos livres
                alunos_livres.remove(aluno)
                alunos_livres.append(projetos[projeto][2][0][0])

                projetos[projeto][2][0] = (aluno, alunos[aluno][1])
                
                break
    #se todas as preferências do aluno já foram verificadas e nenhuma é possível, então ele é descartado.    
    if alunos[aluno][3] > 4:
        alunos_livres.remove(aluno)

    
stableMatch()
print("\nEmparelhamento final :    (projetos ---> lista de alunos)")
for i in projetos:
    print(f"{i} ---> {projetos[i][2]}")
                        
    
    
    
    
            