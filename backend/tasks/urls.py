from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet, DashboardView
router=DefaultRouter(); router.register('categories',CategoryViewSet,basename='category'); router.register('tasks',TaskViewSet,basename='task')
urlpatterns=[path('tasks/dashboard/',DashboardView.as_view(),name='dashboard'),path('',include(router.urls))]
