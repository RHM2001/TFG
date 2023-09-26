const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());

app.get('/get-spotify-token', async (req, res) => {
  try {
    const clientId = '5ba3471f79a443b49a0135b669294f42';
    const clientSecret = '55179f174d5e433d9a16eb9b8fa9c333';
    const scope = 'user-library-read';
    const redirectUri = 'http://localhost:5173/#/';

    const response = await axios.post(
      'https://accounts.spotify.com/api/token',
      null,
      {
        params: {
          grant_type: 'client_credentials',
        },
        headers: {
          'Authorization': 'Basic ' + Buffer.from(`${clientId}:${clientSecret}`).toString('base64'),
        },
      }
    );

    const accessToken = response.data.access_token;

    res.json({ access_token: accessToken });
  } catch (error) {
    console.error('Error al obtener el token de acceso:', error);
    res.status(500).json({ error: 'Error al obtener el token de acceso' });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});
