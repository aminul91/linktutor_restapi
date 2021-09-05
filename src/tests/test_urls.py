from django.test import SimpleTestCase
from django.urls import resolve,reverse
from app.views import *

class TestUrls(SimpleTestCase):
    def test_get_url_resolve(self):
        url = reverse('tutorials')
        self.assertEqual(resolve(url).func.view_class, ApiView)
    
    def test_insert_update_url_resolve(self):
        url = reverse('tutorial_insert')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ApiInsert)
        
    
    
    
