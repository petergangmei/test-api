from restapi.viewsets import StudentViewset
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('student', StudentViewset)