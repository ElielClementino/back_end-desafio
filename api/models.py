from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    user_task = models.ForeignKey('User', on_delete=models.SET_NULL, related_name='tarefas', null=True, blank=True,)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
