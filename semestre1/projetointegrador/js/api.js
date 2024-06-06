import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://info.dengue.mat.br/services/api')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Erro ao buscar dados:', error));
  }, []);

  return (
    <div>
      <h1>Dados da API</h1>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : 'Carregando...'}
    </div>
  );
}

export default App;
