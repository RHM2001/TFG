<template>
    <div v-if="!loggedIn">
        <div class="flex flex-col items-center justify-center mt-24 px-6 py-8 mx-auto">
            <div
                class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">

                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">

                    <a class="flex items-center mb-6 justify-center">
                        <img class="w-100 h-10 mr-2" src="public/images/logo-sonbuenos.png" alt="logo">
                    </a>

                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                        Inicio de sesión confidencial
                    </h1>
                    <form class="space-y-4 md:space-y-6" action="#">
                        <div>
                            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Nombre de
                                usuario</label>
                            <input type="text" name="user" id="user"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                placeholder="Usuario" required>
                        </div>
                        <div>
                            <label for="password"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Contraseña</label>
                            <input type="password" name="password" id="password" placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                required>
                        </div>

                        <button @click.prevent="login" type="button"
                            class="w-full text-white bg-pink-600 hover:bg-pink-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Iniciar
                            Sesion</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <div v-else>

        <div class="container mx-auto px-5 py-12 lg:px-32 lg:pt-12">


            <h1 class="mb-6 text-4xl font-medium leading-tight text-black text-center font-lara">
                Panel de administración
            </h1>


            <div class="flex flex-wrap justify-center">

                <div class="flex justify-between">
                    <!-- Parte Izquierda -->
                    <div class="w-1/3">
                        <div
                            class="flex flex-wrap items-center justify-center block-edit border border-neutral-300 rounded-lg max-w-[18rem] bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 animate-fade-in">

                            <div class="flex items-center justify-center mt-6">
                                <img class="rounded-t-lg" src="public/images/disco-de-vinilo.png" />
                            </div>
                            <div class="p-6">
                                <h5 class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
                                    Generos
                                </h5>
                                <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
                                    Generos introducidos en la base de datos del sistema.
                                </p>
                            </div>
                        </div>

                        <div
                            class="flex flex-wrap items-center justify-center block-edit border border-neutral-300 rounded-lg max-w-[18rem] bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 animate-fade-in">
                            <div class="flex items-center justify-center mt-6">
                                <img class="rounded-t-lg" src="public/images/lista-de-musica.png" />
                            </div>
                            <div class="p-6">
                                <h5 class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
                                    Canciones
                                </h5>
                                <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
                                    Canciones guardadas en la base de datos del sistema.
                                </p>
                            </div>
                        </div>

                    </div>

                    <!-- Parte Centro -->
                    <div class="w-1/3 flex items-center">
                        <div
                            class="flex flex-wrap items-center justify-center block-edit border border-neutral-300 rounded-lg max-w-[18rem]  bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 animate-fade-in    ">
                            <div class="flex items-center justify-center mt-6">
                                <img class="rounded-t-lg" src="public/images/sobre.png" />
                            </div>
                            <div class="p-6">
                                <h5 class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
                                    Solicitudes de sincronización
                                </h5>
                                <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
                                    Gestionar solicitudes de sincronización recibidas.
                                </p>
                            </div>
                        </div>
                    </div>



                    <!-- Parte Derecha -->
                    <div class="w-1/3">
                        <div
                            class="flex flex-wrap items-center justify-center block-edit border border-neutral-300 rounded-lg max-w-[18rem]  bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 animate-fade-in">
                            <div class="flex items-center justify-center mt-6">
                                <img class="rounded-t-lg" src="public/images/entidades.png" />
                            </div>
                            <div class="p-6">
                                <h5 class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
                                    Entidades musicales
                                </h5>
                                <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
                                    Entidades musicales en la base de datos del sistema.
                                </p>
                            </div>
                        </div>

                        <div
                            class="flex flex-wrap items-center justify-center block-edit border border-neutral-300 rounded-lg max-w-[18rem] bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 animate-fade-in">
                            <div class="flex items-center justify-center mt-6">
                                <img class="rounded-t-lg" src="public/images/musica-de-usuario.png" />
                            </div>
                            <div class="p-6">
                                <h5 class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
                                    Artistas
                                </h5>
                                <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
                                    Artistas de la base de datos del sistema.
                                </p>
                            </div>
                        </div>

                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            loggedIn: false,
            username: '',
        };
    },
    mounted() {
        const storedToken = localStorage.getItem('access_token');
        if (storedToken) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${storedToken}`;
            this.loggedIn = true;

        }
    },
    methods: {
        async login() {
            try {
                const username = document.querySelector("#user").value.trim();
                console.log("Usuario: " + username);
                const password = document.querySelector("#password").value.trim();
                console.log("Contraseña: " + password);

                const formData = new FormData();
                formData.append('username', username);
                formData.append('password', password);

                const response = await axios.post('http://localhost:8000/api/editorial/login/', formData);

                console.log('Respuesta del servidor:', response);

                if (response.data.detail) {
                    console.log("Inicio de sesión correcto");

                    // Almacena los tokens en el localStorage
                    localStorage.setItem('access_token', response.data.access_token);
                    localStorage.setItem('refresh_token', response.data.refresh_token);

                    this.loggedIn = true;
                    this.username = username;

                } else {
                    console.error('Error al iniciar sesión:', response.data.message);
                }
            } catch (error) {
                console.error('Error al iniciar sesión (catch):', error);

                // Agrega esto para ver el contenido completo del objeto error.response
                console.log('Respuesta de error del servidor:', error.response);

                // También puedes imprimir información específica del error, por ejemplo:
                if (error.response) {
                    console.log('Respuesta del servidor:', error.response.data);
                    console.log('Código de estado HTTP:', error.response.status);
                } else if (error.request) {
                    console.log('No se recibió respuesta del servidor');
                } else {
                    console.log('Error de configuración de la solicitud:', error.message);
                }
            }
        },
    },
};
</script>

<style>
.block-edit {
    margin-bottom: 20px;
    margin-right: 20px;
    transition: transform 0.2s ease-in-out;
}
</style>