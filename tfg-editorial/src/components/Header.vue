<template>
    <header>
        <!-- Navigation bar -->
        <nav class="relative flex w-full items-center justify-between bg-white py-2 text-neutral-600 shadow-lg hover:text-neutral-700 focus:text-neutral-700 dark:bg-white dark:text-black md:flex-wrap md:justify-start"
            data-te-navbar-ref>
            <div class="flex w-full flex-wrap items-center justify-between px-3">
                <div class="flex items-center">


                    <!-- Hamburger menu button -->
                    <button
                        class="border-0 bg-transparent px-2 text-xl leading-none transition-shadow duration-150 ease-in-out hover:text-neutral-700 focus:text-neutral-700 dark:hover:text-white dark:focus:text-white lg:hidden"
                        type="button" data-te-collapse-init data-te-target="#navbarSupportedContentX"
                        aria-controls="navbarSupportedContentX" aria-expanded="false" aria-label="Toggle navigation">
                        <!-- Hamburger menu icon -->
                        <span class="[&>svg]:w-5">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="h-7 w-7">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                            </svg>
                        </span>
                    </button>
                </div>


                <!-- Navegación -->
                <div class="!visible hidden grow basis-[100%] items-center lg:!flex lg:basis-auto"
                    id="navbarSupportedContentX" data-te-collapse-item>

                    <router-link to="/" class="animate-fade-in mb-4 ml-2 mr-5 mt-3">
                        <img src="https://www.sonbuenos.com/wp-content/uploads/2019/06/logo-sonbuenos-2019-e1559813110801.png"
                            style="max-width: 110px; height: auto;" alt="Logo SonBuenos" />
                    </router-link>

                    <ul class="mr-auto flex flex-col lg:flex-row lg:pl-16 " data-te-navbar-nav-ref>
                        <li class="mb-0 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                            <a class="block transition duration-150 ease-in-out hover:text-neutral-700 focus:text-neutral-700 disabled:text-black/30 dark:hover:text-pink-600  lg:p-2 [&.active]:text-black/90"
                                href="#!" data-te-nav-link-ref data-te-ripple-init
                                data-te-ripple-color="light">Sincronización</a>
                        </li>
                        <li class="mb-0 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                            <router-link to="/artistas"
                                class="block transition duration-150 ease-in-out hover:text-neutral-700 focus:text-neutral-700 disabled:text-black/30 dark:hover:text-pink-600  lg:p-2 [&.active]:text-black/90"
                                data-te-nav-link-ref data-te-ripple-init data-te-ripple-color="light">
                                Artistas & Autores
                            </router-link>
                        </li>

                        <li class="mb-0 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                            <a class="block transition duration-150 ease-in-out hover:text-neutral-700 focus:text-neutral-700 disabled:text-black/30 dark:hover:text-pink-600  lg:p-2 [&.active]:text-black/90"
                                href="#!" data-te-nav-link-ref data-te-ripple-init
                                data-te-ripple-color="light">Merchandising</a>
                        </li>
                        <li class="mb-0 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                            <a class="block transition duration-150 ease-in-out hover:text-neutral-700 focus:text-neutral-700 disabled:text-black/30 dark:hover:text-pink-600  lg:p-2 [&.active]:text-black/90"
                                href="#!" data-te-nav-link-ref data-te-ripple-init
                                data-te-ripple-color="light">Conciertos</a>
                        </li>
                        <li class="mb-0 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                            <a class="block transition duration-150 ease-in-out hover:text-neutral-700 focus:text-neutral-700 disabled:text-black/30 dark:hover:text-pink-600  lg:p-2 [&.active]:text-black/90"
                                href="#!" data-te-nav-link-ref data-te-ripple-init
                                data-te-ripple-color="light">Administrador </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>


    </header>
</template>

<style>
.animate-fade-in:hover {
    transform: scale(1.02);
}
</style>

<script>
// Initialization for ES Users
import {
    Collapse,
    Dropdown,
    initTE,
} from "tw-elements";

initTE({ Collapse, Dropdown });

</script>