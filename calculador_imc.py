#prova
def menu_salvar_carregar():
    while True:
        print("*********************************")
        print("**** SALVAR E CARREGAR DADOS ****")
        print("*********************************")
        
        print("""MENU DE SALVAR E CARREGAR
        1 - Salvar Dados em um Arquivo
        2 - Carregar Dados de um Arquivo
        3 - Voltar ao Menu Principal""")
        
        opc = int(input("Escolha uma opção: "))
        
        if opc == 1:
            with open("avaliados.txt", "w") as file:
                for dados in avaliados:
                    file.write(f"{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
            print("Dados salvos com sucesso.")
        elif opc == 2:
            try:
                with open("avaliados.txt", "r") as file:
                    avaliados.clear()
                    for line in file:
                        id, nome, imc, classificacao = line.strip().split(",")
                        avaliados.append([int(id), nome, float(imc), classificacao])
                print("Dados carregados com sucesso.")
            except FileNotFoundError:
                print("Arquivo não encontrado.")
        elif opc == 3:
            break
        else:
            print("Escolha uma opção válida!")

def menu_estatisticas():
    while True:
        print("*********************************")
        print("********* ESTATÍSTICAS **********")
        print("*********************************")
        
        print("""MENU DE ESTATÍSTICAS E ORDENAÇÃO
        1 - Exibir a Média de IMCs
        2 - Exibir o Maior e Menor IMC
        3 - Exibir Contagem de Avaliados por IMC
        4 - Voltar ao Menu Principal""")
        
        opc = int(input("Escolha uma opção: "))
    #################################################### Media de IMC ###############################################        
        if opc == 1:
            soma=0 
            for dados in avaliados:
                soma += dados[2]
                media = soma / len (avaliados)
            print(f"A media do IMC é: {media:.2f}")
    #################################################### Media de IMC ###############################################
        elif opc == 2:
            if len(avaliados) == 0:
                print("Nenhum avaliado registrado!")
            else:
                maior_imc = max(avaliados, key=lambda x: x[2]) #armazenando o IMC maior
                menor_imc = min(avaliados, key=lambda x: x[2]) #armazenando o IMC menor
                print(f"O maior IMC é {maior_imc[2]} de {maior_imc[1]}, avaliado como: {maior_imc[3]}")
                print(f"O menor IMC é {menor_imc[2]} de {menor_imc[1]}, avaliado como: {menor_imc[3]}")
 
        elif opc == 3: # Início Tarefa (Grupo 6 - Edmo, André, Haslan)
            if len(avaliados) == 0:
                print("Nenhum avaliado registrado.")
            else:
                contagem_imc = {
                    "Magreza Grave": 0,
                    "Magreza Moderada": 0,
                    "Magreza Leve": 0,
                    "Peso Ideal": 0,
                    "Sobrepeso": 0,
                    "Obesidade Grau I": 0,
                    "Obesidade Grau II": 0,
                    "Obesidade Grau III": 0
                }
                
                for dados in avaliados:
                    classificacao = dados[3]
                    contagem_imc[classificacao] += 1
                
                for classificacao, quantidade in contagem_imc.items():
                    print(f"{classificacao}: {quantidade} avaliado(s)") # Imprissão da Quantidade de avaliados em cada Classificação
        elif opc == 4:
            break
        else:
            print("Escolha uma opção válida!") # Fim Tarefa (Grupo 6 - Edmo, André, Haslan)

def classifica_imc(imc):
    if imc < 16:
        return "Magreza Grave"
    elif imc <= 16.9:
        return "Magreza Moderada"
    elif imc <= 18.5:
        return "Magreza Leve"
    elif imc <= 24.9:
        return "Peso Ideal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 34.9:
        return "Obesidade Grau I"
    elif imc <= 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

avaliados = []
id = 0

while True:
    print("*********************************")
    print("*******CALCULADORA DE IMC********")
    print("*********************************")
    
    print("""MENU
          1 - Calcular IMC
          2 - Exibir Resultados
          3 - Atualizar Dados de um Avaliado
          4 - Remover um Avaliado
          5 - Estatísticas
          6 - Salvar e Carregar Dados
          7 - Sair""")
    
    opc = int(input("Escolha uma opção: "))
    
    if opc == 1:
        nome = input("Digite o nome do avaliado: ")
        peso = float(input("Digite o peso do avaliado: "))
        altura = float(input("Digite a altura do avaliado: "))
        imc = round(peso / altura ** 2, 2)
        classificacao = classifica_imc(imc)
        print(f"O IMC de {nome} é {imc} e está classificado como: {classificacao}")
        
        id += 1
        dados = [id, nome, imc, classificacao]
        avaliados.append(dados)
    
    elif opc == 2:
        if len(avaliados) == 0:
            print("Nenhum avaliado registrado.")
        else:
            print("*********************************")
            print("*******EXIBIÇÃO DE RESULTADOS*****")
            print("*********************************")
            print("""SUBMENU DE EXIBIÇÃO DE RESULTADOS:
                  1 - Imprimir Todos os Resultados
                  2 - Imprimir por ID
                  3 - Imprimir Avaliados Ordenados por Nome
                  4 - Imprimir Avaliados Ordenados por IMC
                  5 - Voltar ao Menu Principal""")
            sub_opc = int(input("Escolha uma opção: "))
            
            if sub_opc == 1:
                for dados in avaliados:
                    print(f"ID:{dados[0]} O IMC de {dados[1]} é {dados[2]} e está classificado como: {dados[3]}")
            
            elif sub_opc == 2:
                pass  # Criar Tarefa (1)
            
            elif sub_opc == 3:
                nomes_ordenados = (sorted(avaliados, key=lambda x: x[1]))
                print("Lista dos avaliados, por ordem alfabética:")
                for dados in nomes_ordenados:
                    print(f"ID:{dados[0]} O IMC de {dados[1]} é {dados[2]} e está classificado como: {dados[3]}")
                        
            elif sub_opc == 4:
                imc_ordenado = (sorted(avaliados, key=lambda x: x[2]))
                for dados in imc_ordenado:
                    print(f"ID:{dados[0]} O IMC de {dados[1]} é {dados[2]} e está classificado como: {dados[3]}")

            elif sub_opc == 5:
                continue
    
    elif opc == 3:
        id_procurada = int(input("Digite a Id do avaliado para atualizar: "))
        encontrado = False
        for dados in avaliados:
            if dados[0] == id_procurada:
                nome = input("Digite o novo nome do avaliado: ")
                peso = float(input("Digite o novo peso do avaliado: "))
                altura = float(input("Digite a nova altura do avaliado: "))
                imc = round(peso / altura ** 2, 2)
                classificacao = classifica_imc(imc)
                dados[1] = nome
                dados[2] = imc
                dados[3] = classificacao
                print("Dados atualizados com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Id não encontrada.")
    
    elif opc == 4:
        id_procurada = int(input("Digite a Id do avaliado para remover: "))
        encontrado = False
        for dados in avaliados:
            if dados[0] == id_procurada:
                avaliados.remove(dados)
                print("Avaliado removido com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Id não encontrada.")
    
    elif opc == 5:
        if len(avaliados) == 0:
            print("Nenhum avaliado registrado.")
        else:
            menu_estatisticas()
    
    elif opc == 6:
        menu_salvar_carregar()
    
    elif opc == 7:
        break
    
    else:
        print("Escolha uma opção válida!")