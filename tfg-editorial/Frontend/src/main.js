import './style.css';
import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

import Home from './components/views/Home.vue';
import Artistas from './components/views/Artistas.vue';
import Sincronizacion from './components/views/Sincronizacion.vue';
import Administrador from './components/views/Administrador.vue';

const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/artistas', name: 'artistas', component: Artistas },
    { path: '/sincronizacion', name: 'sincronizacion', component: Sincronizacion },
    { path: '/Administrador', name: 'Administrador', component: Administrador },
];

const router = createRouter({
    history: createWebHistory(), // Cambiado a createWebHistory()
    routes,
});

const app = createApp(App);

// Instala el enrutador creado previamente usando createRouter
app.use(router);

app.mount('#app');
