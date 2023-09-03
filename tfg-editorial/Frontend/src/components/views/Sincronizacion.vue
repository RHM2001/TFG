<template>
    <div class="container mx-auto py-8 lg:pt-8">
        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
            <h5 class="mb-2 text-xl font-medium leading-tight text-black text-center">
                Catálogo con filtros y búsqueda
            </h5>

            <div class="mb-3">
                <div class="relative mb-4 flex w-full flex-wrap items-stretch">
                    <input v-model="searchQuery" type="search"
                        class="relative m-0 -mr-0.5 block w-[1px] min-w-0 flex-auto rounded-l border border-solid border-gray-300 bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-gray-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-gray-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none"
                        placeholder="Buscar" aria-label="Buscar" />
                </div>
            </div>

            <div >
                <table class="min-w-full border border-gray-300 divide-y divide-gray-300">
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
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.generoNombres ? cancion.generoNombres.join(', ') : "" }}</td>
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
