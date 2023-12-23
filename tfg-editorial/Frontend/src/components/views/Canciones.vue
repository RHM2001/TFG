<template>
    <h1 class="text-4xl font-medium leading-tight text-black text-center font-lara mt-6">
        Gestión de canciones
    </h1>

    <div class="container mx-auto py-8 lg:pt-8 fade-in">

        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">


            <div class="relative mb-3 flex flex-wrap items-stretch">


                <input id="datatable-search-input" type="search"
                    class="relative m-0 -mr-0.5 block w-[1px] min-w-0 flex-auto rounded-l border border-solid border-gray-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-gray-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-l-pink-600 focus:text-gray-700 focus:shadow-[inset_0_0_0_1px_rgb(203,81,163)] "
                    placeholder="Buscar" aria-label="Buscar" aria-describedby="button-addon1" />


                <div class="relative">
                    <a class="flex items-center whitespace-nowrap text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-pink-300 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        type="button" data-te-toggle="modal" data-te-target="#exampleModalCenter" data-te-ripple-init
                        data-te-ripple-color="light" @click="showFiltersModal">
                        Filtros
                    </a>
                </div>

            </div>


            <div>
                <div id="datatable"></div>
            </div>
        </div>
    </div>

    <!-- Modal para configurar los filtros -->
    <div data-te-modal-init
        class="fixed left-0 top-0 z-[1055] hidden h-full w-full overflow-y-auto overflow-x-hidden outline-none"
        id="exampleModalCenter" tabindex="-1" aria-labelledby="exampleModalCenterTitle" aria-modal="true" role="dialog">
        <div data-te-modal-dialog-ref
            class="pointer-events-none relative flex min-h-[calc(100%-1rem)] w-auto translate-y-[-50px] items-center opacity-0 transition-all duration-300 ease-in-out min-[576px]:mx-auto min-[576px]:mt-7 min-[576px]:min-h-[calc(100%-3.5rem)] min-[576px]:max-w-[500px]">
            <div
                class="pointer-events-auto relative flex w-full flex-col rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none dark:bg-neutral-600">
                <div
                    class="flex flex-shrink-0 items-center justify-between rounded-t-md border-b-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
                    <!-- Modal title -->
                    <h5 class="text-xl font-medium leading-normal text-neutral-800 dark:text-neutral-200"
                        id="exampleModalCenterTitle">
                        Filtrar canciones
                    </h5>
                    <!-- Close button -->
                    <button type="button"
                        class="box-content rounded-none border-none hover:no-underline hover:opacity-75 focus:opacity-100 focus:shadow-none focus:outline-none"
                        data-te-modal-dismiss aria-label="Close">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="h-6 w-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!-- Modal body -->
                <div class="relative p-4">
                    <!-- Sección de géneros -->
                    <div class="mb-4">
                        <h6 class="text-lg font-medium mb-2">Géneros</h6>
                        <select id="selectGeneros" ref="generosSelect" data-te-select-init multiple
                            class="w-full border rounded p-2">
                            <option v-for="genero in generos" :value="genero.id" :key="genero.id">{{ genero.nombre }}
                            </option>
                        </select>

                    </div>

                    <!-- Sección de artistas -->
                    <div class="mb-4">
                        <h6 class="text-lg font-medium mb-2">Artistas</h6>
                        <select id="selectEntidades" ref="gruposSelect" data-te-select-init multiple
                            class="w-full border rounded p-2">
                            <option v-for="entidad in entidades" :value="entidad.id" :key="entidad.id">{{ entidad.nombre }}
                            </option>
                        </select>
                    </div>

                </div>

                <!-- Modal footer -->

                <div
                    class="flex items-center justify-between rounded-b-md border-t-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">

                    <div class="flex items-center space-x-4">
                        <button type="button"
                            class="inline-block rounded bg-slate-400 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white transition duration-150 ease-in-out hover:bg-primary-accent-100 focus:bg-primary-accent-100 focus:outline-none focus:ring-0 active:bg-primary-accent-200"
                            data-te-ripple-init data-te-ripple-color="light" @click="limpiarFiltros">
                            Limpiar
                        </button>
                    </div>

                    <div class="flex items-center space-x-4">
                        <button type="button"
                            class="inline-block rounded bg-pink-100 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-primary-700 transition duration-150 ease-in-out hover:bg-primary-accent-100 focus:bg-primary-accent-100 focus:outline-none focus:ring-0 active:bg-primary-accent-200"
                            data-te-modal-dismiss data-te-ripple-init data-te-ripple-color="light">
                            Cerrar
                        </button>

                        <button type="button"
                            class="inline-block rounded bg-pink-500 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(59,113,202,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)]"
                            data-te-modal-dismiss data-te-ripple-init data-te-ripple-color="light"
                            @click="actualizarTablaConFiltros">
                            Guardar filtros
                        </button>
                    </div>

                </div>

            </div>
        </div>
    </div>


    <!--Vertically centered modal-->
    <div data-te-modal-init
        class="fixed left-0 top-0 z-[1055] hidden h-full w-full overflow-y-auto overflow-x-hidden outline-none"
        id="modalEditar" tabindex="-1" aria-labelledby="exampleModalCenterTitle" aria-modal="true" role="dialog">
        <div data-te-modal-dialog-ref
            class="pointer-events-none relative flex min-h-[calc(100%-1rem)] w-auto translate-y-[-50px] items-center opacity-0 transition-all duration-300 ease-in-out min-[576px]:mx-auto min-[576px]:mt-7 min-[576px]:min-h-[calc(100%-3.5rem)] min-[576px]:max-w-[500px]">
            <div
                class="pointer-events-auto relative flex w-full flex-col rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none dark:bg-neutral-600">
                <div
                    class="flex flex-shrink-0 items-center justify-between rounded-t-md border-b-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
                    <!--Modal title-->
                    <h5 class="text-xl font-medium leading-normal text-neutral-800 dark:text-neutral-200"
                        id="exampleModalCenterTitle">
                        Cancion:
                    </h5>
                    <!--Close button-->
                    <button type="button"
                        class="box-content rounded-none border-none hover:no-underline hover:opacity-75 focus:opacity-100 focus:shadow-none focus:outline-none"
                        data-te-modal-dismiss aria-label="Close">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="h-6 w-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!--Modal body-->
                <div class="relative overflow-y-auto p-4">

                    <div class="relative mb-4 flex flex-stretch items-stretch">
                        <span
                            class="flex items-center whitespace-nowrap rounded-l border border-r-0 border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral-700 dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                            id="inputGroup-sizing-default">Canción</span>
                        <input type="text"
                            class="relative m-0 block w-[1px] min-w-0 flex-auto rounded-r border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                            id="input-cancion" aria-label="Sizing example input"
                            aria-describedby="inputGroup-sizing-default" v-model="cancionModal.nombre" />
                    </div>

                    <div class="relative mb-4 flex flex-stretch items-stretch">
                        <span
                            class="flex items-center whitespace-nowrap rounded-l border border-r-0 border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral-700 dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                            id="inputGroup-sizing-default">Artista</span>
                        <input type="text"
                            class="relative m-0 block w-[1px] min-w-0 flex-auto rounded-r border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                            id="input-artista" aria-label="Sizing example input"
                            aria-describedby="inputGroup-sizing-default" v-model="cancionModal.artista"/>
                    </div>

                    <div class="relative mb-4 flex flex-stretch items-stretch">
                        <span
                            class="flex items-center whitespace-nowrap rounded-l border border-r-0 border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral-700 dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                            id="inputGroup-sizing-default">Género</span>
                        <input type="text"
                            class="relative m-0 block w-[1px] min-w-0 flex-auto rounded-r border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                            id="input-genero" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"
                            v-model="cancionModal.genero" />
                    </div>

                    <div class="relative mb-4 flex flex-stretch items-stretch">
                        <span
                            class="flex items-center whitespace-nowrap rounded-l border border-r-0 border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral-700 dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                            id="inputGroup-sizing-default">Duración</span>
                        <input type="text"
                            class="relative m-0 block w-[1px] min-w-0 flex-auto rounded-r border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                            id="input-duracion" aria-label="Sizing example input"
                            aria-describedby="inputGroup-sizing-default" v-model="cancionModal.duracion" />
                    </div>

                    <div class="relative mb-4 flex flex-stretch items-stretch">
                        <span
                            class="flex items-center whitespace-nowrap rounded-l border border-r-0 border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral-700 dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                            id="inputGroup-sizing-default">Fecha</span>
                        <input type="text"
                            class="relative m-0 block w-[1px] min-w-0 flex-auto rounded-r border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                            id="input-url" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"
                            v-model="cancionModal.fecha" />
                    </div>

                    <div class="relative mb-4 flex flex-stretch items-stretch">
                        <span
                            class="flex items-center whitespace-nowrap rounded-l border border-r-0 border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral-700 dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                            id="inputGroup-sizing-default">Url</span>
                        <input type="text"
                            class="relative m-0 block w-[1px] min-w-0 flex-auto rounded-r border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                            id="input-url" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"
                            v-model="cancionModal.url" />
                    </div>

                    <div class="relative mb-4 flex flex-stretch items-stretch">
                        <span
                            class="flex items-center whitespace-nowrap rounded-l border border-r-0 border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral-700 dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                            id="inputGroup-sizing-default">Spotify</span>
                        <input type="text"
                            class="relative m-0 block w-[1px] min-w-0 flex-auto rounded-r border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                            id="input-spotify" aria-label="Sizing example input"
                            aria-describedby="inputGroup-sizing-default" v-model="cancionModal.spotify" />
                    </div>

                </div>


                <!--Modal footer-->
                <div
                    class="flex flex-shrink-0 flex-wrap items-center justify-end rounded-b-md border-t-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
                    <button type="button"
                        class="inline-block rounded bg-danger-500 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white transition duration-150 ease-in-out hover:bg-primary-accent-100 focus:bg-primary-accent-100 focus:outline-none focus:ring-0 active:bg-primary-accent-200"
                        data-te-modal-dismiss data-te-ripple-init data-te-ripple-color="light">
                        Revertir
                    </button>
                    <button type="button"
                        class="ml-1 inline-block rounded bg-success px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(59,113,202,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)]"
                        data-te-ripple-init data-te-ripple-color="light">
                        Guardar cambios
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import {
    Datatable,
} from "tw-elements";

export default {
    data() {
        return {
            generos: [],
            entidades: [],
            filtros: {
                generos: [],
                entidades: [],
            },
            cancionModal: {
                nombre: '',
                artista: '',
                genero: '',
                fecha: '',
                duracion: '',
                url: '',
                spotify: ''
            },
        };
    },
    mounted() {
        this.showFiltersModal();
        this.fetchCanciones();
    },
    methods: {

        async showFiltersModal() {
            // Cuando se muestra el modal de filtros, obtén los géneros y las entidades
            this.generos = await this.fetchAllGenerosNames();
            this.entidades = await this.fetchAllEntidadesNames();
        },

        async limpiarFiltros() {

            var select1 = document.querySelector("#selectGeneros");
            var options1 = select1.options;

            for (var i = 0; i < options1.length; i++) {
                if (options1[i].selected) {
                    options1[i].selected = false;
                }
            }

            select1.value = "";

            var select2 = document.querySelector("#selectEntidades");
            var options2 = select2.options;

            for (var i = 0; i < options2.length; i++) {
                if (options2[i].selected) {
                    options2[i].selected = false;
                }
            }

            select2.value = "";
        },

        async actualizarTablaConFiltros() {
            try {
                const selectGeneros = document.querySelector("#selectGeneros");
                const selectEntidades = document.querySelector("#selectEntidades");

                // Guarda los filtros seleccionados en el objeto filtros
                const generosSeleccionados = Array.from(selectGeneros.selectedOptions).map(opcion => opcion.value);
                const entidadesSeleccionadas = Array.from(selectEntidades.selectedOptions).map(opcion => opcion.value);

                console.log('EntidadesIDS:', entidadesSeleccionadas);
                console.log('GenerosIDS:', generosSeleccionados);

                const response = await axios.get('http://localhost:8000/api/editorial/canciones/', {
                    params: {
                        'entidades[]': entidadesSeleccionadas,
                        'generos[]': generosSeleccionados,
                    },
                });

                console.log('URL de la solicitud:', response.config.url);

                // Procesa los datos obtenidos del servidor
                const canciones = await Promise.all(response.data.map(async (cancion) => {
                    await this.fetchEntidadName(cancion);
                    await this.fetchGeneroNames(cancion);

                    return {
                        cancion: cancion.nombre,
                        artista: cancion.entidadNombre,
                        genero: cancion.generoNombres.join(', '),
                        duracion: cancion.duracion,
                        url: cancion.url,
                        fecha: cancion.fecha,
                        idSpotify: cancion.idSpotify,
                        id: cancion.id,
                    };
                }));

                // Actualiza la tabla con los datos filtrados
                const columns = [
                    { label: "Canción", field: "cancion" },
                    { label: "Artista", field: "artista" },
                    { label: "Género", field: "genero" },
                    { label: "Duración", field: "duracion" },
                    { label: "Url", field: "url" },
                    { label: "Fecha", field: "fecha" },
                    { label: "Spotify", field: "idSpotify" },
                    { label: "Id", field: "id" },
                ];

                const data = {
                    columns,
                    rows: canciones,
                };

                this.initDataTable(data);

            } catch (error) {
                console.error('Error fetching canciones:', error);
            }
        },

        async fetchCanciones() {
            try {
                const response = await axios.get('http://localhost:8000/api/editorial/canciones/');
                const canciones = await Promise.all(response.data.map(async (cancion) => {
                    await this.fetchEntidadName(cancion);
                    await this.fetchGeneroNames(cancion);

                    const botonEditar = `<button class="btn-editar" data-te-toggle="modal" data-te-target="#modalEditar" data-id="${cancion.id}"></button>`;

                    return {
                        cancion: cancion.nombre,
                        artista: cancion.entidadNombre,
                        genero: cancion.generoNombres.join(', '),
                        duracion: cancion.duracion,
                        url: cancion.url,
                        fecha: cancion.fecha,
                        idSpotify: cancion.idSpotify,
                        id: cancion.id,
                        editar: botonEditar,
                    };
                }));

                const columns = [
                    { label: "Canción", field: "cancion" },
                    { label: "Artista", field: "artista" },
                    { label: "Género", field: "genero" },
                    { label: "Duración", field: "duracion" },
                    { label: "Url", field: "url" },
                    { label: "Fecha", field: "fecha" },
                    { label: "Spotify", field: "idSpotify" },
                    { label: "Id", field: "id" },
                    { label: "Editar", field: "editar", sort: false },
                ];

                const data = {
                    columns,
                    rows: canciones,
                };

                this.initDataTable(data);

                const tableContainer = document.getElementById('datatable');
                tableContainer.addEventListener('click', (event) => {
                    const target = event.target;
                    if (target.classList.contains('btn-editar')) {
                        const idCancion = target.getAttribute('data-id');
                        this.cambiarInfoModal(idCancion);
                    }
                });

            } catch (error) {
                console.error('Error fetching canciones:', error);
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

        initDataTable(data) {

            const tableElement = document.getElementById('datatable');
            tableElement.innerHTML = '';

            const instance = new Datatable(document.getElementById('datatable'), data, {
                hover: true,
            });

            document.getElementById('datatable-search-input').addEventListener('input', (e) => {
                instance.search(e.target.value);
            });
        },

        async fetchAllGenerosNames() {
            let allGeneros = []; // Inicializar lista de géneros

            try {
                // Obtén los géneros desde la API de Django
                const generoResponse = await axios.get('http://localhost:8000/api/editorial/generos/');

                // Verificar si los datos se recibieron correctamente
                if (generoResponse.status === 200) {
                    // Asigna los nombres de los géneros a la lista allGeneros
                    allGeneros = generoResponse.data.map(genero => genero);
                } else {
                    console.error('Error al obtener los géneros:', generoResponse.statusText);
                }
            } catch (error) {
                console.error('Error al obtener los géneros:', error);
                // Asignar un arreglo vacío en caso de error
                allGeneros = [];
            }
            // Devuelve la lista de nombres de géneros
            return allGeneros;
        },

        async fetchAllEntidadesNames() {
            let allEntidades = []; // Inicializar lista de géneros

            try {
                // Obtén los géneros desde la API de Django
                const entidadResponse = await axios.get('http://localhost:8000/api/editorial/entidades/');

                // Verificar si los datos se recibieron correctamente
                if (entidadResponse.status === 200) {
                    // Asigna los nombres de los géneros a la lista allGeneros
                    allEntidades = entidadResponse.data.map(entidad => entidad);
                } else {
                    console.error('Error al obtener las entidades:', entidadResponse.statusText);
                }
            } catch (error) {
                console.error('Error al obtener las entidades:', error);
                // Asignar un arreglo vacío en caso de error
                allEntidades = [];
            }
            // Devuelve la lista de nombres de géneros
            return allEntidades;
        },

        async cambiarInfoModal(idCancion) {
            try {
                const response = await axios.get(`http://localhost:8000/api/editorial/canciones/${idCancion}`);
                const cancion = response.data;

                await this.fetchEntidadName(cancion);
                await this.fetchGeneroNames(cancion);

                this.cancionModal.nombre = cancion.nombre;
                this.cancionModal.artista = cancion.entidad;
                this.cancionModal.genero = cancion.genero;
                this.cancionModal.fecha = cancion.fecha;
                this.cancionModal.duracion = cancion.duracion;
                this.cancionModal.url = cancion.url;
                this.cancionModal.spotify = cancion.idSpotify;

            } catch (error) {
                console.error('Error fetching canciones:', error);
            }

        },

    }
}
</script>

<style>
.btn-editar {
    background-image: url('../../public/images/configuraciones.png');
    /* Ruta de la imagen */
    background-size: cover;
    /* Ajusta el tamaño de la imagen para cubrir completamente el botón */
    width: 35px;
    /* Ancho del botón */
    height: 35px;
    /* Altura del botón */
}
</style>