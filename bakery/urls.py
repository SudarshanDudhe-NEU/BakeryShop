"""
URL configuration for bakery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from pages.views import home, about, contact  # Import the additional views
from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page at the root URL
    path('products/', product_views.product_list, name='product_list'),
    path('products/<int:product_id>/',
         product_views.product_detail, name='product_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

# Serve media files during development (in debug mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
