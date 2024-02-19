from django.db.models.signals import post_save, pre_delete

from whisperer.events import WhispererEvent, registry
from whisperer.tasks import deliver_event
from whisperer.tests.models import Order
from whisperer.tests.serializers import OrderSerializer


class OrderCreateEvent(WhispererEvent):
    serializer_class = OrderSerializer
    event_type = 'order-created'
    queryset = Order.objects.select_related(
        "customer",
        "address",
    ).all()


class OrderUpdateEvent(WhispererEvent):
    serializer_class = OrderSerializer
    event_type = 'order-updated'


class OrderDeleteEvent(WhispererEvent):
    serializer_class = OrderSerializer
    event_type = 'order-deleted'


registry.register(OrderCreateEvent)
registry.register(OrderUpdateEvent)
registry.register(OrderDeleteEvent)


def signal_receiver(instance, created=False, **kwargs):
    if created:
        deliver_event(instance, 'order-created')
    else:
        deliver_event(instance, 'order-updated')


def signal_delete_receiver(sender, instance, created=False, **kwargs):
    order_data = OrderSerializer(instance).data

    deliver_event(order_data, 'order-deleted')


post_save.connect(signal_receiver, Order)
pre_delete.connect(signal_delete_receiver, sender=Order)
