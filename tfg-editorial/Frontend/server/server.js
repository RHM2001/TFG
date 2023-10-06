const express = require('express');
const axios = require('axios');
const querystring = require('querystring');
const app = express();

const clientId = '5ba3471f79a443b49a0135b669294f42';
const clientSecret = '55179f174d5e433d9a16eb9b8fa9c333';
const redirectUri = 'http://localhost:3000/callback'; // Asegúrate de que coincida con la configuración en la aplicación de Spotify

const PORT = 3000;

// Otras rutas y configuraciones aquí...

// Ruta raíz
app.get('/', (req, res) => {
    res.send('¡Hola, mundo!'); // Puedes enviar cualquier contenido que desees mostrar en la página principal.
});


app.get('/login', (req, res) => {
    const scopes = 'user-read-private user-read-email'; // Agrega los permisos que necesites
    res.redirect(`https://accounts.spotify.com/authorize?response_type=code&client_id=${clientId}&scope=${encodeURIComponent(scopes)}&redirect_uri=${encodeURIComponent(redirectUri)}`);
});


app.get('/callback', async (req, res) => {
    const code = req.query.code || null;
    console.log("CodigooooooooooooooooOOOOooo " + code);

    try {
        const response = await axios.post('https://accounts.spotify.com/api/token', querystring.stringify({
            grant_type: 'authorization_code',
            code: code,
            redirect_uri: redirectUri,
        }), {
            headers: {
                'Authorization': 'Basic ' + Buffer.from(clientId + ':' + clientSecret).toString('base64'),
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });

        const accessToken = response.data.access_token;
        const refreshToken = response.data.refresh_token;

        // Puedes guardar accessToken y refreshToken en una base de datos o en memoria, dependiendo de tus necesidades.

        // Ahora redirige al usuario a la página principal o a donde quieras.
        res.redirect('http://localhost:5173/sincronizacion');
    } catch (error) {
        console.error('Error al intercambiar el código por tokens:', error);
        res.status(500).send('Error al autenticar con Spotify');
    }
});

app.get('/verificar-sesion-spotify', (req, res) => {
    // Implementa la lógica para verificar el estado de la sesión de Spotify aquí
    // Si el usuario está autenticado, envía una respuesta con código 200 (OK)
    // Si el usuario no está autenticado, envía una respuesta con código 401 (No autorizado)
    // Puedes usar la biblioteca 'spotify-web-api-node' para verificar la sesión de Spotify

    // Ejemplo de cómo podrías implementar esto:
    if (usuarioEstaAutenticadoEnSpotify) {
        res.sendStatus(200); // OK
    } else {
        res.sendStatus(401); // No autorizado
    }
});

app.listen(3000, () => {
    console.log('Servidor escuchando en el puerto 3000');
});
