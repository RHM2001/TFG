<template>
   <div class="px-6 text-center text-white md:px-12">
      <h1 class="m-5 text-5xl font-bold leading-tight text-light">SON BUENOS</h1>
      <h3 class="mb-2 mt-0 text-3xl font-medium leading-tight text-light">
         SonBuenos representa una amplia libreria de música, un catálogo con artistas con denominación de origen en la
         Región de Murcia.
      </h3>
      <h3 class="mb-2 mt-0 text-3xl font-medium leading-tight text-neutral-950">
         ¡Consultanos para conseguir
         esa canción que necesitas!
         De todos los géneros, sensaciones,
         estados de ánimo y a medida.
      </h3>
   </div>
   <div class="container mx-auto px-5 py-2 lg:px-32 lg:pt-12">
      <div id="carouselExampleCaptions" class="relative" data-te-carousel-init data-te-ride="carousel">
         <!--Carousel indicators-->
         <div class="absolute bottom-0 left-0 right-0 z-[2] mx-[15%] mb-4 flex list-none justify-center p-0"
            data-te-carousel-indicators>
            <button type="button" data-te-target="#carouselExampleCaptions" data-te-slide-to="0" data-te-carousel-active
               class="mx-[3px] box-content h-[3px] w-[30px] flex-initial cursor-pointer border-0 border-y-[10px] border-solid border-transparent bg-white bg-clip-padding p-0 -indent-[999px] opacity-50 transition-opacity duration-[600ms] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] motion-reduce:transition-none"
               aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-te-target="#carouselExampleCaptions" data-te-slide-to="1"
               class="mx-[3px] box-content h-[3px] w-[30px] flex-initial cursor-pointer border-0 border-y-[10px] border-solid border-transparent bg-white bg-clip-padding p-0 -indent-[999px] opacity-50 transition-opacity duration-[600ms] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] motion-reduce:transition-none"
               aria-label="Slide 2"></button>
            <button type="button" data-te-target="#carouselExampleCaptions" data-te-slide-to="2"
               class="mx-[3px] box-content h-[3px] w-[30px] flex-initial cursor-pointer border-0 border-y-[10px] border-solid border-transparent bg-white bg-clip-padding p-0 -indent-[999px] opacity-50 transition-opacity duration-[600ms] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] motion-reduce:transition-none"
               aria-label="Slide 3"></button>
         </div>

         <!--Carousel items-->
         <div class="relative w-full overflow-hidden after:clear-both after:block after:content-['']">
            <!--First item-->
            <div
               class="relative float-left -mr-[100%] w-full transition-transform duration-[600ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-active data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://www.sonbuenos.com/wp-content/uploads/2023/06/PORTADA-EP-HOONINE.jpg"
                  class="block w-full object-cover h-[400px]" alt="..." />
               <div class="absolute inset-x-[15%] bottom-5 hidden py-5 text-center text-white md:block">
                  <h5 class="text-xl">Nuevo single de HOONINE</h5>
                  <p>
                     HOONINE presenta “Con todo y con eso”, una canción de pop minimalista, producida por la propia Carmen
                     Alarcón.
                  </p>
               </div>
            </div>
            <!--Second item-->
            <div
               class="relative float-left -mr-[100%] hidden w-full transition-transform duration-[600ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://www.sonbuenos.com/wp-content/uploads/2023/06/CLAIM.jpg"
                  class="block w-full object-cover h-[400px]" alt="..." />
               <div class="absolute inset-x-[15%] bottom-5 hidden py-5 text-center text-white md:block">
                  <h5 class="text-xl">BENGALA</h5>
                  <p>
                     CLAIM PRESENTA EL SEGUNDO ADELANTO DE SU TERCER TRABAJO
                  </p>
               </div>
            </div>
            <!--Third item-->
            <div
               class="relative float-left -mr-[100%] hidden w-full transition-transform duration-[600ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-item style="backface-visibility: hidden">
               <img
                  src="https://es.rollingstone.com/wp-content/uploads/2023/03/Arde-Bogota-presenta-Cowboys-de-la-A3-1024x616.jpg"
                  class="block w-full object-cover h-[400px]" alt="..." />
               <div class="absolute inset-x-[15%] bottom-5 hidden py-5 text-center text-white md:block">
                  <h5 class="text-xl">ARDE BOGOTÁ: DIRECTOS AL #3</h5>
                  <p>
                     Arde Bogotá, la banda rock por excelencia en España
                     Arde Bogotá se consagra como la banda rock del momento
                  </p>
               </div>
            </div>
         </div>

         <!--Carousel controls - prev item-->
         <button
            class="absolute bottom-0 left-0 top-0 z-[1] flex w-[15%] items-center justify-center border-0 bg-none p-0 text-center text-white opacity-50 transition-opacity duration-150 ease-[cubic-bezier(0.25,0.1,0.25,1.0)] hover:text-white hover:no-underline hover:opacity-90 hover:outline-none focus:text-white focus:no-underline focus:opacity-90 focus:outline-none motion-reduce:transition-none"
            type="button" data-te-target="#carouselExampleCaptions" data-te-slide="prev">
            <span class="inline-block h-8 w-8">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                  stroke="currentColor" class="h-6 w-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
               </svg>
            </span>
            <span
               class="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">Previous</span>
         </button>
         <!--Carousel controls - next item-->
         <button
            class="absolute bottom-0 right-0 top-0 z-[1] flex w-[15%] items-center justify-center border-0 bg-none p-0 text-center text-white opacity-50 transition-opacity duration-150 ease-[cubic-bezier(0.25,0.1,0.25,1.0)] hover:text-white hover:no-underline hover:opacity-90 hover:outline-none focus:text-white focus:no-underline focus:opacity-90 focus:outline-none motion-reduce:transition-none"
            type="button" data-te-target="#carouselExampleCaptions" data-te-slide="next">
            <span class="inline-block h-8 w-8">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                  stroke="currentColor" class="h-6 w-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
               </svg>
            </span>
            <span
               class="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">Next</span>
         </button>
      </div>
   </div>
</template>

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
