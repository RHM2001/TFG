import './style.css';
import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHashHistory } from 'vue-router';

import Home from './components/views/Home.vue';
import Artistas from './components/views/Artistas.vue';
import Sincronizacion from './components/views/Sincronizacion.vue';


const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/artistas', name: 'artistas', component: Artistas },
    { path: '/sincronizacion', name: 'sincronizacion', component: Sincronizacion },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

const app = createApp(App);

// Instala el enrutador creado previamente usando createRouter
app.use(router);

app.mount('#app');


// server.js
const express = require('express');
const axios = require('axios');
const cors = require('cors'); // Para habilitar el CORS si tu aplicación Vue.js se ejecuta en un dominio diferente

// Middleware
app.use(cors()); // Habilita el CORS

// Ruta para obtener el Token de Acceso
app.get('/get-spotify-token', async (req, res) => {
  try {
    const clientId = '5ba3471f79a443b49a0135b669294f42';
    const clientSecret = '55179f174d5e433d9a16eb9b8fa9c333';
    const scope = 'user-library-read'; // Especifica el alcance necesario
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

    // Devuelve el Token de Acceso como respuesta
    res.json({ access_token: accessToken });
  } catch (error) {
    console.error('Error al obtener el token de acceso:', error);
    res.status(500).json({ error: 'Error al obtener el token de acceso' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});

