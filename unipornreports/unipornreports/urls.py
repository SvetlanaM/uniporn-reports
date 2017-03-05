from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from reports.views import base_view
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', base_view, name ='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
