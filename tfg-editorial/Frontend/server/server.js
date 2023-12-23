const express = require('express');
const axios = require('axios');
const cors = require('cors');
const querystring = require('querystring');
const app = express();
const url = require('url');


const clientId = '5ba3471f79a443b49a0135b669294f42';
const clientSecret = '55179f174d5e433d9a16eb9b8fa9c333';
const redirectUri = 'http://localhost:3000/callback'; // Asegúrate de que coincida con la configuración en la aplicación de Spotify

var accessToken = null;
var refreshToken = null;

const PORT = 3000;

// Otras rutas y configuraciones aquí...

const corsOptions = {
    origin: 'http://localhost:5173',
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true, // Habilita el intercambio de cookies o credenciales para las solicitudes CORS
    optionsSuccessStatus: 204, // Al responder a una solicitud OPTIONS, indica que está permitido ('No Content')
};

app.use(cors(corsOptions));

// Ruta raíz
app.get('/', (req, res) => {
    res.send('¡Hola, mundo!'); // Puedes enviar cualquier contenido que desees mostrar en la página principal.
});


app.get('/login', (req, res) => {
    const scopes = 'user-read-private user-read-email';
    res.redirect(`https://accounts.spotify.com/authorize?response_type=token&client_id=${clientId}&scope=${encodeURIComponent(scopes)}&redirect_uri=${encodeURIComponent(redirectUri)}`);
});


app.get('/callback', (req, res) => {
    const parsedUrl = url.parse(req.url);
    const fragment = parsedUrl.hash.substr(1);
    const params = new URLSearchParams(fragment);
    accessToken = params.get('access_token');
    console.log("TOKEN EN CALLBACK : " + accessToken);

    res.redirect('http://localhost:5173/sincronizacion');
});


app.get('/verificar-sesion-spotify', (req, res) => {
    // Verifica la autenticación del usuario en Spotify usando el token de acceso
    axios.get('https://api.spotify.com/v1/me', {
        headers: {
            'Authorization': 'Bearer ' + accessToken,
        },
    })
        .then((response) => {
            // Si la solicitud a la API de Spotify es exitosa, el usuario está autenticado
            res.sendStatus(200); // OK
        })
        .catch((error) => {
            // Si la solicitud a la API de Spotify falla, el usuario no está autenticado
            res.sendStatus(401); // No autorizado
        });
});

// En el servidor (Node.js)
app.post('/guardar-token', (req, res) => {
    accessToken = req.body.accessToken;

    res.sendStatus(200); // OK
});




app.listen(3000, () => {
    console.log('Servidor escuchando en el puerto 3000');
    console.log("TOKEN : " + accessToken);
});
