from django.db import models

# Create your models here.

class User_data(models.Model):
    user_id=models.CharField(max_length=200)
    text_index=models.IntegerField(default=0)

    def __str__(self):
        return '{} : {}'.format(self.user_id,self.text_index)
