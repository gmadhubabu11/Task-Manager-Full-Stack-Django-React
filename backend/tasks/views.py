from datetime import date
from django.db.models import Count, Q
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from .filters import TaskFilter
class CategoryViewSet(viewsets.ModelViewSet):
 serializer_class=CategorySerializer; permission_classes=[permissions.IsAuthenticated]; http_method_names=['get','post','put','patch','delete','head','options']
 def get_queryset(self): return Category.objects.filter(user=self.request.user)
 def perform_create(self,serializer): serializer.save(user=self.request.user)
class TaskViewSet(viewsets.ModelViewSet):
 serializer_class=TaskSerializer; permission_classes=[permissions.IsAuthenticated]; filterset_class=TaskFilter
 search_fields=['title','description']; ordering_fields=['due_date','priority','created_at']; ordering=['due_date','-created_at']
 def get_queryset(self): return Task.objects.filter(user=self.request.user).select_related('category')
 def perform_create(self,serializer): serializer.save(user=self.request.user)
 @action(detail=True,methods=['patch'],url_path='toggle-complete')
 def toggle_complete(self,request,pk=None):
  task=self.get_object(); task.status='To Do' if task.status=='Done' else 'Done'; task.save(); return Response(self.get_serializer(task).data)
class DashboardView(APIView):
 permission_classes=[permissions.IsAuthenticated]
 def get(self,request):
  qs=Task.objects.filter(user=request.user); today=date.today()
  total=qs.count(); done=qs.filter(status='Done').count()
  overdue=qs.filter(due_date__lt=today).exclude(status='Done'); due_today=qs.filter(due_date=today).exclude(status='Done')
  cats=Category.objects.filter(user=request.user).annotate(task_count=Count('tasks')).values('id','name','color','task_count')
  return Response({'total':total,'to_do':qs.filter(status='To Do').count(),'in_progress':qs.filter(status='In Progress').count(),'done':done,'overdue':overdue.count(),'due_today':due_today.count(),'completion_percentage':round(done/total*100,1) if total else 0,'category_counts':list(cats),'overdue_tasks':TaskSerializer(overdue[:5],many=True,context={'request':request}).data,'today_tasks':TaskSerializer(due_today[:5],many=True,context={'request':request}).data})
