
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Api.urls')),
    path('auth/', include('Accounts.urls')),
    path('', include('Classroom.urls')),

    
]

wrongurlpatterns = [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]
urlpatterns += wrongurlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)