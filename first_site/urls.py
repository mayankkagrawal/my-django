from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('votings/', include('voting.urls')),
    path('admin/',admin.site.urls),
]
