from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.v1.register.serializers import RegisterSerializer
from api.v1.register.models import Register


class RegisterApi(APIView):

    def post(self, request):
        try:
            serializer = RegisterSerializer(data=self.request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        'status': False,
                        "error": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'error': str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                {
                    'status': True
                }, status=status.HTTP_200_OK
            )

