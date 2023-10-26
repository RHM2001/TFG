<template>
    <div class="container mx-auto py-8 lg:pt-8 fade-in">

        <div class="mb-3">
            <div v-if="!isLoggedIn" class="relative flex flex-wrap items-stretch">
                <button @click="loginWithSpotify" type="button" id="botonLoginSpotify"
                    class="custom-button text-dark bg-gradient-to-r from-green-400 via-green-500 to-green-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-green-300 dark:focus:ring-green-800 shadow-lg dark:shadow-lg dark:shadow-green-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                    <img src="public/images/spotify_icon_32.png" alt="Descripción de la imagen" class="button-image">
                    Login
                </button>
                <span class="flex items-center whitespace-nowrap">Iniciar sesión para escuchar las canciones.</span>
            </div>

            <iframe id="spotify-iframe" v-if="accessToken" style="border-radius:12px" width="100%" height="152"
                frameBorder="0" allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>

        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
            <h1 class="mb-2 text-3xl font-medium leading-tight text-black text-center font-lara">
                Explora el Universo Musical de nuestra editorial
            </h1>

            <div class="relative mb-3 flex flex-wrap items-stretch">


                <input id="datatable-search-input" type="search"
                    class="relative m-0 -mr-0.5 block w-[1px] min-w-0 flex-auto rounded-l border border-solid border-gray-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-gray-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-l-pink-600 focus:text-gray-700 focus:shadow-[inset_0_0_0_1px_rgb(203,81,163)] "
                    placeholder="Buscar" aria-label="Buscar" aria-describedby="button-addon1" />


                <div class="relative" data-te-dropdown-ref>
                    <a class="flex items-center whitespace-nowrap text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        type="button" id="dropdownMenuButton1" data-te-dropdown-toggle-ref aria-expanded="false"
                        data-te-ripple-init data-te-ripple-color="light">
                        Filtros
                        <span class="ml-2 w-2">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                                <path fill-rule="evenodd"
                                    d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                                    clip-rule="evenodd" />
                            </svg>
                        </span>
                    </a>
                    <ul class="absolute z-[1000] float-left m-0 hidden min-w-max list-none overflow-hidden rounded-lg
                        border-none bg-white bg-clip-padding text-left text-base shadow-lg dark:bg-neutral-700
                        [&[data-te-dropdown-show]]:block" aria-labelledby="dropdownMenuButton1"
                        data-te-dropdown-menu-ref>
                        <li>
                            <a class="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-neutral-600"
                                data-te-dropdown-item-ref>Género</a>
                        </li>
                        <li>
                            <a class="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-neutral-600"
                                data-te-dropdown-item-ref>Duración</a>
                        </li>
                        <li>
                            <a class="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-neutral-600"
                                data-te-dropdown-item-ref>Entidad</a>
                        </li>
                    </ul>
                </div>
            </div>

            <div>
                <div id="datatable" data-te-selectable="true" data-te-multi="true">></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import {
    Datatable,
    initTE,
} from "tw-elements";

initTE({ Datatable });


export default {
    data() {
        return {
            canciones: [],
            isLoggedIn: false,
            accessToken: null,
        };
    },
    mounted() {
        const accessTokenFromURL = window.location.hash.substr(1).split('&')[0].split('=')[1];

        if (accessTokenFromURL) {
            this.accessToken = accessTokenFromURL;
            this.isLoggedIn = true;
            this.getSpotifyEmbedUrl(this.accessToken).then(() => {
                this.fetchCanciones();
            });
        } else {
            this.fetchCanciones();
        }
    }
    ,
    methods: {

        async getSpotifyEmbedUrl(accessToken) {
            console.log('Access Token:', accessToken);
            await this.$nextTick(); // Espera a que Vue haya renderizado el componente
            const iframeElement = document.getElementById('spotify-iframe');
            console.log('Iframe Element:', iframeElement);
            if (iframeElement) {
                const spotifyEmbedUrl = `https://open.spotify.com/embed/track/60PHayCjXTNL0iw81DlNxi?utm_source=generator&access_token=${accessToken}`;
                iframeElement.src = spotifyEmbedUrl;
            } else {
                console.error('Element with ID "spotify-iframe" not found');
            }
        },


        async fetchCanciones() {
            try {
                const response = await axios.get('http://localhost:8000/api/editorial/canciones/');
                const canciones = await Promise.all(response.data.map(async (cancion) => {
                    await this.fetchEntidadName(cancion);
                    await this.fetchGeneroNames(cancion);

                    const botonEscuchar = `<button class="btn-escuchar animate-fade-in" data-id="${cancion.idSpotify}"></button>`;
                    //const botonEscuchar = `<button class="btn-escuchar" data-id="${cancion.idSpotify}"> <img class="btn-image" src="public/images/boton-de-play.png" alt="Descripción de la imagen"></button>`;

                    return {
                        cancion: cancion.nombre,
                        artista: cancion.entidadNombre,
                        genero: cancion.generoNombres.join(', '),
                        duracion: cancion.duracion,
                        escucha: botonEscuchar,
                    };
                }));

                const columns = [
                    { label: "Canción", field: "cancion" },
                    { label: "Artista", field: "artista" },
                    { label: "Género", field: "genero" },
                    { label: "Duración", field: "duracion" },
                    { label: "Escucha", field: "escucha", sort: false },
                ];

                const data = {
                    columns,
                    rows: canciones,
                };

                this.initDataTable(data);

                const tableContainer = document.getElementById('datatable');
                tableContainer.addEventListener('click', (event) => {
                    const target = event.target;
                    if (target.classList.contains('btn-escuchar')) {
                        const idSpotify = target.getAttribute('data-id');
                        if (!this.isLoggedIn) {
                            console.error('Iniciar sesión en Spotify');
                        } else if (idSpotify) {
                            console.log('ID de SPOTIFY: ' + idSpotify);
                            this.reproducirCancion(idSpotify);
                        } else {
                            console.error('ID de Spotify es nulo o indefinido');
                        }
                    }
                });
            } catch (error) {
                console.error('Error fetching canciones:', error);
            }
        },

        async reproducirCancion(idSpotify) {
            try {
                console.log("ID de SPOTIFY desde el reproducir : " + idSpotify);
                console.log(`Clic en el botón de reproducción. ID de Spotify: ${idSpotify}`);

                // Construye el enlace de Spotify
                const spotifyEmbedUrl = `https://open.spotify.com/embed/track/${idSpotify}?utm_source=generator&access_token=${this.accessToken}`;

                // Actualiza el iframe con el nuevo enlace
                const iframeElement = document.getElementById('spotify-iframe');
                iframeElement.src = spotifyEmbedUrl;
            } catch (error) {
                console.error('Error al obtener el ID de Spotify:', error);
            }
        },

        initDataTable(data) {

            const tableElement = document.getElementById('datatable');
            tableElement.innerHTML = '';

            const instance = new Datatable(document.getElementById('datatable'), data);

            document.getElementById('datatable-search-input').addEventListener('input', (e) => {
                instance.search(e.target.value);
            });
        },

        loginWithSpotify() {
            const clientId = '5ba3471f79a443b49a0135b669294f42';
            const scopes = 'user-read-private user-read-email'; // Agrega los permisos que necesites
            const redirectUri = 'http://localhost:5173/sincronizacion'; // Asegúrate de que coincida con la configuración en la aplicación de Spotify

            // Redirigir al usuario a la página de autorización de Spotify
            window.location.href = `https://accounts.spotify.com/authorize?response_type=token&client_id=${clientId}&scope=${encodeURIComponent(scopes)}&redirect_uri=${encodeURIComponent(redirectUri)}`;
        },

        checkAuthorizationCode() {
            const urlSearchParams = new URLSearchParams(window.location.search);
            const code = urlSearchParams.get('code');

            if (code) {
                // El usuario ha iniciado sesión y autorizado la aplicación
                // Usa el código de autorización para obtener tokens de acceso y actualización
                this.exchangeCodeForTokens(code);
            } else {
                console.error('Código de autorización no encontrado en la URL');
            }
        },

        async exchangeCodeForTokens(code) {
            const clientId = '5ba3471f79a443b49a0135b669294f42'; // Reemplaza con tu ID de cliente de Spotify
            const clientSecret = '55179f174d5e433d9a16eb9b8fa9c333'; // Reemplaza con tu secreto de cliente de Spotify
            const redirectUri = 'http://localhost:3000/callback'; // Reemplaza con tu URI de redirección

            try {
                const response = await axios.post('https://accounts.spotify.com/api/token', null, {
                    params: {
                        grant_type: 'authorization_code',
                        code: code,
                        redirect_uri: redirectUri,
                    },
                    headers: {
                        'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret),
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                });

                const accessToken = response.data.access_token;
                const refreshToken = response.data.refresh_token;

                // Guarda el token de acceso y el token de actualización en tu aplicación (por ejemplo, en el estado del componente Vue.js o en las cookies)
                // ...

                console.log('Token de acceso:', accessToken);
                console.log('Token de actualización:', refreshToken);
            } catch (error) {
                console.error('Error al intercambiar el código por tokens:', error);
                const accessToken = error.response.data.access_token;
                const refreshToken = error.response.data.refresh_token;

                // Guarda el token de acceso y el token de actualización en tu aplicación (por ejemplo, en el estado del componente Vue.js o en las cookies)
                // ...

                console.log('Token de acceso:', accessToken);
                console.log('Token de actualización:', refreshToken);
            }
        },


        async fetchEntidadName(cancion) {
            try {
                const entidadResponse = await axios.get(`http://localhost:8000/api/editorial/entidades/${cancion.entidad}/`);
                cancion.entidadNombre = entidadResponse.data.nombre; // Almacena el nombre de la entidad en entidadNombre
            } catch (error) {
                console.error('Error fetching entidad:', error);
            }
        },

        async fetchIdSpotify(cancion) {
            try {
                const idSpotifyResponse = await axios.get(`http://localhost:8000/api/editorial/entidades/${cancion.idSpotify}/`);
                return cancion.idSpotify = idSpotifyResponse.data.nombre;
            } catch (error) {
                console.error('Error fetching entidad:', error);
            }
        },

        async fetchGeneroNames(cancion) {
            try {
                // Obtén los géneros relacionados con la canción actual
                const generosRelacionados = [];

                for (const generoId of cancion.genero) {
                    const generoResponse = await axios.get(`http://localhost:8000/api/editorial/generos/${generoId}/`);
                    generosRelacionados.push(generoResponse.data.nombre);
                }

                // Asigna los géneros relacionados a la propiedad generoNombres
                cancion.generoNombres = generosRelacionados;
            } catch (error) {
                console.error('Error fetching géneros:', error);
                cancion.generoNombres = []; // Asignar un arreglo vacío en caso de error
            }
        },

    },
    computed: {

    },
};

</script>

<style>
@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.fade-in {
    animation: fadeIn 1s ease-in-out;
}

.custom-button {
    display: flex;
    align-items: center;
}

.button-image {
    margin-right: 10px;
}

.btn-escuchar {
    background-image: url('public/images/boton-de-play.png');
    /* Ruta de la imagen */
    background-size: cover;
    /* Ajusta el tamaño de la imagen para cubrir completamente el botón */
    width: 35px;
    /* Ancho del botón */
    height: 35px;
    /* Altura del botón */
}

.columna-botones {
    display: flex;
    justify-content: center;
    align-items: center;
}

.animate-fade-in:hover {
    transform: scale(1.02);
}
</style>
