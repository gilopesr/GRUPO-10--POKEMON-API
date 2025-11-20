import React from 'react';
import pokemonMap from './pokemon_map.json'; 

const BASE_IMG_URL = "https://raw.githubusercontent.com/wellrccity/pokedex-html-js/master/assets/img/pokemons/";


const PokemonImage = ({ name, style }) => {
  const pokemonNameKey = name ? name.toLowerCase() : '';
  const pokemonId = pokemonMap[pokemonNameKey]; 

  if (!pokemonId) {
    return (
      <div style={{ ...style, backgroundColor: '#ccc', textAlign: 'center', lineHeight: (style.height || '100px') }}>
        pokemon sem imagem
      </div>
    );
  }

  const imageUrl = `${BASE_IMG_URL}poke_${pokemonId}.gif`; 

  return (
    <img 
      src={imageUrl} 
      alt={`GIF de ${name}`} 
      style={style}
    />
  );
};

export default PokemonImage;