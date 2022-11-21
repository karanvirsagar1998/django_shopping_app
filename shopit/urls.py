from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shopit import settings


urlpatterns = [
    path('', include('adminSetup.urls')),
    path('admin/', admin.site.urls),
    # for admin panel
    path('adminSetup/', include('adminSetup.urls')),
    path('view-all-cats/', include('adminSetup.urls')),
    path('add-new-cat/', include('adminSetup.urls')),
    path('view-all-sub-cats/', include('adminSetup.urls')),
    path('add-new-sub-cat/', include('adminSetup.urls')),
    path('edit-category/<str:id>', include('adminSetup.urls')),
    path('delete-category/<str:id>/<str:param>/', include('adminSetup.urls')),
    path('edit-sub-category/<str:id>', include('adminSetup.urls')),
    path('delete-sub-category/<str:id>/<str:param>/', include('adminSetup.urls')),
    path('view-all-products', include('adminSetup.urls')),
    path('add-new-product/', include('adminSetup.urls')),
    path('edit-product/<str:id>', include('adminSetup.urls')),
    path('delete-product/<str:id>', include('adminSetup.urls')),
    path('get-products-count-by-week/<int:month>', include('adminSetup.urls')),
    path('get-product-sales-info', include('adminSetup.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

