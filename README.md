# POKEMON-API

# Integrantes
Giovana Lopes Ribeiro<br>
Isabel Yumi Susa<br>
Milene Oliveira de Souza<br>
Murilo Leone Fernandes<br>

## Sobre a API 
A **POKEMON-API** foi desenvolvida para ser o um **guia de fácil acesso** ao universo Pokémon. 
Para cada Pokémon, a API retorna dados detalhados, incluindo:

* **Identificação:** Nome, Altura e Peso.
* **Tipagem (Vantagem e Fraqueza):** Informações sobre seu Tipo, e, sua vantagem e fraqueza de batalha.
* **Habilidades:** Nome e Descrição da Habilidade principal.
* **Linha Evolutiva:** Detalhes sobre a evolução, como **condição para evoluir** e a **habilidade da próxima forma**.
  
### Para Quem é Destinada?

* **Fãs e entusiastas:** Obtenha informações e curiosidades sobre seus Pokémons favoritos.
* **Desenvolvedores:** Utilize dados estruturados e de fácil integração para criar seus próprios aplicativos, guias, ou jogos temáticos.

## Tecnologias Utilizadas
* Python 3.11
* Flask
* flasgger
* SQLAlchemy
* Docker & Docker Compose
  
## Como Utilizar a API?

### pré requisitos
* [Docker](https://www.docker.com/) instalado
* Python 3.x
* pip (gerenciador de pacotes do Python)

### Passo a Passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/gilopesr/GRUPO-10--POKEMON-API.git

2. Inicie os containers:
   ```bash
   docker-compose up --build

### Acesse a documentação:
    * A API estará disponível em `http://localhost:5000/apidocs/swagger.json` .

## Diagrama ER
<img width="1066" height="641" alt="image" src="https://github.com/user-attachments/assets/bb5f3706-0d72-4668-af82-b6068b1f050a" />

# 🧩 Modelo Relacional – Banco de Dados Pokémon

Este documento descreve o modelo relacional utilizado no banco de dados de Pokémon, incluindo as entidades, relacionamentos e **razões de cardinalidade** entre elas.

## 📘 Entidades Principais

- **pokemon**  
  Representa cada Pokémon com seus atributos básicos (nome, altura, peso, tipo).

- **tipo**  
  Define o tipo elemental do Pokémon (ex: Fogo, Água, Planta), além de suas vantagens e fraquezas.

- **habilidade**  
  Representa habilidades especiais que um Pokémon pode possuir.

- **pokemon_habilidade**  
  Tabela de ligação entre Pokémon e Habilidades (relação muitos-para-muitos).

- **evolucao**  
  Armazena as informações sobre as evoluções de Pokémon, indicando de qual Pokémon evolui para qual, e sob qual condição.

---

## 🔗 Relacionamentos e Cardinalidades

| Entidades Envolvidas | Descrição da Relação | Cardinalidade |
|-----------------------|----------------------|----------------|
| **tipo** → **pokemon** | Um tipo pode estar associado a vários Pokémon, mas cada Pokémon pertence a apenas um tipo. | 1 → N |
| **pokemon** ↔ **habilidade** (via **pokemon_habilidade**) | Um Pokémon pode ter várias habilidades, e uma habilidade pode ser compartilhada por vários Pokémon. | N ↔ N |
| **pokemon** → **evolucao** | Um Pokémon pode evoluir para outro (ou mais de um) Pokémon. Cada registro de evolução indica um Pokémon que evolui para outro. | 1 → N (auto-relacionamento) |

---

## 🧠 Resumo da Cardinalidade

- **tipo** tem **vários** Pokémon → (1:N)  
- **pokemon** possui **várias** habilidades (e vice-versa) → (N:N)  
- **pokemon** pode **evoluir** para outros Pokémon → (1:N)

---

## 🛠️ Ferramenta Utilizada
Diagrama criado com **dbdiagram.io**
