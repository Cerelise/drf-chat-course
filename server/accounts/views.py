from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate

from .models import User
from .serializers import SignUpSerializer


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "用户创建成功", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        current_user = User.objects.filter(email=email)

        if user is not None:
            Token.objects.filter(user=current_user[0]).delete()
            Token.objects.create(user=current_user[0])

            response = {
                "message": "登录成功！",
                "user": {
                    "user_id": user.id,
                    "name": user.username,
                    "email": user.email,
                    "token": user.auth_token.key,
                },
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "无效的邮箱或密码"})

    def get(self, request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([])
def Logout(request):
    token = request.data["token"]
    # print(token)
    user_token = Token.objects.get(key=token)
    user_token.delete()

    response = {"message": "用户已成功登出"}

    return Response(data=response, status=status.HTTP_200_OK)