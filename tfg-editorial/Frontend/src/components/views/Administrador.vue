<template>
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
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            user: '',
            password: '',
        };
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