const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const port = 3000;

app.use(cors());

// Servir arquivos estáticos (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, '../')));

const data = [
  {
    "data_iniSE": 1717286400000,
    "SE": 202423,
    "casos_est": 57,
    "casos_est_min": 3,
    "casos_est_max": 598,
    "casos": 0,
    "p_rt1": 4.7e-9,
    "p_inc100k": 21.3809070587,
    "Localidade_id": 0,
    "nivel": 1,
    "id": 352050920242319900,
    "versao_modelo": "2024-06-10",
    "tweet": null,
    "Rt": 0.4213312268,
    "pop": 266593,
    "tempmin": 13.22635,
    "umidmax": 82.6953,
    "receptivo": 0,
    "transmissao": 0,
    "nivel_inc": 2,
    "umidmed": 68.56465,
    "umidmin": 45.99925,
    "tempmed": 18.1142,
    "tempmax": 25.39215,
    "casprov": 0,
    "casprov_est": null,
    "casprov_est_min": null,
    "casprov_est_max": null,
    "casconf": null,
    "notif_accum_year": 277
  },
  // ... outros dados ...
];

// Rota para fornecer os dados JSON
app.get('/api/dados', (req, res) => {
  res.json(data);
});

// Configurar a aplicação para ouvir em uma porta
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
