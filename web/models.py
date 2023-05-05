from django.db import models


# Create your models here.
class Event(models.Model):
    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', "Muito Urgente"),
    )

    inital_date = models.DateField(
        help_text="data inicial",
    )
    final_date = models.DateField(
        help_text="data final",
    )
    responsible_technician = models.CharField(
        help_text="responsável técnico",
        max_length=80,
        verbose_name="técnico",
    )
    description = models.CharField(
        help_text="visita, coleta, ou relatório?",
        max_length=100,
        verbose_name="descrição",
    )
    priority = models.CharField(
        max_length=1,
        choices=priorities_list,
        verbose_name="prioridade",
    )
    '''status: aberto (true) , fechado (false)'''
    oppened_status = models.BooleanField(
        default=True,
        help_text="aberto ou fechado?",
        verbose_name="status",
    )

    def __str__(self):
        return self.description
