# src/

Esta pasta contém o código fonte Python do projeto.

## Estrutura

```
src/
│
├── main.py        ← Aplicação completa (classes, funções e menu)
└── dados.json     ← Dados guardados (criado automaticamente ao executar)
```

## Organização do `main.py`

O ficheiro está dividido em quatro partes:

### 1. Classes
Definem os "moldes" dos dados do sistema:

- `Cliente` — nome e contacto
- `Servico` — nome e preço base
- `Encomenda` — descrição da peça, cliente, serviço, prazo, preço e estado

```python
class Cliente:
    def __init__(self, nome, contacto):
        self.nome = nome
        self.contacto = contacto
```

### 2. Persistência (JSON)
Funções responsáveis por guardar e ler os dados no ficheiro `dados.json`.
Os objetos são convertidos em dicionários para serem gravados, e
reconstruídos em objetos quando o programa volta a abrir.

- `guardar_dados(clientes, servicos, encomendas)` — escreve no ficheiro
- `ler_dados()` — lê o ficheiro (ou devolve listas vazias na primeira execução)

### 3. Funções de operação
Uma função para cada funcionalidade da aplicação (requisitos RF01 a RF10):

| Função                  | Funcionalidade                          |
|-------------------------|-----------------------------------------|
| `registar_cliente()`    | Registar um novo cliente                |
| `listar_clientes()`     | Listar os clientes                      |
| `listar_servicos()`     | Consultar os serviços disponíveis       |
| `criar_encomenda()`     | Criar uma nova encomenda                |
| `atualizar_estado()`    | Mudar o estado de uma encomenda         |
| `listar_encomendas()`   | Listar todas as encomendas              |
| `filtrar_encomendas()`  | Filtrar por estado ou por cliente       |
| `encomendas_em_atraso()`| Mostrar encomendas com prazo ultrapassado |
| `relatorio_faturacao()` | Calcular a faturação total              |
| `relatorio_por_estado()`| Contar encomendas por estado            |

### 4. Menu principal
Um ciclo `while True` que mostra o menu, lê a opção escolhida pelo
utilizador e chama a função correspondente. É também aqui que a aplicação
carrega os dados guardados ao arrancar e cria os serviços iniciais na
primeira execução.

## Como executar

```bash
cd src
python main.py
```

> Em alguns sistemas, usar `python3 main.py`.

O ficheiro `dados.json` é criado automaticamente na mesma pasta na primeira
vez que a aplicação corre.