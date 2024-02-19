from whisperer.exceptions import WebhookAlreadyRegistered
from whisperer.models import EventQueue, Webhook


class WebhookService(object):
    def register_webhook(self, user, *args, **kwargs):
        event_type = kwargs.get('event_type')
        target_url = kwargs.get('target_url')
        try:
            Webhook.objects.get(user=user, target_url=target_url, event_type=event_type)
            raise WebhookAlreadyRegistered()
        except Webhook.DoesNotExist:
            pass
        webhook = Webhook(user=user)
        for attr, value in kwargs.items():
            setattr(webhook, attr, value)
        webhook.save()
        return webhook

    def update_webhook(self, webhook, user, *args, **kwargs):
        webhook.user = user
        target_url = kwargs.get('target_url', webhook.target_url)
        event_type = kwargs.get('event_type', webhook.event_type)
        try:
            Webhook.objects.exclude(id=webhook.id).get(
                user=user, target_url=target_url, event_type=event_type
            )
            raise WebhookAlreadyRegistered()
        except Webhook.DoesNotExist:
            pass

        for attr, value in kwargs.items():
            setattr(webhook, attr, value)
        webhook.save(update_fields=kwargs.keys())
        return webhook

    def delete_webhook(self, webhook):
        webhook.is_active = False
        webhook.save(update_fields=['is_active'])


class EventQueueService(object):
    @staticmethod
    def create_event_queue(
        hook_id,
        event_type,
        app_label=None,
        model_name=None,
        instance_pk=None,
        instance_dict=None,
    ):
        if instance_dict is None:
            instance_dict = {}
        instance = EventQueue(
            hook_id=hook_id,
            event_type=event_type,
            app_label=app_label,
            model_name=model_name,
            instance_pk=instance_pk,
            instance_dict=instance_dict,
        )
        instance.save()
        return instance
