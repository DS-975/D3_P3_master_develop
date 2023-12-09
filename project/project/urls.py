from django.contrib import admin
from django.urls import path, include # include <- Для работы приложения Flatpages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')), # <- Для работы приложения Flatpages

    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
    # подключились к главному приложению с прификсом products/.
    path('products/', include('simpleapp.urls'))
]
