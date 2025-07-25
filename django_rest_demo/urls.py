from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes/', include('school_class.urls')),
    path('subjects/', include('subjects.urls')),
    path('teachers/', include('teacher.urls')),

]
