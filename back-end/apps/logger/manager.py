import os
import logging

class Logger(type):
    """
        Esta clase aplica el patron de diseño singelton par el manejo del logger
        en el proyecto con el fin de dejar un estandar en el reportse re errores o 
        advertencias del sistema
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Retorna la instancia de la clase
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ManagerLogging( metaclass = Logger ):
    
    def __init__(self):
        logging.getLogger('boto3').setLevel(logging.CRITICAL)
        logging.getLogger('botocore').setLevel(logging.CRITICAL)
        logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
        logging.getLogger('urllib3').setLevel(logging.CRITICAL)
        self.logger = logging.getLogger("Karla_backend")
        self.logger.addHandler(logging.StreamHandler()) # Writes to console
        self.logger.setLevel(self.set_level())
        logging.basicConfig( format='%(asctime)s | %(levelname)s | %(message)s | %(info)s' )
    
    def set_level( self ):
        try:
            from django.conf import settings
        except ModuleNotFoundError:
            return os.environ.get("Logging")
        else:
            return settings.LOG

    def get_logger( self ):
        return self.logger