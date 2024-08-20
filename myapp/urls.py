from django.urls import path
from myapp.views import ItemListCreate, ItemDetail, SomeShit


urlpatterns = [
    path("items/", ItemListCreate.as_view(), name="item-create"),
    path("items/<int:pk>/", ItemDetail.as_view(), name="item-details"),
    path("shit/", SomeShit.as_view(), name="shit"),
]
