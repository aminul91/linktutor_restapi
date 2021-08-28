from django.urls import path
from app.views import home_view

app_name = 'app'

urlpatterns = [
    # url: '/', name = app:home
    path('', home_view, name='home'),
]
