from django.db import models


class Tarefas(models.Model):
    title = models.CharField(max_length=50)
    user_task = models.ForeignKey('User', on_delete=models.SET_NULL, related_name='tarefas')

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
