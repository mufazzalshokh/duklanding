from django.urls import path

from page.views import HomeTemplateView

app_name = 'page'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
]
