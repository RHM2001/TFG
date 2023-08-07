import './style.css';
import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHashHistory } from 'vue-router';

import Index from './components/views/Index.vue';
import Artistas from './components/views/Artistas.vue';


const routes = [
    { path: '/', name: 'index', component: Index },
    { path: '/artistas', name: 'artistas', component: Artistas },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

const app = createApp(App);

// Instala el enrutador creado previamente usando createRouter
app.use(router);

app.mount('#app');
