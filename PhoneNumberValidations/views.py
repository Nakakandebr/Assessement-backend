from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import PhoneNumber
from .serializers import PhoneNumberSerializer

class PhoneNumberList(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

    def list(self, request, *args, **kwargs):
        phone_numbers = self.get_queryset()
        serializer = self.get_serializer(phone_numbers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhoneNumberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhoneNumberFilter(generics.ListAPIView):
    serializer_class = PhoneNumberSerializer

    def list(self, request, *args, **kwargs):
        try:
            country = self.kwargs['country']
            state = self.kwargs['state']
            phone_numbers = PhoneNumber.objects.filter(country=country, state=state)
            serializer = self.get_serializer(phone_numbers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PhoneNumber.DoesNotExist:
            return Response({'detail': 'Phone number not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
