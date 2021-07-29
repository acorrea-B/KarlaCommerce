from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersTestCase(TestCase):
    def setUp(self):
        self.super_user = {"identification" : "1234",
                      "password" : "pass1234567",
                      "user_type":1,
                    } 
        self.operator = {"first_name":"a",
                         "last_name":"b",
                         "identification":"1231298",
                         "password":"er",
                         "user_type":3,
                         "phone_number":"213123123",
                         "email":"asdas@commerce.co"
                        }
        self.customer = {"first_name":"pepito",
                          "last_name":"perez",
                          "identification":"3245645",
                          "user_type":2,
                          "email":"asdas@example.com"
                        }

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(**self.super_user)
        user.save()
        
        user_create = get_user_model().\
                      objects.get(identification = self.super_user.get("identification"))
        
        self.assertTrue(user_create)
        self.assertTrue(user_create.is_active)
        self.assertTrue(user_create.is_superuser)

    
    def test_create_operator(self):
        user = get_user_model().objects.create_user( **self.operator )
        user.save()
        user_create = get_user_model().\
                      objects.get(identification = self.operator.get("identification"))
        
        self.assertTrue(user_create)
        self.assertTrue(user_create.is_active)
        self.assertFalse(user_create.is_superuser)
    
    def test_create_customer(self):
        user = get_user_model().objects.create_user( **self.customer )
        user.save()
        user_create = get_user_model().\
                      objects.get(identification = self.customer.get("identification"))
        
        self.assertTrue(user_create)
        self.assertTrue(user_create.is_active)
        self.assertFalse(user_create.is_superuser)
    
    