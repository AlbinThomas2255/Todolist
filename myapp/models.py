from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

todos=[

    {"id":1,"task_name":"gbillpay","user":"ram"},
    {"id":2,"task_name":"task2","user":"ravi"},
    {"id":3,"task_name":"task3","user":"arjun"},
    {"id":4,"task_name":"task4","user":"aravind"},
    {"id":5,"task_name":"task5","user":"arjun"},
    {"id":6,"task_name":"task6","user":"hari"},

    
]

class Todos(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task_name



    # orm querry create
    # ModelName.objects.create(feild1=value1,feild2=value2,......feildn=valuen)
    # Todos.object.create(task_name='ebill',user='ram')



    # for fetching all todos
    # qs=modelname.objects.all()
    # qs=Todos.objects.all()



    # for fetching specific one
    # td=modelname.objects.get(id=2)
    # td=Todos.objects.get(id=2)


    # filtering
    # qs=modelname.objects.filter(user="ram")
    # qs=Todo.obejcts.filter(user="ram")


    # update orm
    # Todos.objects.filter(id=1).update(task_name="electricity bill")


    # delete orm

    # Todos.objects.filter(id=1).delete()


