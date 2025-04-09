import os
import time
import json

tarefas= []
add_outra_tarefa=""

def exiber_mensagem_boas_vindas(): 
    print("Bem vindo (a) ao seu gerenciador de tarefas!\n")

def opcoes():
    print("1- Adicionar tarefa")
    print("2- Listar tarefas")
    print("3- Remover tarefa")
    print("4- Sair do gerenciador de tarefas")

def voltar_menu_opcao_escolhida():
    voltar= input("Aperte ENTER para voltar às escolhas!")
    os.system("cls" if os.name =="nt" else "clear")
    main()

#Código genérico do adicionar_tarefas
def codigos_adicionar_tarefas():
        adicionar= input("\nInsira uma tarefa: ")
        tarefas.append(adicionar)
        salvar_tarefas(tarefas)
        print("\nTarefa adicionada!")
    
def adicionar_tarefas():
    os.system("cls" if os.name =="nt" else "clear")
    print("Adicione uma tarefa à sua lista!")
    codigos_adicionar_tarefas()
    add_outra_tarefa=int(input("\nDeseja adicionar outra tarefa? Digite 1 para sim e 2 para não: "))
    
    while(add_outra_tarefa == 1):
            codigos_adicionar_tarefas()  
            add_outra_tarefa=int(input("\nDeseja adicionar outra tarefa? Digite 1 para sim e 2 para não: "))

    if(add_outra_tarefa != 1 and add_outra_tarefa !=2):
        print("Opção inválida, insira uma opção válida!\n")
        time.sleep(4)
        adicionar_tarefas()
        
    voltar_menu_opcao_escolhida()

#Código genérico da lista de tarefas
def lista_de_tarefas_exibir_simplificada():
    print("Listando suas tarefas!")
    i=0
    for elemento in tarefas:
        print(f"{i}-{elemento}")
        i= i+1

def exibir_lista_tarefas():
    os.system("cls" if os.name =="nt" else "clear")
    lista_de_tarefas_exibir_simplificada()
    voltar_menu_opcao_escolhida()

def remover_tarefa():
    lista_de_tarefas_exibir_simplificada()

    insercao_da_tarefa_a_remover=input("Insira o respectivo número da tarefa que deseja remover: ")
    insercao_da_tarefa_a_remover= int(insercao_da_tarefa_a_remover)
    tarefa_removida=tarefas.pop(insercao_da_tarefa_a_remover)
    salvar_tarefas(tarefas)
    print(f"""A tarefa: "{tarefa_removida}" foi removida com sucesso!""")

    voltar_menu_opcao_escolhida()

def opcao_invalida():
    print("Opção inválida, insira uma opção válida!\n")
    opcoes()
    opcao_escolhida()

def opcao_escolhida():
    escolha_da_opcao= input("Insira a opção desejada: ")
    escolha_da_opcao= int(escolha_da_opcao)
    os.system("cls" if os.name =="nt" else "clear")

    try:
        if escolha_da_opcao == 1:
            adicionar_tarefas()
        elif escolha_da_opcao == 2:
            exibir_lista_tarefas()
        elif escolha_da_opcao == 3:
            remover_tarefa()
        elif escolha_da_opcao == 4:
            print("Saindo do seu gerenciador de tarefas!")
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#Cria uma função que recebe uma lista tarefas e salva no arquivo tarefas.json (ou outro, se quiser)
def salvar_tarefas(tarefas, nome_arquivo= "tarefas.json"):
    #Abre o arquivo para escrita("w"), e o encoding="utf-8" é tipo uma super tabela que suporta todas as línguas e suas particularidades
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        #“Salva minha lista tarefas dentro do arquivo arquivo, com visual bonito (indentado) e mantendo os acentos.”
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

#Carrega as tarefas do sistema 
def carregar_tarefas(nome_arquivo="tarefas.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

tarefas= carregar_tarefas()

#Função principal do projeto
def main():
    global tarefas
    exiber_mensagem_boas_vindas()
    opcoes()
    opcao_escolhida()