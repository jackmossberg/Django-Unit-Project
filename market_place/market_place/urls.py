
from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from items import views as item_views

urlpatterns = [
    path('', item_views.browsing, name='home'),
    path('cart/', include('cart.urls')),
    path('app/',include('app.urls')),
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('dashboard/',include('dashboarditems.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)