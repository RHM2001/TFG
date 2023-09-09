<template>
    <h1 class="mt-6 text-white text-center">
        Escudería de artistas
    </h1>

    <div class="container mx-auto px-5 py-12 lg:px-32 lg:pt-12">
        <div class="-m-1 flex flex-wrap justify-center md:-m-2">



            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg"
                        src="https://www.sonbuenos.com/wp-content/uploads/2023/04/arde-bogota-lowres.jpg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        Arde Bogotá
                    </p>
                </div>
            </div>

            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg" src="https://www.sonbuenos.com/wp-content/uploads/2022/03/hooninesb.jpg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        Hoonine
                    </p>
                </div>
            </div>

            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg" src="https://www.sonbuenos.com/wp-content/uploads/2023/04/franvvi.jpeg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        Franvi
                    </p>
                </div>
            </div>

            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg" src="https://www.sonbuenos.com/wp-content/uploads/2020/04/nunatakweb.jpg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        Nunatak
                    </p>
                </div>
            </div>

            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg" src="https://www.sonbuenos.com/wp-content/uploads/2023/04/04-1.jpg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        María de Juan
                    </p>
                </div>
            </div>

            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg" src="https://www.sonbuenos.com/wp-content/uploads/2023/04/Bengala-4-2.jpg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        Claim
                    </p>
                </div>
            </div>

            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg" src="https://www.sonbuenos.com/wp-content/uploads/2022/03/carmesiwebsb.jpg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        Carmesí
                    </p>
                </div>
            </div>

            <div
                class="block-artistas max-w-[18rem] rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-white animate-fade-in">
                <div class="relative overflow-hidden bg-cover bg-no-repeat">
                    <img class="rounded-t-lg"
                        src="https://www.sonbuenos.com/wp-content/uploads/2023/04/foto-sephun-lowres.jpeg"
                        alt="Foto Arde Bogota" />
                </div>
                <div class="p-2">
                    <p class="text-center text-pink-800">
                        Se ha perdidio un niño
                    </p>
                </div>
            </div>


        </div>
    </div>
</template>

<style>
.block-artistas {
    margin-bottom: 20px;
    margin-right: 20px;
    transition: transform 0.2s ease-in-out;

}

.block-artistas img {
    width: 225px;
    height: 225px;
    transition: opacity 0.2s ease-in-out;
    opacity: 0.9;
}

.block-artistas:hover {
    transform: scale(1.05);
}

.block-artistas:hover img {
    opacity: 1;
}
</style>

<script>

export default {

    mounted() {
        const script = document.createElement("script");
        script.type = "text/javascript";
        script.src = "../node_modules/tw-elements/dist/js/tw-elements.umd.min.js";
        document.body.appendChild(script);
    }
}
</script>