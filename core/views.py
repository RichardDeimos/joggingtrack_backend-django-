from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken
from .serializers import UserSerializer
from rest_framework import generics
from django.http import HttpResponse
from core.models import Profile, Record
from core.serializers import ProfileSerializer, RecordSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def GetUserRole(request):
    userRole = request.user.profile.role
    return Response(userRole, status=status.HTTP_201_CREATED)

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = (permissions.IsAuthenticated)
    def get_queryset(self):
        records = Record.objects.all()
        if self.request.GET :         
            print("################get_queryset start###########")
            print(self.request.query_params)
            userRole = self.request.user.profile.role

            if userRole != 'admin':
                records = records.filter(user_id=self.request.user.id)
            fromdate = self.request.query_params['from'];
            todate = self.request.query_params['to'];
            if todate :
                records = records.filter(date__lte=todate)
            if fromdate:
                records = records.filter(date__gte=fromdate)
        # else:
        #     print("################INPUT start###########")
        #     print(self.request.data)
        #     record = RecordSerializer(data=self.request.data)
        #     if record.is_valid():
        #         profile = record.update(instance)   
        #     return record
        return records


class Signup(APIView): 
    #permission_classes = (permissions.IsAuthenticated, )
    def post(self, request, format=None):

        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated, )
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
