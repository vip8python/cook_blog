from django.urls import path
from django.views.generic import CreateView

from contact.views import ContactView, AboutView

app_name = 'contact'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('feedback/', CreateView.as_view(), name='feedback'),
    path('about/', AboutView.as_view(), name='about'),

]
