<template>
   <div class="carousel-container ">
      <div id="carouselExampleCaptions" class="relative" data-te-carousel-init data-te-ride="carousel">


         <!--Carousel items-->
         <div class="relative w-full overflow-hidden after:clear-both after:block after:content-['']">
            <!--First item-->
            <div
               class="relative float-left -mr-[100%] w-full transition-transform duration-[800ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-active data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://www.sonbuenos.com/wp-content/uploads/2023/06/PORTADA-EP-HOONINE.jpg"
                  class="block w-full object-cover h-[1000px]" alt="..." />

            </div>
            <!--Second item-->
            <div
               class="relative float-left -mr-[100%] hidden w-full transition-transform duration-[800ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://www.somosclaim.com/wp-content/uploads/2021/06/IMG_9707-Editar-2-1.jpg"
                  class="block w-full object-cover h-[1000px]" alt="..." />

            </div>
            <!--Third item-->
            <div
               class="relative float-left -mr-[100%] hidden w-full transition-transform duration-[800ms] ease-in-out motion-reduce:transition-none"
               data-te-carousel-item style="backface-visibility: hidden">
               <img src="https://s1.lanzadigital.com/wp-content/uploads/2022/05/Arde_Bogota_Zahora_Magestic_CD_4.jpg"
                  class="block w-full object-cover h-[1000px]" alt="..." />

            </div>
         </div>


      </div>
   </div>

   <div class="text-overlay fade-in">
      <p class="font-lara" style="font-size: 40px; color: white;">Representamos una amplia librería
         de música, un catálogo con artistas con denominación de origen en la
         Región de Murcia.</p>

      <p class="font-lara mt-8" style="font-size: 40px; color: white;">
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
   height: 100vh;

}

body {
   font-family: 'Roboto', sans-serif;
   margin: 0;
   padding: 0;
   overflow-x: hidden;
}

.text-overlay {
   position: absolute;
   top: 125pt;
   left: 200pt;
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