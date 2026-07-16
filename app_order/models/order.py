from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    product = models.ManyToManyField("app_product.Product", blank=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        default="pending",
        choices=[("pending", "Pendente"), ("paid", "Pago"), ("canceled", "Cancelado")],
    )

    def __str__(self):
        return f"Pedido #{self.id} - Usuário: {self.user.username}"
