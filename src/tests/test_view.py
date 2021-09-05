from django.test import TestCase, Client
from django.urls import reverse
from app.models import *
from app.views import *

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.tutorials_url = reverse('tutorials')
        self.tutorials_insert = reverse('tutorial_insert')
        
        
    def test_Project_list_GET(self):
        response = self.client.get(self.tutorials_url)
        self.assertEqual(response.status_code,200)
    
        


        
    
    
    
