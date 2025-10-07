# POKEMON-API

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

