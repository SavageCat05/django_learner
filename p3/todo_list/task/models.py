from django.db import models
from django.contrib.auth.models import User

priorities = (
    ('low','low'),
    ('medium','medium'),
    ('high','high'),
)


# Create your models here.

class sign_in(models.Model):
    # id = models.AutoField(primary_key=True, db_column='user_id')
    Username = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField()
    phone = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.Username} {self.phone}"


class task_loader(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_id', null=True, blank=True)
    # phone = models.OneToOneField(sign_in, on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.CharField(max_length=50)
    task_priority = models.CharField(max_length=50, choices=priorities)
    task_due_date = models.DateField()
    task_detail = models.TextField(max_length=200)


    def __str__(self):
        return f"{self.task_title} \nDue-Date:({self.task_due_date})"

# from task.models import sign_in, task_loader