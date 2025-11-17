import React, { useState, useEffect } from 'react';
import { pokemonAPI } from './services/api';
import './App.css';

function App() {
  const [pokemons, setPokemons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedPokemon, setSelectedPokemon] = useState(null);

  useEffect(() => {
    fetchPokemons();
  }, []);

  const fetchPokemons = async () => {
    try {
      setLoading(true);
      const response = await pokemonAPI.getAllPokemons();
      setPokemons(response.data);
    } catch (err) {
      setError('Erro ao carregar pokémons da API. Verifique se o backend está rodando.');
      console.error('Error fetching pokemons:', err);
    } finally {
      setLoading(false);
    }
  };

  const fetchPokemonDetails = async (id) => {
    try {
      const response = await pokemonAPI.getPokemonById(id);
      setSelectedPokemon(response.data);
    } catch (err) {
      console.error('Error fetching pokemon details:', err);
      setError('Erro ao carregar detalhes do Pokémon');
    }
  };

  const handleRetry = () => {
    setError(null);
    setLoading(true);
    fetchPokemons();
  };

  if (loading) {
    return (
      <div className="app">
        <div className="loading">
          <h2>Carregando Pokémons...</h2>
          <p>Aguarde enquanto conectamos com a API</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <div className="error">
          <h2>Ops! Algo deu errado</h2>
          <p>{error}</p>
          <button 
            onClick={handleRetry}
            style={{
              marginTop: '15px',
              padding: '10px 20px',
              backgroundColor: '#ff0000',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer'
            }}
          >
            Tentar Novamente
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Pokédex - API Pokémon</h1>
        <p>Conectado com backend Flask</p>
      </header>

      <div className="container">
        {/* Lista de Pokémons */}
        <div className="pokemon-list">
          <h2>Lista de Pokémons ({pokemons.length})</h2>
          <div className="pokemon-grid">
            {pokemons.map(pokemon => (
              <div 
                key={pokemon.id} 
                className={`pokemon-card ${selectedPokemon?.id === pokemon.id ? 'selected' : ''}`}
                onClick={() => fetchPokemonDetails(pokemon.id)}
                style={{
                  borderColor: selectedPokemon?.id === pokemon.id ? '#ff0000' : '#dee2e6'
                }}
              >
                <h3>{pokemon.nome}</h3>
                <p><strong>Tipo:</strong> {pokemon.tipo || 'N/A'}</p>
                <p><strong>Altura:</strong> {pokemon.altura}</p>
                <p><strong>Peso:</strong> {pokemon.peso}</p>
                {pokemon.habilidades && (
                  <p>
                    <strong>Habilidades:</strong> {pokemon.habilidades.length > 0 ? pokemon.habilidades.length : 'Nenhuma'}
                  </p>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Detalhes do Pokémon */}
        {selectedPokemon ? (
          <div className="pokemon-details">
            <h2>Detalhes do Pokémon</h2>
            <div className="card">
              <div className="card-header">
                <h1>{selectedPokemon.nome}</h1>
                <div className="pokemon-stats">
                  <p><strong>Altura:</strong> {selectedPokemon.altura}</p>
                  <p><strong>Peso:</strong> {selectedPokemon.peso}</p>
                  <p><strong>Tipo:</strong> {selectedPokemon.tipo}</p>
                </div>
              </div>

              {/* Habilidades */}
              {selectedPokemon.habilidades && selectedPokemon.habilidades.length > 0 && (
                <>
                  <hr />
                  <div className="card-habilidade">
                    <h2>Habilidades</h2>
                    {selectedPokemon.habilidades.map(habilidade => (
                      <div key={habilidade.id} className="habilidade">
                        <h3>{habilidade.nome}</h3>
                        <p>{habilidade.descricao || 'Descrição não disponível'}</p>
                      </div>
                    ))}
                  </div>
                </>
              )}

              {/* Evoluções */}
              {selectedPokemon.evolucoes && selectedPokemon.evolucoes.length > 0 && (
                <>
                  <hr />
                  <div className="card-evolucao">
                    <h2>Evoluções</h2>
                    {selectedPokemon.evolucoes.map(evo => (
                      <div key={evo.id} className="evolucao">
                        <p>Evolui para: <strong>{evo.para_pokemon || 'Próxima forma'}</strong></p>
                        <p>Condição: {evo.condicao || 'Nível up'}</p>
                        {evo.habilidade && <p>Habilidade: {evo.habilidade}</p>}
                      </div>
                    ))}
                  </div>
                </>
              )}

              {/* Mensagem se não há habilidades nem evoluções */}
              {(!selectedPokemon.habilidades || selectedPokemon.habilidades.length === 0) && 
               (!selectedPokemon.evolucoes || selectedPokemon.evolucoes.length === 0) && (
                <div className="card-habilidade">
                  <h2>Informações</h2>
                  <div className="habilidade">
                    <p>Este Pokémon não possui habilidades ou evoluções cadastradas no banco de dados.</p>
                  </div>
                </div>
              )}
            </div>
          </div>
        ) : (
          <div className="pokemon-details">
            <h2>Detalhes do Pokémon</h2>
            <div className="card placeholder">
              <div className="card-header">
                <h1>👆 Selecione um Pokémon</h1>
                <p>Clique em um Pokémon da lista para ver seus detalhes completos</p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;