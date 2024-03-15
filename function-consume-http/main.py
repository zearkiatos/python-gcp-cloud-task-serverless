def consume(request):
    """Definición de la función invocada por la Cloud Function. 
    La función retorna la información recibida de en el body
    
    Args:
        request (flask.Request): Objeto con la información de la petición.
    Returns:
        Información recibida en el body de la petición
    """
    data = request.data
    print('Se recibe un elemeto de la cola')
    print(data)
    return data
