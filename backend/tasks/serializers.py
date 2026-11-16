from datetime import date
from rest_framework import serializers
from .models import Category, Task
class CategorySerializer(serializers.ModelSerializer):
 class Meta: model=Category; fields=('id','name','color'); read_only_fields=()
 def validate_name(self,value):
  qs=Category.objects.filter(user=self.context['request'].user,name__iexact=value.strip())
  if self.instance: qs=qs.exclude(pk=self.instance.pk)
  if qs.exists(): raise serializers.ValidationError('You already have a category with this name.')
  return value.strip()
 def validate_color(self,value):
  import re
  if not re.fullmatch(r'#[0-9A-Fa-f]{6}',value): raise serializers.ValidationError('Enter a valid hex colour, e.g. #4F46E5.')
  return value
class TaskSerializer(serializers.ModelSerializer):
 category=CategorySerializer(read_only=True)
 category_id=serializers.PrimaryKeyRelatedField(source='category',queryset=Category.objects.all(),allow_null=True,required=False,write_only=True)
 class Meta: model=Task; fields=('id','title','description','category','category_id','priority','status','due_date','completed_at','created_at','updated_at'); read_only_fields=('id','completed_at','created_at','updated_at')
 def validate_title(self,value):
  value=value.strip()
  if len(value)<3: raise serializers.ValidationError('Title must contain at least 3 characters.')
  if len(value)>100: raise serializers.ValidationError('Title cannot exceed 100 characters.')
  return value
 def validate_due_date(self,value):
  if value and not self.instance and value<date.today(): raise serializers.ValidationError('Due date cannot be in the past.')
  return value
 def validate_category_id(self,value):
  if value and value.user_id!=self.context['request'].user.id: raise serializers.ValidationError('Choose one of your own categories.')
  return value
