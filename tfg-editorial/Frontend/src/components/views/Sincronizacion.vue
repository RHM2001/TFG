<template>
    <div class="container mx-auto py-8 lg:pt-8 fade-in">

        <div class="mb-3">
            <button @click="loginWithSpotify" type="button"
                class="custom-button text-dark bg-gradient-to-r from-green-400 via-green-500 to-green-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-green-300 dark:focus:ring-green-800 shadow-lg dark:shadow-lg dark:shadow-green-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                <img src="public/images/spotify_icon_32.png" alt="Descripción de la imagen" class="button-image">
                Login</button>

            <iframe style="border-radius:12px"
                src="https://open.spotify.com/embed/track/60PHayCjXTNL0iw81DlNxi?utm_source=generator" width="100%"
                height="152" frameBorder="0" allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

        </div>

        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
            <h5 class="mb-2 text-xl font-medium leading-tight text-black text-center">
                Catálogo con filtros y búsqueda
            </h5>

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

                <div id="datatable"></div>
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
            searchQuery: "",
            sortKey: 'nombre',
            sortOrder: 1,
        };
    },
    mounted() {
        this.fetchCanciones();
    },
    methods: {

        async fetchCanciones() {
            try {
                const response = await axios.get('http://localhost:8000/api/editorial/canciones/');
                const canciones = response.data.map(cancion => {
                    return [
                        cancion.nombre,
                        cancion.entidad,
                        cancion.genero,
                        cancion.duracion,
                        '<button class="btn-escuchar"> <img class="btn-image" src="public/images/boton-de-play.png" alt="Descripción de la imagen"></button>',
                    ]
                });

                const columns = ['Canción', 'Artista', 'Género', 'Duración', 'Escucha'];
                const data = {
                    columns,
                    rows: canciones,
                };

                // Inicializa el DataTable con los datos obtenidos
                this.initDataTable(data);
            } catch (error) {
                console.error('Error fetching canciones:', error);
            }
        },

        initDataTable(data) {
            const instance = new Datatable(document.getElementById('datatable'), data);

            document.getElementById('datatable-search-input').addEventListener('input', (e) => {
                instance.search(e.target.value);
            });
        },

        loginWithSpotify() {
            const clientId = '5ba3471f79a443b49a0135b669294f42';
            const redirectUri = 'http://localhost:5173/sincronizacion';
            const scopes = ['user-read-private', 'user-read-email']; // Agregue los permisos que necesite

            const authUrl = `https://accounts.spotify.com/authorize?response_type=code&client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scopes.join('%20')}`;


            window.location.href = authUrl;
        },

        async fetchEntidadName(cancion) {
            try {
                const entidadResponse = await axios.get(`http://localhost:8000/api/editorial/entidades/${cancion.entidad}/`);
                cancion.entidadNombre = entidadResponse.data.nombre; // Almacena el nombre de la entidad en entidadNombre
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
    display: flex;
    justify-content: center;
    align-items: center;
}

.btn-escuchar .btn-image {
    width: 35px;
    height: 35px;
}

.columna-botones {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
