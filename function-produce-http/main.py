from google.cloud import tasks_v2
import os

# Se leen las variables de entorno especificadas
location_id = os.environ.get('LOCATION_ID', '')
projec_id = os.environ.get('PROJECT_ID', '')
queue_id = os.environ.get('QUEUE_ID', '')
url_function = os.environ.get('URL_FUNCTION', '')

client = tasks_v2.CloudTasksClient()

def produce(request):
    """Definición de la función invocada por la Cloud Function. 
    La función realiza el encolamiento de una tarea en Task Queue
    
    Args:
        request (flask.Request): Objeto con la información de la petición.
    Returns:
        Información con la información de la tarea creada
    """
    # Construye el nombre de la cola a la que se realizará la conexión
    parent = client.queue_path(projec_id, location_id, queue_id)

    # Definición de los parametros de la tarea que se creará
    task = {
        "http_request": {  # Determina el tipo de tareas, en este caso una petición HTTP.
            "http_method": tasks_v2.HttpMethod.POST,
            "url": url_function,  # Determina la URL completa a la que se realizará el consumo del servicio.
            "headers": {
                "Content-type": "application/json"
            },
            "body": request.data,
        }
    }
    # Se realiza la creación de la tarea en la cola
    response = client.create_task(request={"parent": parent, "task": task})
    return {
        'message': 'Se crea la tarea de manera exitosa',
        'name': response.name,
        'http_request': {
            'url' : response.http_request.url,
            'http_method' : str(response.http_request.http_method)
        }
    }
