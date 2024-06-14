// URL da API
const apiUrl = 'http://localhost:3000/api/dados';

// Função para formatar a data
function formatDate(timestamp) {
  const date = new Date(timestamp);
  return date.toLocaleDateString();
}

// Função para preencher a tabela com os dados
function populateTable(data) {
  const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];

  data.forEach(item => {
    const row = tableBody.insertRow();

    const cellData = row.insertCell();
    cellData.textContent = formatDate(item.data_iniSE);

    const cellSE = row.insertCell();
    cellSE.textContent = item.SE;

    const cellCasosEst = row.insertCell();
    cellCasosEst.textContent = item.casos_est;

    const cellCasosEstMin = row.insertCell();
    cellCasosEstMin.textContent = item.casos_est_min;

    const cellCasosEstMax = row.insertCell();
    cellCasosEstMax.textContent = item.casos_est_max;

    const cellCasos = row.insertCell();
    cellCasos.textContent = item.casos;

    // Adicione mais células conforme necessário
  });
}

// Fetch data from the API and populate the table
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    populateTable(data);
  })
  .catch(error => {
    console.error('Erro ao buscar dados da API:', error);
  });
