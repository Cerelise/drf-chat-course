from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def room_list(requset):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    serializer_data = serializer.data

    return Response({
        "message": "获取房间列表成功！",
        "rooms": serializer_data
    },
                    status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    roomSerializer = RoomSerializer(room)
    room_detail = roomSerializer.data
    return Response({
        "message": "进入房间成功！",
        "room": room_detail
    },
                    status=status.HTTP_200_OK)
