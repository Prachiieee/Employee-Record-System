from django.urls import path,include
from . import views
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('skill_api',views.SkillViewSet,basename='skill_api')
router.register('Dep_api',views.DepartmentViewSet,basename='Dep_api')
router.register('Emp_api',views.EmpViewSet,basename='Emp_api')

urlpatterns = [
    path('',views.home, name='home'),
    path('api/',include(router.urls))
]