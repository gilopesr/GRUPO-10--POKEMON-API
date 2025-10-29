import './App.css'

function App() {
    const pokemon = {
        nome: "Bulbasaur",
        altura: "0.7 m",
        peso: "6.9 kg",
        tipos: ["Planta", "Poison"],
        vantagens: ["Água", "Terrestre", "Rocha"],
        fraquezas: ["Fogo", "Gelo", "Voador", "Psíquico"],
        habilidade: {
            nome: "Overgrow",
            descricao: "Aumenta o poder de movimentos do Tipo Planta em 50% quando o HP do Pokémon está baixo (1/3 ou menos).",
        },
        evolucao: {
            proximaForma: "Ivysaur",
            condicao: "Nível 16",
            habilidadeProxima: "Overgrow",
        }
    };

    return (
        <div className="card">
            <div className="card-header">
                <h1>{pokemon.nome}</h1>
                <div className="pokemon-stats">
                    <p><strong>Altura:</strong> {pokemon.altura}</p>
                    <p><strong>Peso:</strong> {pokemon.peso}</p>
                </div>
            </div>

            <hr /> 
            <div className="card-tipagem">
                <h2>Tipo</h2>
                <div className="tag-group">
                    {pokemon.tipos.map(tipo => (
                        <span key={tipo} className={`tag type-${tipo.toLowerCase()}`}>{tipo}</span>
                    ))}
                </div>

                <h3>Fraquezas</h3>
                <div className="tag-group">
                    {pokemon.fraquezas.map(fq => (
                        <span key={fq} className={`tag fraqueza-${fq.toLowerCase()}`}>{fq}</span>
                    ))}
                </div>
                
                <h3>Vantagens</h3>
                <div className="tag-group">
                    {pokemon.vantagens.map(vt => (
                        <span key={vt} className={`tag vantagem-${vt.toLowerCase()}`}>{vt}</span>
                    ))}
                </div>
            </div>

            <hr /> 
            <div className="card-habilidade">
                <h2>Habilidade Principal</h2>
                <h3>{pokemon.habilidade.nome}</h3>
                <p>{pokemon.habilidade.descricao}</p>
            </div>

            <hr />
            <div className="card-evolucao">
                <h2>Linha Evolutiva</h2>
                <p>Evolui para: <strong>{pokemon.evolucao.proximaForma}</strong></p>
                <p>Condição: {pokemon.evolucao.condicao}</p>
                <p>Habilidade da próxima forma: {pokemon.evolucao.habilidadeProxima}</p>
            </div>

        </div>
    );
}

export default App
