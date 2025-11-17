import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export const pokemonAPI = {
  getAllPokemons: () => api.get('/pokemons'),
  getPokemonById: (id) => api.get(`/pokemons/${id}`),
  createPokemon: (data) => api.post('/pokemons', data),
  updatePokemon: (id, data) => api.put(`/pokemons/${id}`, data),
  deletePokemon: (id) => api.delete(`/pokemons/${id}`),
};

export const tipoAPI = {
  getAllTipos: () => api.get('/tipos'),
  getTipoById: (id) => api.get(`/tipos/${id}`),
};

export const habilidadeAPI = {
  getAllHabilidades: () => api.get('/habilidades'),
  getHabilidadeById: (id) => api.get(`/habilidades/${id}`),
};

export const evolucaoAPI = {
  getAllEvolucoes: () => api.get('/evolucoes'),
};

export default api;