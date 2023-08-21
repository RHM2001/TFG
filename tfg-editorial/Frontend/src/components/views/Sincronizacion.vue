<template>
    <div class="container mx-auto py-8 lg:pt-8">
        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
            <h5 class="mb-2 text-xl font-medium leading-tight text-black text-center">
                Catalogo con filtros y busqueda
            </h5>

            <div data-te-datatable-init>
                <table striped hover :items="canciones" :fields="fields">

                </table>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            fields: [
                { key: 'nombre', label: 'Nombre' },
                { key: 'entidad', label: "Entidad" }
            ],
            canciones: []
        }
    }
}

</script>