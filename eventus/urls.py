from django.conf.urls import url
import events
from django.contrib import admin
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ 
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
    path('panel/',views.main_panel,name="panel")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)