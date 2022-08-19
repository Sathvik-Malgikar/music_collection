from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  


urlpatterns = [
    path('library',views.library,name='library'),
    path('library/listen',views.listen,name="listen"),
    path('library/search',views.search,name="search"),
    path('library/getmedia/',views.getmedia,name="getmedia"),
    ]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)