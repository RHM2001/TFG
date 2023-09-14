<template>
    <div class="container mx-auto py-8 lg:pt-8">


        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
            <h5 class="mb-2 text-xl font-medium leading-tight text-black text-center">
                Catálogo con filtros y búsqueda
            </h5>



            <div class="relative mb-3 fade-in collapse-container">

                <div class="mb-3 ">
                    <div class="relative mb-4 flex w-full flex-wrap items-stretch">
                        <input v-model="searchQuery" type="search"
                            class="relative m-0 -mr-0.5 block w-[1px] min-w-0 flex-auto rounded-l border border-solid border-gray-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-gray-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-gray-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none"
                            placeholder="Buscar" aria-label="Buscar" />
                    </div>
                </div>

                <div data-te-dropdown-ref>
                    <button
                        class="flex items-center whitespace-nowrap rounded bg-secondary px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-secondary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-secondary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-secondary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] motion-reduce:transition-none dark:shadow-[0_4px_9px_-4px_rgba(59,113,202,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)]"
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
                    </button>
                    <ul class="absolute z-[1000] float-left m-0 hidden min-w-max list-none overflow-hidden rounded-lg
                        border-none bg-white bg-clip-padding text-left text-base shadow-lg dark:bg-neutral-700
                        [&[data-te-dropdown-show]]:block" aria-labelledby="dropdownMenuButton1"
                        data-te-dropdown-menu-ref>
                        <li>
                            <a class="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-neutral-600"
                                href="#" data-te-dropdown-item-ref>Género</a>
                        </li>
                        <li>
                            <a class="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-neutral-600"
                                href="#" data-te-dropdown-item-ref>Duración</a>
                        </li>
                    </ul>
                </div>
            </div>

            <div>
                <table class="min-w-full border border-gray-300 divide-y divide-gray-300 fade-in">
                    <thead class="bg-gray-50">
                        <tr>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer"
                                @click="sortBy('nombre')">Nombre</th>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer"
                                @click="sortBy('entidadNombre')">Entidad</th>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer"
                                @click="sortBy('generoNombres')">Género</th>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer"
                                @click="sortBy('duracion')">Duración</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-300">
                        <tr v-for="(cancion, index) in sortedAndFilteredCanciones" :key="index">
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.nombre }}</td>
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.entidadNombre }}</td>
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.generoNombres ?
                                cancion.generoNombres.join(',') : "" }}</td>
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.duracion }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

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
                this.canciones = response.data;

                // Para cada canción, obtén el nombre de la entidad a través de otra solicitud
                for (const cancion of this.canciones) {
                    await this.fetchEntidadName(cancion);
                    await this.fetchGeneroNames(cancion);
                }

                console.log(response.data); // Mover el console.log aquí
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
        sortBy(key) {
            if (this.sortKey === key) {
                this.sortOrder *= -1;
            } else {
                this.sortKey = key;
                this.sortOrder = 1;
            }
        },



        performSearch() {
            // Filtra las canciones en función de la searchQuery
            this.filteredCanciones = this.canciones.filter(cancion =>
                cancion.nombre.toLowerCase().includes(this.searchQuery.toLowerCase())
                || cancion.entidadNombre.toLowerCase().includes(this.searchQuery.toLowerCase())
                || (cancion.generoNombres && cancion.generoNombres.join(', ').toLowerCase().includes(this.searchQuery.toLowerCase()))
            );
        },

    },
    computed: {
        sortedAndFilteredCanciones() {
            let filteredCanciones = this.canciones;

            if (this.searchQuery) {
                filteredCanciones = this.canciones.filter(cancion =>
                    cancion.nombre.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                    cancion.entidadNombre.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                    (cancion.generoNombres && cancion.generoNombres.join(', ').toLowerCase().includes(this.searchQuery.toLowerCase()))
                );
            }

            if (this.sortKey) {
                const sorted = filteredCanciones.slice().sort((a, b) => {
                    const valA = a[this.sortKey];
                    const valB = b[this.sortKey];
                    if (valA === valB) return 0;
                    return this.sortOrder * (valA > valB ? 1 : -1);
                });
                return sorted;
            }

            return filteredCanciones;
        },
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
</style>
