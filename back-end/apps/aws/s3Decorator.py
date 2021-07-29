"""
    Los decoradores, por medio de un wrapper agregan
    logica que permite la gestion de errores en los datos de 
    entrada y salida, además, de la gestión de la comunicacion  con S3.

    En este caso se maneja una restriccion solo para archivos de imagenes
    con los formatos ".jpg",".jpeg", ".png
"""

def validate_str_extension(  file_patch ):
    extencion = str.find( file_patch, ".",   
                          len(file_patch) - 6,
                               len(file_patch) - 1 
                            )
    extencion - len(file_patch)
    extencions = [".jpg",".jpeg", ".png"]
    return file_patch[extencion:] in extencions
    

def photo_url( function ):
    def func( self, file_name, time):
        if validate_str_extension( file_name ) and isinstance(time, int):
            return function(self, file_name, time)
        else:
            return "Formato de archivo no permitido, solo se admiten (.jpg, .jpeg, .png) en en el file_name e int en experitation"
    return func