**Sistema de Gestão de Encomendas de Restauro**

Aplicação de consola que ajuda um pequeno negócio de restauro e pintura de mobiliário (Rose Maria Restauros) a gerir clientes, serviços e encomendas acompanhando o estado de cada peça, os prazos de entrega e a faturação.

---

## Informação do Projeto

| Campo            | Detalhe                              |
|------------------|--------------------------------------|
| **Curso**        | UFCD 10790 – Projeto de Programação  |
| **Formando**     | Yasmin Mota Dreer de Resende         |
| **Formador**     | Carlos Barata                        |
| **Instituição**  | IEFP                                 |
| **Data de início** | [dd/mm/aaaa]                       |
| **Data de entrega** | 19/06/2026                        |
| **Versão**       | 1.0                                  |

---

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Requisitos Técnicos](#requisitos-técnicos)
- [Como Instalar e Executar](#como-instalar-e-executar)
- [Persistência de Dados](#persistênciadedados)
- [Estrutura do Código](#estruturadocódigo)
- [Documentação](#documentação)
- [Estado do Projeto](#estado-do-projeto)

---

## Descrição

O Sistema de Gestão de Encomendas de Restauro é uma aplicação de consola desenvolvida em Python para apoiar a gestão diária de um pequeno negócio de restauro e pintura de mobiliário.


Problema que resolve: ateliês de pequena dimensão organizam as encomendas de forma manual (cadernos, folhas soltas, memória), o que leva a perda de informação, prazos esquecidos e ausência de uma visão clara da faturação. Esta aplicação centraliza tudo num único sítio.
Utilizadores: o gestor do ateliê (utilizador único). A aplicação é uma ferramenta interna de gestão — os clientes não acedem ao sistema.
Abordagem técnica: aplicação de consola em Python, com persistência dos dados num ficheiro JSON local. Não utiliza base de dados nem interface gráfica, mantendo-se simples, portátil e fácil de executar.

---

## Funcionalidades

 [X]RF01 — Registar clientes (nome e contacto)
 [X]RF02 — Listar clientes registados
 [X]RF03 — Consultar serviços disponíveis e respetivos preços base
 [X]RF04 — Criar encomendas (cliente, serviço, descrição da peça, prazo e preço)
 [X]RF05 — Atualizar o estado de uma encomenda (Recebida → Em progresso → Concluída → Entregue)
 [X]RF06 — Listar todas as encomendas
 [X]RF07 — Filtrar encomendas por estado e por cliente
 [X]RF08 — Identificar encomendas em atraso
 [X]RF09 — Relatório de faturação total
 [X]RF10 — Relatório de encomendas por estado
 [X]RF11 — Persistência dos dados em ficheiro JSON

---

## Estrutura do Repositório

```
projeto-ufcd-10790/
│
├── README.md               ← Este ficheiro — apresentação do projeto
├── .gitignore              ← Ficheiros a ignorar pelo Git
│
├── src/                    ← Código fonte Python
│   ├── main.py             ← Aplicação completa (classes, funções e menu)
│   └── dados.json          ← Dados guardados (criado automaticamente ao executar)
│
├── docs/                   ← Documentação do projeto
│   ├── ambito.docx         ← Documento de âmbito do projeto
│   ├── requisitos.xlsx     ← Levantamento de requisitos (RF e RNF)
│   ├── cronograma.md       ← Cronograma das atividades (Gantt)
│   ├── relatorio.docx      ← Relatório final do projeto
│   ├── manual_utilizador.docx  ← Manual de utilização da aplicação
│   └── manual_tecnico.docx     ← Manual de instalação e execução
│
├── assets/                 ← Recursos visuais e apresentação
│   └── apresentacao.pptx   ← Apresentação final
│
└── tests/                  ← Testes (opcional)
```

---

## Requisitos Técnicos

Python 3.10 ou superior
Bibliotecas: apenas a biblioteca padrão do Python — não é necessário instalar nada externo:

json — leitura e escrita dos dados (incluído no Python)
datetime — cálculo das encomendas em atraso (incluído no Python)

Como o projeto só usa módulos incluídos no Python, não existe ficheiro requirements.txt nem dependências a instalar.
```

---

## Como Instalar e Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/YasminDreer/projeto-ufcd-10790.git
cd projeto-ufcd-10790
```

### 2. (Opcional) Criar ambiente virtual

```bash
cd src
python main.py
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
cd src
python main.py
```
Na primeira execução, a aplicação cria automaticamente o ficheiro dados.json e os serviços iniciais. Não é preciso configurar mais nada.
---

**##Persistência de Dados**

A aplicação não usa base de dados. Toda a informação (clientes, serviços e encomendas) é guardada num ficheiro de texto no formato JSON:

Ficheiro: src/dados.json
Criação: automática, na primeira vez que a aplicação corre
Atualização: o ficheiro é regravado sempre que se regista, cria ou altera algum dado, garantindo que nada se perde entre utilizações


Esta abordagem mantém o projeto simples e portátil — basta o ficheiro main.py e o dados.json para a aplicação funcionar em qualquer computador com Python.
```

---

**##Estrutura do Código**

O código está todo no ficheiro src/main.py, organizado em quatro partes claras:

```
main.py
│
├── 1. CLASSES          → Cliente, Servico, Encomenda (os "moldes" dos dados)
│
├── 2. PERSISTÊNCIA     → guardar_dados() e ler_dados() (ficheiro JSON)
│
├── 3. FUNÇÕES          → uma função por operação:
│                          registar_cliente, listar_clientes, listar_servicos,
│                          criar_encomenda, atualizar_estado, listar_encomendas,
│                          filtrar_encomendas, encomendas_em_atraso,
│                          relatorio_faturacao, relatorio_por_estado
│
└── 4. MENU             → ciclo principal que mostra as opções e chama
                          a função correspondente à escolha do utilizador
```
A aplicação usa Programação Orientada a Objetos (classes para representar os dados) e tratamento de exceções (try/except) para validar as entradas do utilizador e evitar que o programa termine inesperadamente.
---

## Documentação

| Documento                  | Localização                        | Descrição                              |
|----------------------------|------------------------------------|----------------------------------------|
| Relatório do Projeto       | `docs/relatorio.docx`              | Relatório completo do projeto          |
| Levantamento de Requisitos | `docs/requisitos.xlsx`             | Requisitos funcionais e não funcionais |
| Manual do Utilizador       | `docs/manual_utilizador.docx`      | Como usar a aplicação                  |
| Manual Técnico             | `docs/manual_tecnico.docx`         | Instalação e configuração              |
| Apresentação               | `assets/apresentacao.pptx`         | Slides da apresentação final           |

---

## Estado do Projeto

```
Sessão 1 — Requisitos        ✅ Concluído
Sessão 2 — Desenho           ✅ Concluído
Sessão 3 — Desenvolvimento 1 ✅ Concluído
Sessão 4 — Desenvolvimento 2 ✅ Concluído
Sessão 5 — Apresentação      🔄 Em curso
```

---

*UFCD 10790 – Projeto de Programação | 2026*
