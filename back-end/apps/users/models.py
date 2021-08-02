from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """
        La clase UserManager se usa para sobre escribir los metodos
        usados por django.contrib.auth para crear los diferentes tipos 
        de usuarios.

        En este caso se sobre escribe el metodo create_user para que registre a 
        los usuarios de tipo operator y costumer, el metodo create_superuser se 
        sobre escribe para que pueda crear un super usuario con los campos definidos 
        en el modelo.  

    """

    def create_user(self, identification, user_type, first_name, 
                    last_name, email, phone_number = "",password=None,
                    is_admin=False, is_staff=False, is_active=True):
        if not identification:
            raise ValueError("User must have an identification")
        if user_type == 3 and not password:
            raise ValueError("User must have a password")
        if user_type == 3 and not phone_number:
            raise ValueError("User must have a phone Number")
        
        if user_type == 3: 
            is_staff = True

        user = self.model(
            identification=identification,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            email = email
        )
        user.user_type = user_type
        user.set_password(password)  
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active

        user.save(using=self._db)
        return user
        
    def create_superuser(self, identification, user_type, 
                         password, first_name = None, last_name = None, 
                         phone_number = None, **extra_fields):
        if not identification:
            raise ValueError("User must have an identification")
        if not password:
            raise ValueError("User must have a password")


        user = self.model(
            identification=identification
        )
        user.user_type = user_type
        user.set_password(password)
        user.staff = True
        user.is_superuser = True
        user.admin =True
        user.active = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    #tipos de usuarios pemitidos en el sistema
    USER_TYPE_CHOICES = (
      (1, 'admin'),
      (2, 'costumer'),
      (3, 'operator'),
    )
    username=None
    #se extiende el modelo de usuarios de django con los campos que se requieren para el comercio
    phone_number=models.CharField( max_length=15, blank=True)
    identification=models.CharField(max_length=12, unique=True)
    email=models.CharField(unique=True, max_length=50, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
  
    #cambio de autenticacion, por autenticacion por medio del numero de identificacion y password
    USERNAME_FIELD = 'identification'
    REQUIRED_FIELDS = ['user_type']    
    
    objects = UserManager()