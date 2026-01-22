from django.db import models #BD Tools
from django.contrib.auth.models import User #UserModel

#TaskTable
class Task(models.Model):
    title=models.CharField(max_length=200)
    description= models.TextField(blank=True)

 #StateList
    status_choices=[
        ('to do', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]   

    status=models.CharField(
        max_length=10,
        choices=status_choices,
        default='to do'
    )

    #PriorityList
    priority_choices=[
        (1, '1 - Very Low'),
        (2, '2 - Low'),
        (3, '3 - Medium'),
        (4, '4 - High'),
        (5, '5 - Critical'),
    ]

    priority=models.IntegerField(
        choices=priority_choices,
        default=1
    )

    #TaskUserRelation / DeleteData
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    #Creation,update and expiration times
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    due_date=models.DateTimeField(null=True, blank=True)

    #TaskTitle
    def __str__(self):
        return self.title
    
    #To make it look nice :D
    class Meta:
        verbose_name='Task'
        verbose_name_plural='Tasks'
        

