from django.urls import path

from IFRNNews.views import home, contato, sobre

# dominio/IFRNews/sobre/contato

urlpatterns = [
    path("", home),  # home
    path("sobre/", sobre),  # /sobre/
    path("contato/", contato),  # /contato/
]
