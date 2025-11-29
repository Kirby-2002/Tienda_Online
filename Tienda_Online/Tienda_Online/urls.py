# Tienda_Online/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. Rutas de administración
    path('admin/', admin.site.urls),
    
    # 2. Rutas de la aplicación (Catálogo, Solicitud, etc.)
    path('', include('MainApp.urls')),
]

# 3. Configuración para servir archivos MEDIA (solo en modo DEBUG)
# Este bloque toma la configuración de MEDIA_URL y MEDIA_ROOT de settings.py
# y le dice al servidor de desarrollo que sirva esos archivos.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)