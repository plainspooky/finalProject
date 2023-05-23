from django.db import models


# Create your models here.
class OtherDocuments(models.Model):
    registration_number = models.CharField(
        help_text="número de inscrição",
        max_length=50,
        verbose_name="número de inscrição",
    )
    description = models.CharField(
        help_text="nome da autarquia",
        max_length=200,
        verbose_name="nome da autarquia"
    )
class Company(models.Model):
    class Meta:
        abstract = True

    corporate_name = models.CharField(
        help_text="razão social da empresa contratada",
        max_length=200,
        verbose_name="Razão Social",
    )
    address = models.CharField(
        help_text="endereço da empresa contratada",
        max_length=200,
        verbose_name="Endereço",
    )
    phone_fax = models.CharField(
            help_text="telefone para contato",
            max_length=50,
            verbose_name="Telefone/Fax",
    )
    cnpj = models.CharField(
        blank=True,
        max_length=50,
        verbose_name=("CNPJ"),
        help_text=("CNPJ"),
    )

class ContractedCompany(Company):
    other_documents = models.ForeignKey(
        OtherDocuments,
        on_delete=models.CASCADE,
        verbose_name="Outros Documentos (licenças, registros e afins"
    )
class ContractingCompany(Company):
    email = models.EmailField(
        blank=True,
        help_text="endereço e-Mail",
        max_length=254,
        null=True,
        verbose_name="endereço e-Mail",
    )
    responsible_contact=models.CharField(
        help_text="Nome do Responsável Técnico",
        max_length=80,
        verbose_name="nome do responsável técnico",
    )

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
    other_documents = models.ForeignKey(
        OtherDocuments,
        on_delete=models.CASCADE,
        verbose_name="Outros documentos"
    )

    def __str__(self):
        return self.description
