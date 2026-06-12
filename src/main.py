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
from datetime import date

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