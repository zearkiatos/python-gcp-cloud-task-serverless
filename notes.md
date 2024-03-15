# GCP Cloud Task: Patrón Productor/Consumidor usando funciones y colas de tareas

## Objetivos

- Orquestar un conjunto de microservicios de manera asíncrona empleando colas de mensajería.
- Crear y configurar el servicio de Cloud Task para orquestar llamados de Cloud Function

## Estructura de carpetas

En el proyecto encontrará tres carpetas principales:

- La carpeta `collections` en donde se encuentra la colección de Postman para poder realizar pruebas sobre las funciones publicadas.
- La carpeta `function-consumir-http` en donde se encuentra la implementación de la función que será llamada por cada tarea del servicio de Cloud Task.
- La carpeta `function-producir-http` en donde se encuentra la implementación de la función que nos permitirá crear tareas al servicio de Cloud Task.

## Creación de la cuenta de servicio

Para crear y configurar la cuenta de servicio, por favor ejecute los siguiente comandos:

> No olvide remplazar <id_proyecto> con el identificador del proyecto que está utilizando

```console
gcloud iam service-accounts create misw-das-productor --description="Cuenta de servicio para el tutorial de cloud task" --display-name="Productor tutorial cloud task"
gcloud projects add-iam-policy-binding <id_proyecto> --member="serviceAccount:misw-das-productor@<id_proyecto>.iam.gserviceaccount.com" --role="roles/cloudtasks.enqueuer"
```

## Creación de la cola de tareas

Para realizar la creación de la cola en el servicio de Cloud Task, debe ejecutar el siguiente comando:

```console
gcloud tasks queues create cola-cloud-task-tutorial --location=us-central1
```

## Publicación de la funciones 

Debe tener presente que las funciones utilizarán la cuenta de almacenamiento para configurar los permisos que tienen. Además, se conectará a la cola previamente creada.

### Función Consumir Http

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los siguientes comandos:

```console
cd function-consumir-http
gcloud functions deploy funcion-tutorial-consumidor --entry-point consumir --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función

### Función Producir Http

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los siguientes comandos:

> No olvide remplazar <id_proyecto> con el identificador del proyecto que está utilizando

```console
cd function-producir-http
gcloud functions deploy funcion-tutorial-productor --entry-point producir --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --service-account "misw-das-productor@<id_proyecto>.iam.gserviceaccount.com" --set-env-vars LOCATION_ID=us-central1,PROJECT_ID=<id_proyecto>,QUEUE_ID=cola-cloud-task-tutorial,URL_FUNCTION=https://us-central1-<id_proyecto>.cloudfunctions.net/funcion-tutorial-consumidor
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función
