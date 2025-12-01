
from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('cart/', include('cart.urls')),
    path('',include('app.urls')),
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('dashboard/',include('dashboarditems.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)