from django.db import models

# Create your models here.
class Event(models.Model):
    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', "Muito Urgente"),
         )
    inital_date = models.DateField()
    final_date = models.DateField()
    responsible_technician = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    priority = models.CharField(max_length=1)

    def __str__(self):
        return self.description