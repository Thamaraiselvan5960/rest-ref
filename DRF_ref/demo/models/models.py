from django.db import models

class Sample(models.Model):
    id = models.AutoField(primary_key=True)
    name = modelsl=models.CharField(null=True,blank=True)
    age = models.IntegerField(default = 10,blank = True)


    class Meta:
        managed = True  #if using external model
        db_table = 'feeds"."feeds' # table name in database

    def __str__(self):
        return f'{self.description}'