from django.urls import path, include
from .views import ProfileList, Signup,  GetUserRole, RecordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'records', RecordViewSet)

urlpatterns = [
    path('auth/signup', Signup.as_view()),
    path('users', ProfileList.as_view()),
    path('profile', GetUserRole ),
    path('', include(router.urls))
]