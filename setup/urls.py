# extensão/urls.py
from django.urls import path
from extensão.views import index

urlpatterns = [
    path('', index, name='index'),  # URL raiz para renderizar index.html
]

# from django.contrib import admin
# from django.urls import path
# from extensão.views import index
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',index),
# ]
