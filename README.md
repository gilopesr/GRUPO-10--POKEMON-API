# 🧩 POKEMON-API

## 👥 Integrantes
- Giovana Lopes Ribeiro  
- Isabel Yumi Susa  
- Milene Oliveira de Souza  
- Murilo Leone Fernandes  

---

## 🌍 Sobre a API

A **POKEMON-API** foi desenvolvida como um **guia interativo e completo** do universo Pokémon.  
Cada Pokémon possui dados detalhados fornecidos pela API, incluindo:

- **Identificação:** Nome, Altura e Peso  
- **Tipagem (Vantagem e Fraqueza):** Tipo, vantagens e fraquezas em batalha  
- **Habilidades:** Nome e descrição da habilidade principal  
- **Linha Evolutiva:** Condição e detalhes da evolução, incluindo a habilidade da próxima forma  

---

## 👥 Para Quem é Destinada?

- **Fãs e entusiastas:** Explore curiosidades e informações completas sobre Pokémons.  
- **Desenvolvedores:** Utilize dados estruturados e de fácil integração em aplicativos, guias e jogos.

---

## 🚀 Novas Implementações

### 🔄 Problemas Resolvidos

**❌ ANTES:**
- Frontend estático com dados mockados  
- Backend isolado, sem integração  
- CORS não configurado  

**✅ DEPOIS:**
- Frontend dinâmico consumindo a **API real**  
- Integração total **frontend ↔ backend**  
- **Docker Compose** com todos os serviços  
- **Hot reload** ativo em desenvolvimento  
- **CORS** configurado corretamente  

---

### 🛠 Arquivos Criados/Modificados

**Backend**
- `config.py` → ✅ Corrigido com configuração de CORS  
- `app.py` → ✅ Atualizado para ambiente Docker  
- `requirements.txt` → ✅ Incluído `flask-cors`  
- `Dockerfile` → ✅ Adicionado suporte a hot reload  
- `docker-compose.yml` → ✅ Criado com todos os serviços  

**Frontend**
- `src/services/api.js` → ✅ Novo cliente HTTP com Axios  
- `src/App.jsx` → ✅ Reescrito com integração real com a API  
- `src/App.css` → ✅ Estilos atualizados e responsivos  
- `package.json` → ✅ Adicionado Axios  

---

## 🌐 URLs Disponíveis

| Serviço | URL | Descrição |
|----------|-----|------------|
| 🧠 Backend Flask | [http://localhost:5000](http://localhost:5000) | API principal |
| 📘 Swagger Docs | [http://localhost:5000/apidocs](http://localhost:5000/apidocs) | Documentação interativa |
| 💚 Health Check | [http://localhost:5000/health](http://localhost:5000/health) | Verifica status da API |
| ⚡ Endpoint Principal | [http://localhost:5000/api/pokemons](http://localhost:5000/api/pokemons) | Lista de Pokémons |
| 🎨 Frontend React | [http://localhost:5173](http://localhost:5173) | Interface Web |

---

## 🧠 Resultado Final

✅ API Pokémon **100% funcional**  
✅ Frontend **integrado e responsivo**  
✅ Ambiente **Dockerizado** e padronizado  
✅ Projeto **pronto para produção**

---

## 🛠 Tecnologias Utilizadas

### Backend
- Python 3.10+  
- Flask  
- Flask-SQLAlchemy  
- Flask-CORS  
- Flasgger (Swagger)  
- SQLite  

### Frontend
- React 19  
- Vite  
- Axios  
- CSS3  

### Infraestrutura
- Docker  
- Docker Compose  

---

## 📋 Pré-requisitos

- **Docker** instalado  
- **Docker Compose** (incluso no Docker Desktop)  
- **Git**  

---

## 🎯 Como Utilizar a API

### 🔹 Opção 1: Docker Compose (Recomendado)

```bash
# Clonar o repositório
git clone https://github.com/gilopesr/GRUPO-10--POKEMON-API.git
cd GRUPO-10--POKEMON-API

# Executar todos os serviços
docker-compose up --build
```

**Acesse:**
- Frontend: [http://localhost:5173](http://localhost:5173)  
- Backend: [http://localhost:5000](http://localhost:5000)  
- Swagger: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)  
- Health Check: [http://localhost:5000/health](http://localhost:5000/health)

---

### 🔹 Opção 2: Execução Manual

**Backend**
```bash
cd GRUPO-10--POKEMON-API
pip install -r requirements.txt
python app.py
```

**Frontend**
```bash
cd poke-frontend
npm install
npm run dev
```

---

## 📚 Endpoints da API

### Pokémons
- `GET /api/pokemons` – Lista todos os Pokémons  
- `GET /api/pokemons/{id}` – Busca por ID  
- `POST /api/pokemons` – Cria novo Pokémon  
- `PUT /api/pokemons/{id}` – Atualiza Pokémon  
- `DELETE /api/pokemons/{id}` – Remove Pokémon  

### Tipos
- `GET /api/tipos` – Lista todos os tipos  
- `GET /api/tipos/{id}` – Busca tipo por ID  

### Habilidades
- `GET /api/habilidades` – Lista todas as habilidades  
- `GET /api/habilidades/{id}` – Busca habilidade por ID  

### Evoluções
- `GET /api/evolucoes` – Lista todas as evoluções  

---

## 🗃️ Estrutura do Projeto

```
GRUPO-10--POKEMON-API/
├── poke-frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── services/api.js
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── controller/
│   ├── pokemon_controller.py
│   ├── tipo_controller.py
│   ├── habilidade_controller.py
│   └── evolucao_controller.py
├── instance/
│   └── pokemon.db
├── app.py
├── config.py
├── pokemon.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🔧 Comandos Úteis

**Desenvolvimento**
```bash
docker-compose restart api
docker-compose restart frontend
docker-compose logs -f
docker-compose down
```

**Banco de Dados**
```bash
sqlite3 instance/pokemon.db
.tables
SELECT * FROM pokemon;
```

---

## 🧠 Solução de Problemas

**Erro de CORS**
- Verifique se o `Flask-CORS` está ativo  
- Confirme as URLs no `src/services/api.js`  

**Frontend não carrega dados**
- Verifique se o backend está rodando na porta 5000  
- Use `docker-compose logs api` para depurar  

**Dependências ausentes**
```bash
cd poke-frontend && npm install
pip install -r requirements.txt
```

---

## 📊 Diagrama ER

![Modelo Relacional Pokémon](https://github.com/user-attachments/assets/bb5f3706-0d72-4668-af82-b6068b1f050a)

---

## 🧩 Modelo Relacional – Banco de Dados Pokémon

### 📘 Entidades Principais
- **pokemon**
- **tipo**
- **habilidade**
- **pokemon_habilidade**
- **evolucao**

### 🔗 Relacionamentos
| Entidade | Descrição | Cardinalidade |
|-----------|------------|----------------|
| tipo → pokemon | Um tipo pode estar associado a vários Pokémon | 1:N |
| pokemon ↔ habilidade | Relação muitos-para-muitos | N:N |
| pokemon → evolucao | Um Pokémon pode evoluir em outro | 1:N |

---

## 🛠️ Ferramenta Utilizada

Diagrama criado com **dbdiagram.io**

---

## 📄 Licença

Projeto desenvolvido para **fins educacionais**.

---

## 🤝 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir **issues** e **pull requests**.

> Desenvolvido com ❤️ pelo **Grupo 10**
