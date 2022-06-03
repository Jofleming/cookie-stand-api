from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookiestand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookiestandSerializer


class CookiestandList(ListCreateAPIView):
    queryset = Cookiestand.objects.all()
    serializer_class = CookiestandSerializer


class CookiestandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cookiestand.objects.all()
    serializer_class = CookiestandSerializer
