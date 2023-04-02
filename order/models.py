from django.db import models
from supermegasite.models import Product

# Create your models here.


class Order(models.Model):
    ACCEPTED = 'ПРИНЯТ'
    CHOICES = [
        ('ACCEPTED', 'ПРИНЯТ'),
        ('IN_PROCESSING', 'В ОБРАБОТКЕ'),
        ('SENT', 'ОТПРАВЛЕН'),
        ('RECEIVED', 'ПОЛУЧЕН')
    ]
    fullname = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    card_number = models.CharField(max_length=20)
    cvv = models.CharField(max_length=100)
    expiration = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.CharField(choices=CHOICES, verbose_name='Статус заказа', default=ACCEPTED, max_length=55)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
