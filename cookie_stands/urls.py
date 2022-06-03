from django.urls import path
from .views import CookiestandList, CookiestandDetail

urlpatterns = [
    path("", CookiestandList.as_view(), name="cookiestand_list"),
    path("<int:pk>/", CookiestandDetail.as_view(), name="cookiestand_detail"),
]
