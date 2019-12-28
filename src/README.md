# Автоматическое создание REST API для всех моделей DRF проекта.

Сам код находится в /src/ubex_auto_api/core.py


**Подразумевается, что в приложении уже установлены:**
- Django==3.0.1
- djangorestframework==3.11.0
- django-filter==2.2.0


## Установка:
1. Скачать проект
2. Выполнить *pip install /путь/до/скачанного/проекта/src/distr/ubexautoapi-0.1.tar.gz*
3. Импортировать в главный файл *urls.py*
```
from ubex_auto_api.core import create_auto_router

*** какой-то код ***

auto_router = create_auto_router()
urlpatterns.append(
    url('auto_api/', include(auto_router.urls)),
)
```
4. Готово


## Использование
Теперь все модели будут доступны по */auto_api/*

Например модель Rate доступна по */auto_api/rate*

Имена моделей у урлах задаются в нижнем регистре.

Доступна фильтрация по полям модели, например:
```/auto_api/rate?date=22&rate=2```

Доступно лимитирование (и пагинация через offset), например:
```/auto_api/rate?limit=2```

Доступна сортировка, например:
```/auto_api/rate?ordering=id```


Доступны операции: получение списка, получение по ключу, создание, изменение по ключу, удаление по ключу (GET, POST, PUT, DELETE методы).



