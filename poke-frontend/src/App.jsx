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
      setError('Erro ao carregar pokémons da API');
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
    }
  };

  if (loading) return <div className="loading">Carregando pokémons...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="app">
      <header className="app-header">
        <h1>Pokédex - API Pokémon</h1>
        <p>Conectado com backend Flask</p>
      </header>

      <div className="container">
        <div className="pokemon-list">
          <h2>Lista de Pokémons</h2>
          <div className="pokemon-grid">
            {pokemons.map(pokemon => (
              <div 
                key={pokemon.id} 
                className="pokemon-card"
                onClick={() => fetchPokemonDetails(pokemon.id)}
              >
                <h3>{pokemon.nome}</h3>
                <p><strong>Tipo:</strong> {pokemon.tipo || 'N/A'}</p>
                <p><strong>Altura:</strong> {pokemon.altura}</p>
                <p><strong>Peso:</strong> {pokemon.peso}</p>
                {pokemon.habilidades && (
                  <p><strong>Habilidades:</strong> {pokemon.habilidades.length}</p>
                )}
              </div>
            ))}
          </div>
        </div>

        {selectedPokemon && (
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

              {selectedPokemon.evolucoes && selectedPokemon.evolucoes.length > 0 && (
                <>
                  <hr />
                  <div className="card-evolucao">
                    <h2>Evoluções</h2>
                    {selectedPokemon.evolucoes.map(evo => (
                      <div key={evo.id} className="evolucao">
                        <p>Evolui para: <strong>{evo.para_pokemon}</strong></p>
                        <p>Condição: {evo.condicao}</p>
                        {evo.habilidade && <p>Habilidade: {evo.habilidade}</p>}
                      </div>
                    ))}
                  </div>
                </>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;