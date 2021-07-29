import boto3
from django.conf import settings
from botocore.config import Config
from botocore.exceptions import ClientError
from .s3Decorator import  photo_url

class Photos:
    """
        Esta clase maneja comunicación con el bucket de s3
        con el proyecto, mediante el cliente de boto3
    """

    def __init__( self, logging ):
        self.logging = logging
        self.bucket =  settings.IMAGES_BUCKET
        self.s3_client = self.s3_django_connection()
    
    def s3_django_connection( self ):
        try:
            session = boto3.client( "s3", 
                                     config = Config(signature_version='s3v4')
                                )
        except Exception:
            return Exception
        else:
            return session 
    
    @photo_url
    def get_presigned_url( self, file_name, expiration ):
        """
            Esta función tiene como objetivo obtener una url prefirmada
            de un objeto que se encuentre almacenado en el bucket de s3, 
            con el fin de no exponer los archivos del bucket y 
            evitar la descarga de los mismos en la raiz del proyecto.

            Argumentos:
                file_name(str) - nombre del archivo que se encuentra almacenado en s3
                expiration(int) - tiempo de vida de la url que se obtendra
            Retorna:
                url(str)  en caso de que todo salga bien
                e(dict) el error que se pudo presentar en el proceso despues de haber 
                        sido registrado en el log del sistema
        """
        try:
            response = self.s3_client.\
                        generate_presigned_url( "get_object", 
                                                Params = { "Bucket" : self.bucket,
                                                            "Key" : file_name },
                                                ExpiresIn = expiration,
                                                HttpMethod = "https"
                                            )
        except ClientError as e:
            # En el caso en que se presente un error se registra en el log del sistema
            self.logging.error(e, extra = { "info": self.get_presigned_url.__name__})
            return e
        else:
            return response