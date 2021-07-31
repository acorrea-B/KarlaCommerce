from django.contrib.auth import get_user_model

class UserManager:

    def get_or_create_costumer(self, identification, first_name,
                               last_name, email):
        """
            get_or_create_costumer esta función se encarga de obtener un usuario
            por su número de identificación si este usuario no existe lo crea como 
            nuevo y retorna al usuario
            Argumentos:
                identification(str) - número de identificacion del cliente
                first_name(str) - nombres del cliente
                last_name(str) - apellidos del cliente
                email(str) - correo electónico del cliente
                
            Retorna:
                costumer(User)
        """
        try:
            costumer = get_user_model().\
                       objects.get(identification = identification)
        except get_user_model().DoesNotExist:
            costumer = get_user_model().\
                      objects.create_user(user_type = 2,
                                          first_name = first_name,
                                          last_name = last_name,
                                          identification = identification,
                                          email = email
                                          )
            costumer.save()
            return costumer
        else:
            return costumer