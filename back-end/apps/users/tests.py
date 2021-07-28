from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersTestCase(TestCase):
    def setUp(self):
        self.admin = {"identification" : "1234",
                      "password" : "pass1234567",
                      "first_name":"a",
                      "last_name":"b",
                      "user_type":1,
                      "phoneNumber":"1256756"
                    } 
        self.operator = {"first_name":"a",
                         "last_name":"b",
                         "identification":"1231298",
                         "password":"er",
                         "user_type":3,
                         "phoneNumber":"213123123",
                         "email":"asdas@commerce.co"
                        }
        self.customer = {"first_name":"pepito",
                          "last_name":"perez",
                          "identification":"3245645",
                          "user_type":2,
                          "email":"asdas@example.com"
                        }

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(**self.admin)
        user.save()
        
        user_create = get_user_model().\
                      objects.get(self.admin.get("identification"))
        
        self.assertTrue(user_create)
        self.assertTrue(user_create.admin)
        self.assertTrue(user_create.staff)
        self.assertTrue(user_create.is_active)
        self.assertTrue(user_create.is_superuser)

    
    def test_create_operator(self):
        user = get_user_model().objects.create_user( **self.operator )
        user.save()
        user_create = get_user_model().\
                      objects.get(self.operator.get("identification"))
        
        self.assertTrue(user_create)
        self.assertFalse(user_create.admin)
        self.assertTrue(user_create.staff)
        self.assertTrue(user_create.is_active)
        self.assertFalse(user_create.is_superuser)
    
    def test_create_costumer(self):
        user = get_user_model().objects.create_user( **self.costumer )
        user.save()
        user_create = get_user_model().\
                      objects.get(self.costumer.get("identification"))
        
        self.assertTrue(user_create)
        self.assertFalse(user_create.admin)
        self.assertFalse(user_create.staff)
        self.assertTrue(user_create.is_active)
        self.assertFalse(user_create.is_superuser)
    
    