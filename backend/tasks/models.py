from django.conf import settings
from django.db import models
from django.utils import timezone
class Category(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='categories')
 name=models.CharField(max_length=60); color=models.CharField(max_length=7,default='#4F46E5')
 class Meta: unique_together=('user','name'); ordering=['name']
 def __str__(self): return self.name
class Task(models.Model):
 PRIORITIES=[('Low','Low'),('Medium','Medium'),('High','High')]
 STATUSES=[('To Do','To Do'),('In Progress','In Progress'),('Done','Done')]
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='tasks')
 title=models.CharField(max_length=100); description=models.TextField(blank=True)
 category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL,related_name='tasks')
 priority=models.CharField(max_length=10,choices=PRIORITIES,default='Medium'); status=models.CharField(max_length=20,choices=STATUSES,default='To Do')
 due_date=models.DateField(null=True,blank=True); completed_at=models.DateTimeField(null=True,blank=True)
 created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
 class Meta: ordering=['due_date','-created_at']
 def save(self,*args,**kwargs):
  if self.status=='Done' and not self.completed_at: self.completed_at=timezone.now()
  elif self.status!='Done': self.completed_at=None
  super().save(*args,**kwargs)
 def __str__(self): return self.title
