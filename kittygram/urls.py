# from django.urls import path
# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]


# # Обновлённый urls.py
# from django.urls import path
# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ]


# # Обновлённый urls.py
# from django.urls import path
# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]

# urls.py
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import include, path
from cats.views import CatViewSet

# router = SimpleRouter()
router = DefaultRouter()
router.register('cats', CatViewSet, basename='cat')

urlpatterns = [
    path('', include(router.urls)),
]
