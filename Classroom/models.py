from django.db import models

# Create your models here.

from Accounts.models import *

class MyPost(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(MyClassroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.post


class MyComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(MyPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
