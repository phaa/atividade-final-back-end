import uuid
from django.db import models

# Create your models here.
class CreditCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.CharField("Portador", max_length=100)
    number = models.IntegerField("Número do cartão")
    valid_until = models.DateField("Válido até")
    cvv = models.IntegerField("Código de verificação")
    class Meta:  
        db_table = "credit_card"

