### URL and URL's include from app

```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('shop/', include('shop.urls'))
]
```

