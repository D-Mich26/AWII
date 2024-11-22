from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MesaDeAyudaFESC import views

# Define las URLs de tu proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevo_empleado/', views.nuevo_empleado, name='nuevo_empleado'),
    path('nuevo_tecnico/', views.nuevo_tecnico, name='nuevo_tecnico'),
    path('nueva_peticion/', views.nueva_peticion, name='nueva_peticion'),
    path('asignar_ticket/', views.asignar_ticket, name='asignar_ticket'),
    path('resolver_ticket/<int:peticion_id>/', views.resolver_ticket, name='resolver_ticket'),
]


# Añadir rutas para servir archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
