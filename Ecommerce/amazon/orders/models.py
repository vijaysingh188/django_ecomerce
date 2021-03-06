import math
from django.db import models
from carts.models import Cart
from amazon.utilis import unique_order_id_generator
from django.db.models.signals import pre_save,post_save
from decimal import Decimal

ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('shipped','Shipped'),
    ('paid','Paid'),
    ('refunded','Refunded')
)


class Order(models.Model):
    order_id = models.CharField(max_length=120,blank=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120,default='created',choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99,decimal_places=2,max_digits=10)
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        new_total = math.fsum([cart_total, shipping_total])
        formatted_total = format(new_total, '.2f')
        self.total = formatted_total
        self.save()
        return new_total


def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id,sender=Order)

def post_save_cart_total(sender,instance,created,*args,**kwargs):
    if not created:
        cart_obj = instance
        print(type(instance))
        print(instance,'insta')
        cart_total = cart_obj.total
        print(cart_total,'cart_total')
        cart_id = cart_obj.id
        print(cart_id,'cart_id')
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count()==1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total,sender=Cart)

def post_save_order(sender,instance,created,*args,**kwargs):   #if order is already created
    if created:

        instance.update_total()



post_save.connect(post_save_order,sender=Order)







