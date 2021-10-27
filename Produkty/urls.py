from rest_framework import  routers
from django.urls import include ,path
from .views import KategoriaViewSet,ProduktyViewSet, ProducentViewSet

router = routers.DefaultRouter()
router.register(r'kate', KategoriaViewSet)
router.register(r'produk',ProduktyViewSet)
router.register(r'prod',ProducentViewSet)

urlpatterns = [

    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]