from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('order/request/', views.order_request, name='order_request'),
    path('order/tracking/<str:token>/', views.order_track, name='order_tracking')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
