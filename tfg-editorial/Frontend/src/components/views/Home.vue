<template>
   <div class="carousel-container ">
      <div id="carouselExampleCaptions" class="relative" data-te-carousel-init data-te-ride="carousel">


         <!--Carousel items-->
         <div class="relative w-full overflow-hidden after:clear-both after:block after:content-['']">
            <!--First item-->
            <div
               class="relative float-left -mr-[100%] w-full transition-transform duration-[400ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-active data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://www.sonbuenos.com/wp-content/uploads/2023/06/PORTADA-EP-HOONINE.jpg"
                  class="block w-full object-cover h-[1000px]" alt="..." />

            </div>
            <!--Second item-->
            <div
               class="relative float-left -mr-[100%] hidden w-full transition-transform duration-[400ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://verdaderalocura.com/wp-content/uploads/2019/09/NUNATAK-PPAL-750x430.jpg"
                  class="block w-full object-cover h-[1000px]" alt="..." />

            </div>
            <!--Third item-->
            <div
               class="relative float-left -mr-[100%] hidden w-full transition-transform duration-[400ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://s1.lanzadigital.com/wp-content/uploads/2022/05/Arde_Bogota_Zahora_Magestic_CD_4.jpg"
                  class="block w-full object-cover h-[1000px]" alt="..." />

            </div>
         </div>


      </div>
   </div>

   <div class="text-overlay fade-in">
      <p class="font-lara" style="font-size: 30px; color: white;">Representamos una amplia librería
         de música, un catálogo con artistas con denominación de origen en la
         Región de Murcia.</p>

      <p class="font-lara mt-8" style="font-size: 30px; color: white;">
         ¡Consultanos para conseguir
         esa canción que necesitas!
         De todos los géneros, sensaciones,
         estados de ánimo y a medida.
      </p>
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

<style scoped>
.carousel-container {
   position: relative;
   width: 100%;
}

.text-overlay {
   position: absolute;
   top: 125pt;
   left: 100pt;
   width: 400px;
   margin: 0 auto;
   text-align: justify;
}

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