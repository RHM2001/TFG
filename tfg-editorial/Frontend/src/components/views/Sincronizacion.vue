<template>
    <div class="container mx-auto py-8 lg:pt-8 fade-in">

        <div id="alertContainer"></div>

        <div class="mb-3">
            <div v-if="!isLoggedIn" class="relative flex flex-wrap items-stretch">
                <button @click="loginWithSpotify" type="button" id="botonLoginSpotify"
                    class="custom-button text-dark bg-gradient-to-r from-green-400 via-green-500 to-green-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-green-300 dark:focus:ring-green-800 shadow-lg dark:shadow-lg dark:shadow-green-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                    <img src="public/images/spotify_icon_32.png" alt="Descripción de la imagen" class="button-image">
                    Login
                </button>
                <span class="flex items-center font-lara whitespace-nowrap text-2xl">Iniciar sesión para escuchar las
                    canciones.</span>
            </div>

            <iframe id="spotify-iframe" v-if="accessToken" style="border-radius:12px" width="100%" height="152"
                frameBorder="0" allowfullscreen=""
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>

        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
            <h1 class="mb-2 text-4xl font-medium leading-tight text-black text-center font-lara">
                Explora el Universo Musical de nuestra editorial
            </h1>

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
                <div id="datatable" data-te-selectable="true" data-te-multi="true"></div>
            </div>
        </div>

        <div v-if="!isSongSelect" class="relative flex flex-wrap center py-2">
            <button type="button" data-te-toggle="modal" data-te-target="#modalContacto" data-te-ripple-init
                class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg  font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">Contactar
                para sincronización</button>
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

    <!-- Modal para contacto de sincronización -->
    <div data-te-modal-init
        class="fixed left-0 top-0 z-[1055] hidden h-full w-full overflow-y-auto overflow-x-hidden outline-none"
        id="modalContacto" tabindex="-1" aria-labelledby="exampleModalScrollableLabel" aria-hidden="true">
        <div data-te-modal-dialog-ref
            class="pointer-events-none relative h-[calc(100%-1rem)] w-auto translate-y-[-50px] opacity-0 transition-all duration-300 ease-in-out min-[576px]:mx-auto min-[576px]:mt-7 min-[576px]:h-[calc(100%-3.5rem)] min-[576px]:max-w-[500px]">
            <div
                class="pointer-events-auto relative flex max-h-[100%] w-full flex-col overflow-hidden rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none dark:bg-neutral-600">
                <div
                    class="flex flex-shrink-0 items-center justify-between rounded-t-md border-b-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
                    <!--Modal title-->
                    <h5 class="text-xl font-medium leading-normal text-neutral-800 dark:text-neutral-200"
                        id="exampleModalScrollableLabel">
                        Solicitar sincronización sobre alguna canción
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
                <div class="relative overflow-y-auto p-4">
                    <div class="relative mb-3">
                        <input type="email"
                            class="peer m-0 block h-[58px] w-full rounded border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-4 text-base font-normal leading-tight text-neutral-700 transition duration-200 ease-linear placeholder:text-transparent focus:border-primary focus:pb-[0.625rem] focus:pt-[1.625rem] focus:text-neutral-700 focus:outline-none peer-focus:text-primary dark:border-neutral-600 dark:text-neutral-200 dark:focus:border-primary dark:peer-focus:text-primary [&:not(:placeholder-shown)]:pb-[0.625rem] [&:not(:placeholder-shown)]:pt-[1.625rem]"
                            id="nombreEmpresa" placeholder="name@example.com" />
                        <label for="floatingInput"
                            class="pointer-events-none absolute left-0 top-0 origin-[0_0] border border-solid border-transparent px-3 py-4 text-neutral-500 transition-[opacity,_transform] duration-200 ease-linear peer-focus:-translate-y-2 peer-focus:translate-x-[0.15rem] peer-focus:scale-[0.85] peer-focus:text-primary peer-[:not(:placeholder-shown)]:-translate-y-2 peer-[:not(:placeholder-shown)]:translate-x-[0.15rem] peer-[:not(:placeholder-shown)]:scale-[0.85] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">Nombre
                            de la empresa</label>
                    </div>
                    <div class="relative mb-3">
                        <input type="email"
                            class="peer m-0 block h-[58px] w-full rounded border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-4 text-base font-normal leading-tight text-neutral-700 transition duration-200 ease-linear placeholder:text-transparent focus:border-primary focus:pb-[0.625rem] focus:pt-[1.625rem] focus:text-neutral-700 focus:outline-none peer-focus:text-primary dark:border-neutral-600 dark:text-neutral-200 dark:focus:border-primary dark:peer-focus:text-primary [&:not(:placeholder-shown)]:pb-[0.625rem] [&:not(:placeholder-shown)]:pt-[1.625rem]"
                            id="nombreContacto" placeholder="name@example.com" />
                        <label for="floatingInput"
                            class="pointer-events-none absolute left-0 top-0 origin-[0_0] border border-solid border-transparent px-3 py-4 text-neutral-500 transition-[opacity,_transform] duration-200 ease-linear peer-focus:-translate-y-2 peer-focus:translate-x-[0.15rem] peer-focus:scale-[0.85] peer-focus:text-primary peer-[:not(:placeholder-shown)]:-translate-y-2 peer-[:not(:placeholder-shown)]:translate-x-[0.15rem] peer-[:not(:placeholder-shown)]:scale-[0.85] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">Nombre
                            de contacto</label>
                    </div>
                    <div class="relative mb-3">
                        <input type="email"
                            class="peer m-0 block h-[58px] w-full rounded border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-4 text-base font-normal leading-tight text-neutral-700 transition duration-200 ease-linear placeholder:text-transparent focus:border-primary focus:pb-[0.625rem] focus:pt-[1.625rem] focus:text-neutral-700 focus:outline-none peer-focus:text-primary dark:border-neutral-600 dark:text-neutral-200 dark:focus:border-primary dark:peer-focus:text-primary [&:not(:placeholder-shown)]:pb-[0.625rem] [&:not(:placeholder-shown)]:pt-[1.625rem]"
                            id="direccionCorreo" placeholder="name@example.com" />
                        <label for="floatingInput"
                            class="pointer-events-none absolute left-0 top-0 origin-[0_0] border border-solid border-transparent px-3 py-4 text-neutral-500 transition-[opacity,_transform] duration-200 ease-linear peer-focus:-translate-y-2 peer-focus:translate-x-[0.15rem] peer-focus:scale-[0.85] peer-focus:text-primary peer-[:not(:placeholder-shown)]:-translate-y-2 peer-[:not(:placeholder-shown)]:translate-x-[0.15rem] peer-[:not(:placeholder-shown)]:scale-[0.85] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">Dirección
                            de correo</label>
                    </div>
                    <div class="relative mb-3">
                        <input type="tel"
                            class="peer m-0 block h-[58px] w-full rounded border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-4 text-base font-normal leading-tight text-neutral-700 transition duration-200 ease-linear placeholder:text-transparent focus:border-primary focus:pb-[0.625rem] focus:pt-[1.625rem] focus:text-neutral-700 focus:outline-none peer-focus:text-primary dark:border-neutral-600 dark:text-neutral-200 dark:focus:border-primary dark:peer-focus:text-primary [&:not(:placeholder-shown)]:pb-[0.625rem] [&:not(:placeholder-shown)]:pt-[1.625rem]"
                            id="numeroTelefono" placeholder="name@example.com" />
                        <label for="floatingInput"
                            class="pointer-events-none absolute left-0 top-0 origin-[0_0] border border-solid border-transparent px-3 py-4 text-neutral-500 transition-[opacity,_transform] duration-200 ease-linear peer-focus:-translate-y-2 peer-focus:translate-x-[0.15rem] peer-focus:scale-[0.85] peer-focus:text-primary peer-[:not(:placeholder-shown)]:-translate-y-2 peer-[:not(:placeholder-shown)]:translate-x-[0.15rem] peer-[:not(:placeholder-shown)]:scale-[0.85] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">Número
                            de teléfono</label>
                    </div>
                    <div class="relative mb-3">
                        <input type="text"
                            class="peer m-0 block h-[58px] w-full rounded border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-4 text-base font-normal leading-tight text-neutral-700 transition duration-200 ease-linear placeholder:text-transparent focus:border-primary focus:pb-[0.625rem] focus:pt-[1.625rem] focus:text-neutral-700 focus:outline-none peer-focus:text-primary dark:border-neutral-600 dark:text-neutral-200 dark:focus:border-primary dark:peer-focus:text-primary [&:not(:placeholder-shown)]:pb-[0.625rem] [&:not(:placeholder-shown)]:pt-[1.625rem]"
                            id="ubicacion" placeholder="name@example.com" />
                        <label for="floatingInput"
                            class="pointer-events-none absolute left-0 top-0 origin-[0_0] border border-solid border-transparent px-3 py-4 text-neutral-500 transition-[opacity,_transform] duration-200 ease-linear peer-focus:-translate-y-2 peer-focus:translate-x-[0.15rem] peer-focus:scale-[0.85] peer-focus:text-primary peer-[:not(:placeholder-shown)]:-translate-y-2 peer-[:not(:placeholder-shown)]:translate-x-[0.15rem] peer-[:not(:placeholder-shown)]:scale-[0.85] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">País/Ubicación</label>
                    </div>
                    <div class="relative mb-3" data-te-input-wrapper-init>
                        <textarea
                            class="peer block min-h-[auto] w-full rounded border bg-transparent px-3 py-[0.32rem] leading-[1.6] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0"
                            id="detallesProyecto" rows="3" placeholder="Your message"></textarea>
                        <label for="exampleFormControlTextarea1"
                            class="pointer-events-none absolute left-3 top-0 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[1.6] text-neutral-500 transition-all duration-200 ease-out peer-focus:-translate-y-[0.9rem] peer-focus:scale-[0.8] peer-focus:text-primary peer-data-[te-input-state-active]:-translate-y-[0.9rem] peer-data-[te-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">Detalles
                            del proyecto</label>
                    </div>
                    <div class="relative mb-3">
                        <input type="number"
                            class="peer m-0 block h-[58px] w-full rounded border border-solid border-neutral-300 bg-transparent bg-clip-padding px-3 py-4 text-base font-normal leading-tight text-neutral-700 transition duration-200 ease-linear placeholder:text-transparent focus:border-primary focus:pb-[0.625rem] focus:pt-[1.625rem] focus:text-neutral-700 focus:outline-none peer-focus:text-primary dark:border-neutral-600 dark:text-neutral-200 dark:focus:border-primary dark:peer-focus:text-primary [&:not(:placeholder-shown)]:pb-[0.625rem] [&:not(:placeholder-shown)]:pt-[1.625rem]"
                            id="presupuestoDisponible" placeholder="name@example.com" />
                        <label for="floatingInput"
                            class="pointer-events-none absolute left-0 top-0 origin-[0_0] border border-solid border-transparent px-3 py-4 text-neutral-500 transition-[opacity,_transform] duration-200 ease-linear peer-focus:-translate-y-2 peer-focus:translate-x-[0.15rem] peer-focus:scale-[0.85] peer-focus:text-primary peer-[:not(:placeholder-shown)]:-translate-y-2 peer-[:not(:placeholder-shown)]:translate-x-[0.15rem] peer-[:not(:placeholder-shown)]:scale-[0.85] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">Presupuesto
                            disponible</label>
                    </div>
                    <div class="relative mb-3" data-te-input-wrapper-init>
                        <textarea
                            class="peer block min-h-[auto] w-full rounded border bg-transparent px-3 py-[0.32rem] leading-[1.6] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0"
                            id="comentariosAdicionales" rows="3" placeholder="Your message"></textarea>
                        <label for="exampleFormControlTextarea1"
                            class="pointer-events-none absolute left-3 top-0 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[1.6] text-neutral-500 transition-all duration-200 ease-out peer-focus:-translate-y-[0.9rem] peer-focus:scale-[0.8] peer-focus:text-primary peer-data-[te-input-state-active]:-translate-y-[0.9rem] peer-data-[te-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary">Comentarios
                            adicionales (opcional)</label>
                    </div>
                </div>


                <!-- Modal footer -->

                <div
                    class="flex items-center justify-between rounded-b-md border-t-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">

                    <div class="flex items-center space-x-4">
                        <button type="button"
                            class="inline-block rounded bg-pink-100 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-primary-700 transition duration-150 ease-in-out hover:bg-primary-accent-100 focus:bg-primary-accent-100 focus:outline-none focus:ring-0 active:bg-primary-accent-200"
                            data-te-modal-dismiss data-te-ripple-init data-te-ripple-color="light">
                            Cerrar
                        </button>

                        <button type="button"
                            class="inline-block rounded bg-pink-500 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(59,113,202,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)]"
                            data-te-modal-dismiss data-te-ripple-init data-te-ripple-color="light"
                            @click="enviarSolicitud()">
                            Enviar
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios';

import {
    Datatable,
    Select,
    initTE,
} from "tw-elements";

initTE({ Datatable });
initTE({ Select });

var filas_dataTable = null;

export default {
    data() {
        return {
            canciones: [],
            isLoggedIn: false,
            accessToken: null,
            generos: [],
            entidades: [],
            filtros: {
                generos: [],
                entidades: [],
            },
        };
    },
    mounted() {
        axios.defaults.headers.common['Authorization'] = null;
        const accessTokenFromURL = window.location.hash.substr(1).split('&')[0].split('=')[1];
        this.showFiltersModal();
        if (accessTokenFromURL) {
            this.accessToken = accessTokenFromURL;
            this.isLoggedIn = true;
            this.getSpotifyEmbedUrl(this.accessToken).then(() => {
                this.fetchCanciones();
            });
        } else {
            this.fetchCanciones();
        }
        const datatable = document.getElementById('datatable');

        datatable.addEventListener('selectRows.te.datatable', (e) => {
            filas_dataTable = e.selectedRows;
        })
    },
    methods: {

        async enviarSolicitud() {
            console.log("Argumentos de la solicitud:");

            const empresa = document.querySelector("#nombreEmpresa").value.trim();
            console.log("NOMBRE DE LA EMPRESA: " + empresa);

            const contacto = document.querySelector("#nombreContacto").value.trim();
            console.log("NOMBRE DE CONTACTO: " + contacto);

            const correo = document.querySelector("#direccionCorreo").value.trim();
            console.log("DIRECCION DE CORREO: " + correo);

            const telefono = document.querySelector("#numeroTelefono").value.trim();
            console.log("NUMERO DE TELEFONO: " + telefono);

            const ubicacion = document.querySelector("#ubicacion").value.trim();
            console.log("UBICACION: " + ubicacion);

            const detalles = document.querySelector("#detallesProyecto").value.trim();
            console.log("DETALLES DEL PROYECTO: " + detalles);

            const presupuesto = document.querySelector("#presupuestoDisponible").value.trim();
            console.log("PRESUPUESTO DISPONIBLE: " + presupuesto);

            const comentarios = document.querySelector("#comentariosAdicionales").value.trim();
            console.log("COMENTARIOS ADICIONALES: " + comentarios);

            console.log(filas_dataTable);

            // Verificar campos obligatorios
            if (!empresa || !contacto || !correo || !telefono || !ubicacion || !detalles || !presupuesto) {
                const alertContainer = document.querySelector("#alertContainer");
                alertContainer.innerHTML = `<div
  class="mb-3 inline-flex w-full items-center rounded-lg bg-danger-100 px-6 py-5 text-base text-danger-700"
  role="alert">
  <span class="mr-2">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      class="h-5 w-5">
      <path
        fill-rule="evenodd"
        d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25zm-1.72 6.97a.75.75 0 10-1.06 1.06L10.94 12l-1.72 1.72a.75.75 0 101.06 1.06L12 13.06l1.72 1.72a.75.75 0 101.06-1.06L13.06 12l1.72-1.72a.75.75 0 10-1.06-1.06L12 10.94l-1.72-1.72z"
        clip-rule="evenodd" />
    </svg>
  </span>
  Hay que completar todos los campos excepto el opcional.
</div>`;

            }

            try {

                const datosSolicitud = {
                    empresa,
                    contacto,
                    correo,
                    telefono,
                    ubicacion,
                    detalles,
                    presupuesto,
                    comentarios
                };

                const response = await axios.post(`http://localhost:8000/api/editorial/solicitudes/`, datosSolicitud);

                console.log('Solicitud enviada:', response.data);


            } catch (error) {
                console.error('Error al modificar la canción:', error);
            }
        },


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

                    const botonEscuchar = `<button class="btn-escuchar animate-fade-in" data-id="${cancion.idSpotify}"></button>`;

                    return {
                        cancion: cancion.nombre,
                        artista: cancion.entidadNombre,
                        genero: cancion.generoNombres.join(', '),
                        duracion: cancion.duracion,
                        escucha: botonEscuchar,
                    };
                }));

                // Actualiza la tabla con los datos filtrados
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

        async getSpotifyEmbedUrl(accessToken) {
            console.log('Access Token:', accessToken);
            await this.$nextTick();
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

                    const botonEscuchar = `<button class="btn-escuchar animate-fade-in" data-id="${cancion.idSpotify}" ></button>`;

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

            const instance = new Datatable(document.getElementById('datatable'), data, {
                hover: true,
            });

            document.getElementById('datatable-search-input').addEventListener('input', (e) => {
                instance.search(e.target.value);
            });
        },

        loginWithSpotify() {
            const clientId = '5ba3471f79a443b49a0135b669294f42';
            const scopes = 'user-read-private user-read-email';
            const redirectUri = 'http://localhost:5173/sincronizacion';

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
    background-image: url('../../public/images/boton-de-play.png');
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
