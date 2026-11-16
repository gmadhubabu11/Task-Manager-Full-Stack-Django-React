from datetime import date
from django.db.models import Q
import django_filters
from .models import Task
class TaskFilter(django_filters.FilterSet):
 due=django_filters.CharFilter(method='filter_due')
 def filter_due(self,queryset,name,value):
  today=date.today()
  if value=='today': return queryset.filter(due_date=today).exclude(status='Done')
  if value=='overdue': return queryset.filter(due_date__lt=today).exclude(status='Done')
  if value=='upcoming': return queryset.filter(due_date__gt=today).exclude(status='Done')
  return queryset
 class Meta: model=Task; fields=['status','priority','category']
