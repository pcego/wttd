from django.db import models
from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):

    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('E-Mail', blank=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('Criado Em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscricoes'
        verbose_name = 'inscricao'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
