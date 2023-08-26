from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


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
    try:
        message = Message.objects.filter(room=room)[0:20]
        serializer = MessageSerializer(message, many=True)
        serializer_data = serializer.data
        return Response(
            {
                "message": "进入房间成功！",
                "room": room_detail,
                "message_list": serializer_data
            },
            status=status.HTTP_200_OK)
    except:
        return Response({"message": "进入房间成功！", "room": room_detail})
