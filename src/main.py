# ============================================================
#      AS CLASSES (os "moldes" dos nossos dados)
# ============================================================

class Cliente:
    def __init__(self, nome, contacto):
        self.nome = nome
        self.contacto = contacto


class Servico:
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base


class Encomenda:
    def __init__(self, descricao_peca, cliente, servico, prazo, preco, estado="Recebida"):
        self.descricao_peca = descricao_peca   # ex: "Cómoda antiga em carvalho"
        self.cliente = cliente                 # nome do cliente
        self.servico = servico                 # nome do serviço escolhido
        self.prazo = prazo                     # data limite, ex: "2026-07-15"
        self.preco = preco                     # valor a cobrar
        self.estado = estado                   # começa sempre em "Recebida"
        
# ============================================================
#       GUARDAR E LER OS DADOS (ficheiro JSON)
# ============================================================

import json
from datetime import date, datetime

NOME_FICHEIRO = "dados.json"

def guardar_dados(clientes, servicos, encomendas):
    # transformar cada objeto num dicionário simples
    lista_clientes = []
    for c in clientes:
        lista_clientes.append(vars(c))

    lista_servicos = []
    for s in servicos:
        lista_servicos.append(vars(s))

    lista_encomendas = []
    for e in encomendas:
        lista_encomendas.append(vars(e))

    # juntar tudo num só dicionário
    dados = {
        "clientes": lista_clientes,
        "servicos": lista_servicos,
        "encomendas": lista_encomendas
    }

    # escrever no ficheiro
    with open(NOME_FICHEIRO, "w", encoding="utf-8") as ficheiro:
        json.dump(dados, ficheiro, ensure_ascii=False, indent=4)


def ler_dados():
    try:
        with open(NOME_FICHEIRO, "r", encoding="utf-8") as ficheiro:
            dados = json.load(ficheiro)
    except FileNotFoundError:
        # se o ficheiro ainda não existe (1ª vez que corre), começa vazio
        return [], [], []

    # reconstruir os objetos a partir dos dicionários
    clientes = []
    for c in dados["clientes"]:
        clientes.append(Cliente(c["nome"], c["contacto"]))

    servicos = []
    for s in dados["servicos"]:
        servicos.append(Servico(s["nome"], s["preco_base"]))

    encomendas = []
    for e in dados["encomendas"]:
        encomendas.append(Encomenda(e["descricao_peca"], e["cliente"], e["servico"],
                                     e["prazo"], e["preco"], e["estado"]))

    return clientes, servicos, encomendas

# ============================================================
#        AS FUNÇÕES DE CADA OPERAÇÃO
# ============================================================
    
clientes = []
servicos = []
encomendas = []

# ---- registar um cliente ----
def registar_cliente():
    print("\n--- Registar Cliente ---")
    nome = input("Nome do cliente: ")
    if nome == "":
        print("O nome não pode ficar vazio.")
        return
    contacto = input("Contacto: ")
    novo_cliente = Cliente(nome, contacto)
    clientes.append(novo_cliente)
    guardar_dados(clientes, servicos, encomendas)
    print("Cliente registado com sucesso!")

# ---- listar clientes ----
def listar_clientes():
    print("\n--- Lista de Clientes ---")
    if len(clientes) == 0:
        print("Ainda não há clientes registados.")
        return
    for cliente in clientes:
        print("- " + cliente.nome + " | Contacto: " + cliente.contacto)
        
# ---- consultar serviços ----
def listar_servicos():
    print("\n--- Serviços Disponíveis ---")
    for servico in servicos:
        print("- " + servico.nome + " | Preço base: " + str(servico.preco_base) + " EUR")
        
# ---- criar uma encomenda ----
def criar_encomenda():
    print("\n--- Nova Encomenda ---")

    if len(clientes) == 0:
        print("Não há clientes. Regista primeiro um cliente.")
        return

    listar_clientes()
    nome_cliente = input("\nEscreve o nome do cliente desta encomenda: ")

    # verificar se o cliente existe
    cliente_existe = False
    for cliente in clientes:
        if cliente.nome == nome_cliente:
            cliente_existe = True
    if cliente_existe == False:
        print("Esse cliente não existe. Regista-o primeiro.")
        return

    listar_servicos()
    nome_servico = input("\nEscreve o nome do serviço: ")

    descricao = input("Descrição da peça: ")
    prazo = input("Prazo de entrega (DD-MM-AAAA): ")
    # validar que a data está no formato certo
    try:
        datetime.strptime(prazo, "%d-%m-%Y")
    except ValueError:
        print("Data inválida. Usa o formato DD-MM-AAAA. A encomenda não foi criada.")
        return
    
    preco_texto = input("Preço (EUR): ")
    try:
        preco = float(preco_texto)
    except ValueError:
        print("Preço inválido. A encomenda não foi criada.")
        return

    nova_encomenda = Encomenda(descricao, nome_cliente, nome_servico, prazo, preco)
    encomendas.append(nova_encomenda)
    guardar_dados(clientes, servicos, encomendas)
    print("Encomenda criada com sucesso!")


# ---- atualizar o estado de uma encomenda ----
def atualizar_estado():
    print("\n--- Atualizar Estado ---")
    if len(encomendas) == 0:
        print("Não há encomendas registadas.")
        return

    # mostrar as encomendas com um número à frente
    numero = 1
    for encomenda in encomendas:
        print(str(numero) + ") " + encomenda.descricao_peca +
              " | Cliente: " + encomenda.cliente +
              " | Estado atual: " + encomenda.estado)
        numero = numero + 1

    escolha_texto = input("\nNúmero da encomenda que queres atualizar: ")
    try:
        escolha = int(escolha_texto)
    except ValueError:
        print("Número inválido.")
        return

    if escolha < 1 or escolha > len(encomendas):
        print("Não existe encomenda com esse número.")
        return

    print("\nEstados possíveis:")
    print("1) Recebida")
    print("2) Em progresso")
    print("3) Concluída")
    print("4) Entregue")
    estado_escolhido = input("Escolhe o novo estado (1-4): ")

    if estado_escolhido == "1":
        novo_estado = "Recebida"
    elif estado_escolhido == "2":
        novo_estado = "Em progresso"
    elif estado_escolhido == "3":
        novo_estado = "Concluída"
    elif estado_escolhido == "4":
        novo_estado = "Entregue"
    else:
        print("Opção inválida.")
        return

    # a encomenda nº "escolha" está na posição (escolha - 1) da lista
    encomendas[escolha - 1].estado = novo_estado
    guardar_dados(clientes, servicos, encomendas)
    print("Estado atualizado com sucesso!")


# ---- listar todas as encomendas ----
def listar_encomendas():
    print("\n--- Todas as Encomendas ---")
    if len(encomendas) == 0:
        print("Ainda não há encomendas registadas.")
        return
    for encomenda in encomendas:
        print("- " + encomenda.descricao_peca +
              " | Cliente: " + encomenda.cliente +
              " | Serviço: " + encomenda.servico +
              " | Prazo: " + encomenda.prazo +
              " | Preço: " + str(encomenda.preco) + " EUR" +
              " | Estado: " + encomenda.estado)


# ---- filtrar encomendas ----
def filtrar_encomendas():
    print("\n--- Filtrar Encomendas ---")
    print("1) Por estado")
    print("2) Por cliente")
    opcao = input("Escolhe como queres filtrar (1-2): ")

    if opcao == "1":
        estado = input("Escreve o estado (Recebida / Em progresso / Concluída / Entregue): ")
        encontrou = False
        for encomenda in encomendas:
            if encomenda.estado == estado:
                print("- " + encomenda.descricao_peca + " | Cliente: " + encomenda.cliente)
                encontrou = True
        if encontrou == False:
            print("Nenhuma encomenda com esse estado.")

    elif opcao == "2":
        nome = input("Escreve o nome do cliente: ")
        encontrou = False
        for encomenda in encomendas:
            if encomenda.cliente == nome:
                print("- " + encomenda.descricao_peca + " | Estado: " + encomenda.estado)
                encontrou = True
        if encontrou == False:
            print("Esse cliente não tem encomendas.")
    else:
        print("Opção inválida.")


# ---- encomendas em atraso ----
def encomendas_em_atraso():
    print("\n--- Encomendas em Atraso ---")
    hoje = date.today()   # data de hoje (uma data real)

    encontrou = False
    for encomenda in encomendas:
        # transformar o texto "DD-MM-AAAA" numa data real, para poder comparar
        prazo_data = datetime.strptime(encomenda.prazo, "%d-%m-%Y").date()
        if prazo_data < hoje and encomenda.estado != "Entregue":
            print("- " + encomenda.descricao_peca +
                  " | Cliente: " + encomenda.cliente +
                  " | Prazo: " + encomenda.prazo +
                  " | Estado: " + encomenda.estado)
            encontrou = True
    if encontrou == False:
        print("Não há encomendas em atraso. Tudo em dia!")
        
def relatorio_faturacao():
    print("\n--- Relatorio de Faturacao ---")
    total = 0
    for encomenda in encomendas:
        total = total + encomenda.preco
    print("Numero de encomendas: " + str(len(encomendas)))
    print("Faturacao total: " + str(total) + " EUR")
 
 
def relatorio_por_estado():
    print("\n--- Encomendas por Estado ---")
    estados = ["Recebida", "Em progresso", "Concluida", "Entregue"]
    for estado in estados:
        contador = 0
        for encomenda in encomendas:
            if encomenda.estado == estado:
                contador = contador + 1
        print(estado + ": " + str(contador))
        
