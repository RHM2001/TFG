<template>
    <h1 class="text-4xl font-medium leading-tight text-black text-center font-lara mt-6">
        Gestión de solicitudes
    </h1>

    <div class="container mx-auto py-8 lg:pt-8 fade-in">

        <div
            class="block rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">


            <div>
                <div id="datatable-noTratado"></div>
            </div>


            <button type="button" data-te-target="#modalSolicitudesTratado" data-te-toggle="modal"
                class="inline-block rounded bg-info px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#54b4d3] transition duration-150 ease-in-out hover:bg-info-600 hover:shadow-[0_8px_9px_-4px_rgba(84,180,211,0.3),0_4px_18px_0_rgba(84,180,211,0.2)] focus:bg-info-600 focus:shadow-[0_8px_9px_-4px_rgba(84,180,211,0.3),0_4px_18px_0_rgba(84,180,211,0.2)] focus:outline-none focus:ring-0 active:bg-info-700 active:shadow-[0_8px_9px_-4px_rgba(84,180,211,0.3),0_4px_18px_0_rgba(84,180,211,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(84,180,211,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(84,180,211,0.2),0_4px_18px_0_rgba(84,180,211,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(84,180,211,0.2),0_4px_18px_0_rgba(84,180,211,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(84,180,211,0.2),0_4px_18px_0_rgba(84,180,211,0.1)]">
                Ver solicitudes tratadas
            </button>

        </div>
    </div>

    <!--Modal para ver la solicitud-->
    <div data-te-modal-init
        class="fixed left-0 top-0 z-[1055] hidden h-full w-full overflow-y-auto overflow-x-hidden outline-none"
        id="modalSolicitudesTratado" tabindex="-1" aria-labelledby="exampleModalCenterTitle" aria-modal="true"
        role="dialog">
        <div data-te-modal-dialog-ref
            class="pointer-events-none relative flex min-h-[calc(100%-1rem)] w-auto translate-y-[-50px] items-center opacity-0 transition-all duration-300 ease-in-out min-[576px]:mx-auto min-[576px]:mt-7 min-[576px]:min-h-[calc(100%-3.5rem)] min-[576px]:max-w-[1500px]">
            <div
                class="pointer-events-auto relative flex w-full flex-col rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none dark:bg-neutral-600">
                <div
                    class="flex flex-shrink-0 items-center justify-between rounded-t-md border-b-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
                    <!--Modal title-->
                    <h5 class="text-xl font-medium leading-normal text-neutral-800 dark:text-neutral-200"
                        id="exampleModalCenterTitle">
                        Solicitud
                    </h5>
                    <!--Close button-->
                    <button type="button"
                        class="box-content rounded-none border-none hover:no-underline hover:opacity-75 focus:opacity-100 focus:shadow-none focus:outline-none"
                        data-te-modal-dismiss aria-label="Close">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="h-6 w-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!--Modal body-->
                <div>
                    <div id="datatable-tratado"></div>
                </div>

                <!--Modal footer-->
                <div
                    class="flex flex-shrink-0 flex-wrap items-center justify-end rounded-b-md border-t-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">

                    <button type="button"
                        class="inline-block rounded bg-primary-100 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-primary-700 transition duration-150 ease-in-out hover:bg-primary-accent-100 focus:bg-primary-accent-100 focus:outline-none focus:ring-0 active:bg-primary-accent-200"
                        data-te-modal-dismiss data-te-ripple-init data-te-ripple-color="light">
                        Cerrar
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!--Modal para ver la solicitud-->
    <div data-te-modal-init
        class="fixed left-0 top-0 z-[1055] hidden h-full w-full overflow-y-auto overflow-x-hidden outline-none"
        id="modalInfoNoTratado" tabindex="-1" aria-labelledby="exampleModalCenterTitle" aria-modal="true" role="dialog">
        <div data-te-modal-dialog-ref
            class="pointer-events-none relative flex min-h-[calc(100%-1rem)] w-auto translate-y-[-50px] items-center opacity-0 transition-all duration-300 ease-in-out min-[576px]:mx-auto min-[576px]:mt-7 min-[576px]:min-h-[calc(100%-3.5rem)] min-[576px]:max-w-[700px]">
            <div
                class="pointer-events-auto relative flex w-full flex-col rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none dark:bg-neutral-600">
                <div
                    class="flex flex-shrink-0 items-center justify-between rounded-t-md border-b-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
                    <!--Modal title-->
                    <h5 class="text-xl font-medium leading-normal text-neutral-800 dark:text-neutral-200"
                        id="exampleModalCenterTitle">
                        Solicitud
                    </h5>
                    <!--Close button-->
                    <button type="button"
                        class="box-content rounded-none border-none hover:no-underline hover:opacity-75 focus:opacity-100 focus:shadow-none focus:outline-none"
                        data-te-modal-dismiss aria-label="Close">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="h-6 w-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!--Modal body-->
                <div class="relative p-4 flex flex-wrap">

                    <div class="w-1/2 p-4 flex flex-wrap justify-center">
                        <!-- Contenido izquierda -->
                        <div class="relative mb-4 ">
                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Empresa:</strong> {{
                                        solicitudNoTratadoModal.empresa }}
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Contacto:</strong> {{
                                        solicitudNoTratadoModal.contacto }}
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Correo:</strong> {{
                                        solicitudNoTratadoModal.correo }}
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Telefono:</strong> {{
                                        solicitudNoTratadoModal.telefono }}
                                </span>
                            </div>

                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Ubicación:</strong> {{
                                        solicitudNoTratadoModal.ubicacion }}
                                </span>
                            </div>

                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Presupuesto:</strong> {{
                                        solicitudNoTratadoModal.presupuesto }} €
                                </span>
                            </div>
                        </div>

                    </div>

                    <div class="w-1/2 p-4 lex flex-wrap justify-center">
                        <div class="relative mb-4 ">
                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Detalles:</strong>
                                    <span style="word-wrap: break-word; overflow-wrap: break-word; white-space: pre-line;">
                                        {{ solicitudNoTratadoModal.detalles }}
                                    </span>
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Comentarios:</strong> {{
                                        solicitudNoTratadoModal.comentarios ?? 'Sin comentarios' }}
                                </span>
                            </div>

                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Canciones:</strong>
                                    <span style="word-wrap: break-word; overflow-wrap: break-word; white-space: pre-line;">
                                        <template
                                            v-if="solicitudNoTratadoModal.canciones && solicitudNoTratadoModal.canciones.length > 0">
                                            <template v-for="(cancion, index) in solicitudNoTratadoModal.canciones">
                                                {{ index > 0 ? ', ' : '' }}{{ cancion.nombre }} de {{ cancion.entidadNombre
                                                }}
                                            </template>
                                        </template>
                                        <template v-else>
                                            Sin canciones
                                        </template>
                                    </span>
                                </span>


                            </div>
                        </div>
                    </div>


                </div>

                <!--Modal footer-->
                <div
                    class="flex flex-shrink-0 flex-wrap items-center justify-end rounded-b-md border-t-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">

                    <button type="button" @click="eliminarSolicitud"
                        class="inline-block rounded bg-danger px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#dc4c64] transition duration-150 ease-in-out hover:bg-danger-600 hover:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.3),0_4px_18px_0_rgba(220,76,100,0.2)] focus:bg-danger-600 focus:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.3),0_4px_18px_0_rgba(220,76,100,0.2)] focus:outline-none focus:ring-0 active:bg-danger-700 active:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.3),0_4px_18px_0_rgba(220,76,100,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(220,76,100,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.2),0_4px_18px_0_rgba(220,76,100,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.2),0_4px_18px_0_rgba(220,76,100,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.2),0_4px_18px_0_rgba(220,76,100,0.1)]"
                        data-te-ripple-init data-te-ripple-color="light">
                        Cancelar solicitud
                    </button>

                    <button type="button" @click="aceptarSolicitud"
                        class="ml-1 inline-block rounded bg-success px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(59,113,202,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)]"
                        data-te-ripple-init data-te-ripple-color="light">
                        Aceptar solicitud
                    </button>

                </div>
            </div>
        </div>
    </div>

    <!--Modal para ver la solicitud ya tratada-->
    <div data-te-modal-init
        class="fixed left-0 top-0 z-[1055] hidden h-full w-full overflow-y-auto overflow-x-hidden outline-none"
        id="modalInfoTratado" tabindex="-1" aria-labelledby="exampleModalCenterTitle" aria-modal="true" role="dialog">
        <div data-te-modal-dialog-ref
            class="pointer-events-none relative flex min-h-[calc(100%-1rem)] w-auto translate-y-[-50px] items-center opacity-0 transition-all duration-300 ease-in-out min-[576px]:mx-auto min-[576px]:mt-7 min-[576px]:min-h-[calc(100%-3.5rem)] min-[576px]:max-w-[700px]">
            <div
                class="pointer-events-auto relative flex w-full flex-col rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none dark:bg-neutral-600">
                <div
                    class="flex flex-shrink-0 items-center justify-between rounded-t-md border-b-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">
                    <!--Modal title-->
                    <h5 class="text-xl font-medium leading-normal text-neutral-800 dark:text-neutral-200"
                        id="exampleModalCenterTitle">
                        Solicitud tratada
                    </h5>
                    <!--Close button-->
                    <button type="button"
                        class="box-content rounded-none border-none hover:no-underline hover:opacity-75 focus:opacity-100 focus:shadow-none focus:outline-none"
                        data-te-modal-dismiss aria-label="Close">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="h-6 w-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <!--Modal body-->
                <div class="relative p-4 flex flex-wrap">

                    <div class="w-1/2 p-4 flex flex-wrap justify-center">
                        <!-- Contenido izquierda -->
                        <div class="relative mb-4 ">
                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Empresa:</strong> {{
                                        solicitudNoTratadoModal.empresa }}
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Contacto:</strong> {{
                                        solicitudNoTratadoModal.contacto }}
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Correo:</strong> {{
                                        solicitudNoTratadoModal.correo }}
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Telefono:</strong> {{
                                        solicitudNoTratadoModal.telefono }}
                                </span>
                            </div>

                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Ubicación:</strong> {{
                                        solicitudNoTratadoModal.ubicacion }}
                                </span>
                            </div>

                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Presupuesto:</strong> {{
                                        solicitudNoTratadoModal.presupuesto }} €
                                </span>
                            </div>
                        </div>

                    </div>

                    <div class="w-1/2 p-4 lex flex-wrap justify-center">
                        <div class="relative mb-4 ">
                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Detalles:</strong>
                                    <span style="word-wrap: break-word; overflow-wrap: break-word; white-space: pre-line;">
                                        {{ solicitudNoTratadoModal.detalles }}
                                    </span>
                                </span>
                            </div>


                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Comentarios:</strong> {{
                                        solicitudNoTratadoModal.comentarios ?? 'Sin comentarios' }}
                                </span>
                            </div>

                            <div class="relative mb-4 flex">
                                <span
                                    class="flex items-center whitespace-nowrap rounded border border-solid border-neutral-300 px-3 py-[0.25rem] text-center text-base font-normal leading-[1.6] text-neutral dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200"
                                    id="inputGroup-sizing-default">
                                    <strong style="font-weight: bold; margin-right: 0.5rem;">Canciones:</strong>
                                    <span style="word-wrap: break-word; overflow-wrap: break-word; white-space: pre-line;">
                                        <template
                                            v-if="solicitudNoTratadoModal.canciones && solicitudNoTratadoModal.canciones.length > 0">
                                            <template v-for="(cancion, index) in solicitudNoTratadoModal.canciones">
                                                {{ index > 0 ? ', ' : '' }}{{ cancion.nombre }} de {{ cancion.entidadNombre
                                                }}
                                            </template>
                                        </template>
                                        <template v-else>
                                            Sin canciones
                                        </template>
                                    </span>
                                </span>


                            </div>
                        </div>
                    </div>


                </div>

                <!--Modal footer-->
                <div
                    class="flex flex-shrink-0 flex-wrap items-center justify-end rounded-b-md border-t-2 border-neutral-100 border-opacity-100 p-4 dark:border-opacity-50">

                    <button type="button"
                        class="inline-block rounded bg-primary-100 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-primary-700 transition duration-150 ease-in-out hover:bg-primary-accent-100 focus:bg-primary-accent-100 focus:outline-none focus:ring-0 active:bg-primary-accent-200"
                        data-te-modal-dismiss data-te-ripple-init data-te-ripple-color="light">
                        Cerrar
                    </button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import {
    Datatable,
    Select,
    initTE
} from "tw-elements";

initTE({ Select });

export default {
    data() {
        return {
            solicitudNoTratadoModal: {
                id: '',
                empresa: '',
                contacto: '',
                correo: '',
                telefono: '',
                ubicacion: '',
                detalles: '',
                presupuesto: '',
                comentarios: '',
                canciones: [],
            },
        };
    },
    mounted() {
        this.fetchNoTratado();
        this.fetchTratado();
    },
    methods: {

        async fetchTratado() {
            try {
                const response = await axios.get('http://localhost:8000/api/editorial/solicitudes/');

                // Filtrar las solicitudes no tratadas
                const solicitudesNoTratadas = response.data.filter(solicitud => solicitud.tratado);

                const canciones = await Promise.all(solicitudesNoTratadas.map(async (solicitud) => {
                    const botonInfo = `<button class="btn-info" data-te-toggle="modal" data-te-target="#modalInfoTratado" data-id="${solicitud.id}"></button>`;

                    return {
                        id: solicitud.id,
                        empresa: solicitud.empresa,
                        contacto: solicitud.contacto,
                        correo: solicitud.correo,
                        telefono: solicitud.telefono,
                        ubicacion: solicitud.ubicacion,
                        detalles: solicitud.detalles,
                        presupuesto: solicitud.presupuesto + " €",
                        comentarios: solicitud.comentarios,
                        tratado: solicitud.tratado,
                        canciones: solicitud.canciones,
                        info: botonInfo
                    };
                }));

                const columns = [
                    { label: "Id", field: "id" },
                    { label: "Empresa", field: "empresa" },
                    { label: "Contacto", field: "contacto" },
                    { label: "Correo", field: "correo" },
                    { label: "Ubicacion", field: "ubicacion" },
                    { label: "Detalles", field: "detalles" },
                    { label: "Presupuesto", field: "presupuesto" },
                    { label: "Info", field: "info", sort: false },
                ];

                const data = {
                    columns,
                    rows: canciones,
                };

                this.initDataTableTratado(data);

                const tableContainer = document.getElementById('datatable-tratado');
                tableContainer.addEventListener('click', (event) => {
                    const target = event.target;
                    if (target.classList.contains('btn-info')) {
                        const idSolicitud = target.getAttribute('data-id');
                        this.cambiarInfoNoTratadoModal(idSolicitud);
                    }
                });

            } catch (error) {
                console.error('Error fetching solicitudes:', error);
            }
        },

        initDataTableTratado(data) {

            const tableElement = document.getElementById('datatable-tratado');
            tableElement.innerHTML = '';

            const instance = new Datatable(document.getElementById('datatable-tratado'), data, {
                hover: true,
            });
        },

        async fetchNoTratado() {
            try {
                const response = await axios.get('http://localhost:8000/api/editorial/solicitudes/');

                // Filtrar las solicitudes no tratadas
                const solicitudesNoTratadas = response.data.filter(solicitud => !solicitud.tratado);

                const canciones = await Promise.all(solicitudesNoTratadas.map(async (solicitud) => {
                    const botonInfo = `<button class="btn-info" data-te-toggle="modal" data-te-target="#modalInfoNoTratado" data-id="${solicitud.id}"></button>`;

                    return {
                        id: solicitud.id,
                        empresa: solicitud.empresa,
                        contacto: solicitud.contacto,
                        correo: solicitud.correo,
                        telefono: solicitud.telefono,
                        ubicacion: solicitud.ubicacion,
                        detalles: solicitud.detalles,
                        presupuesto: solicitud.presupuesto + " €",
                        comentarios: solicitud.comentarios,
                        tratado: solicitud.tratado,
                        canciones: solicitud.canciones,
                        info: botonInfo
                    };
                }));

                const columns = [
                    { label: "Id", field: "id" },
                    { label: "Empresa", field: "empresa" },
                    { label: "Contacto", field: "contacto" },
                    { label: "Correo", field: "correo" },
                    { label: "Ubicacion", field: "ubicacion" },
                    { label: "Detalles", field: "detalles" },
                    { label: "Presupuesto", field: "presupuesto" },
                    { label: "Info", field: "info", sort: false },
                ];

                const data = {
                    columns,
                    rows: canciones,
                };

                this.initDataTableNoTratado(data);

                const tableContainer = document.getElementById('datatable-noTratado');
                tableContainer.addEventListener('click', (event) => {
                    const target = event.target;
                    if (target.classList.contains('btn-info')) {
                        const idSolicitud = target.getAttribute('data-id');
                        this.cambiarInfoNoTratadoModal(idSolicitud);
                    }
                });

            } catch (error) {
                console.error('Error fetching solicitudes:', error);
            }
        },


        initDataTableNoTratado(data) {

            const tableElement = document.getElementById('datatable-noTratado');
            tableElement.innerHTML = '';

            const instance = new Datatable(document.getElementById('datatable-noTratado'), data, {
                hover: true,
            });
        },

        async cambiarInfoNoTratadoModal(idSolicitud) {
            try {
                const response = await axios.get(`http://localhost:8000/api/editorial/solicitudes/${idSolicitud}`);
                const solicitud = response.data;

                this.solicitudNoTratadoModal.id = solicitud.id;
                this.solicitudNoTratadoModal.empresa = solicitud.empresa;
                this.solicitudNoTratadoModal.contacto = solicitud.contacto;
                this.solicitudNoTratadoModal.correo = solicitud.correo;
                this.solicitudNoTratadoModal.telefono = solicitud.telefono;
                this.solicitudNoTratadoModal.ubicacion = solicitud.ubicacion;
                this.solicitudNoTratadoModal.detalles = solicitud.detalles;
                this.solicitudNoTratadoModal.presupuesto = solicitud.presupuesto;
                this.solicitudNoTratadoModal.comentarios = solicitud.comentarios;
                this.solicitudNoTratadoModal.canciones = [];

                await Promise.all(solicitud.canciones.map(async (idCancion) => {
                    const cancionResponse = await axios.get(`http://localhost:8000/api/editorial/canciones/${idCancion}`);
                    const cancion = cancionResponse.data;

                    await this.fetchEntidadName(cancion);

                    this.solicitudNoTratadoModal.canciones.push({
                        nombre: cancion.nombre,
                        entidadNombre: cancion.entidadNombre
                    });
                }));


            } catch (error) {
                console.error('Error fetching solicitudes:', error);
            }

        },

        async fetchEntidadName(cancion) {
            try {
                const entidadResponse = await axios.get(`http://localhost:8000/api/editorial/entidades/${cancion.entidad}/`);
                cancion.entidadNombre = entidadResponse.data.nombre;
            } catch (error) {
                console.error('Error fetching entidad:', error);
            }
        },

        async aceptarSolicitud() {
            try {
                await this.marcarComoTratada(this.solicitudNoTratadoModal.id);
                this.$router.go();
            } catch (error) {
                console.error('Error al aceptar solicitud:', error);
            }
        },

        async marcarComoTratada(solicitudId) {
            try {
                const response = await axios.put(`http://localhost:8000/api/editorial/solicitudes/${solicitudId}/marcar-tratada/`);
                console.log(response.data);  // Manejar la respuesta como sea necesario
            } catch (error) {
                console.error('Error al marcar solicitud como tratada:', error);
                throw error;  // Re-lanzar el error para que pueda ser manejado por la función que llamó a esta
            }
        },

        async eliminarSolicitud() {
            try {
                await this.eliminacionSolicitud(this.solicitudNoTratadoModal.id);
                this.$router.go();
            } catch (error) {
                console.error('Error al eliminar solicitud:', error);
            }
        },

        async eliminacionSolicitud(solicitudId) {
            try {
                const response = await axios.delete(`http://localhost:8000/api/editorial/solicitudes/${solicitudId}/eliminar_solicitud/`);
                console.log(response.data);  // Manejar la respuesta como sea necesario
            } catch (error) {
                console.error('Error al eliminar solicitud:', error);
                throw error;  // Re-lanzar el error para que pueda ser manejado por la función que llamó a esta
            }
        },

    }
}
</script>

<style>
.btn-info {
    background-image: url('../../public/images/configuraciones.png');

    background-size: cover;

    width: 35px;

    height: 35px;
}
</style>