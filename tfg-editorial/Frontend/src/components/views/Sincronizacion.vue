<template>
    <div class="container mx-auto py-8 lg:pt-8">
        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
            <h5 class="mb-2 text-xl font-medium leading-tight text-black text-center">
                Catálogo con filtros y búsqueda
            </h5>

            <div data-te-datatable-init>
                <table class=" min-w-full border border-gray-300 divide-y divide-gray-300">
                    <thead class="bg-gray-50">
                        <tr>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Nombre
                            </th>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Editorial
                            </th>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Género
                            </th>
                            <th scope="col"
                                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Duración
                            </th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-300">
                        <tr v-for="(cancion, index) in canciones" :key="index">
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.nombre }}</td>
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.entidadNombre }}</td>
                            <td class="px-6 py-4 whitespace-nowrap">{{ cancion.genero }}</td>
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
            fields: [
                { key: 'nombre', label: 'Nombre' },
                { key: 'entidad', label: 'Entidad' }
            ],
            canciones: []
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
        }

    }
};

</script>
