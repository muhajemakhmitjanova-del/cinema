from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import RegisterSerializer


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "Пользователь успешно создан!"})