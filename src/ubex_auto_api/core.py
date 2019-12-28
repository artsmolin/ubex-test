import django.apps
from rest_framework import serializers as s, viewsets, routers
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


def create_auto_router():
    _view_set_classes = []
    models = django.apps.apps.get_models(include_auto_created=True)

    for model in models:
        serializer_class = _create_serializer_class(model)
        view_set_class = _create_view_set_class(serializer_class)
        _view_set_classes.append(view_set_class)

    router = _create_router(_view_set_classes)
    return router


def _create_serializer_class(model):
    serializer_class = type(f'{model.__class__.__name__}Serializer',
                            (s.ModelSerializer,),
                            {})
    serializer_class.Meta = type('Meta', (), {'model': model, 'fields': '__all__'})
    return serializer_class


def _create_view_set_class(serializer_class):
    model = serializer_class.Meta.model
    model_field_names = [field.name for field in model._meta.get_fields()]
    view_set_class = type(f'{model.__class__.__name__}ViewSet',
                          (viewsets.ModelViewSet,),
                          {
                              'queryset': model.objects.all(),
                              'serializer_class': serializer_class,
                              'filter_backends': [DjangoFilterBackend, OrderingFilter],
                              'filterset_fields': model_field_names,
                              'ordering_fields': model_field_names,
                              'pagination_class': LimitOffsetPagination,
                          })
    return view_set_class


def _create_router(view_set_cls):
    _router = routers.DefaultRouter()
    for view_set_class in view_set_cls:
        path = f'{view_set_class.serializer_class.Meta.model.__name__}'.lower()
        _router.register(path, view_set_class)
    return _router
  