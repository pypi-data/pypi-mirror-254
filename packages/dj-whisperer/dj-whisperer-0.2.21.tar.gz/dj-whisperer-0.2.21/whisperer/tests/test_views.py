from collections import namedtuple

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from whisperer.models import EventQueue, Webhook, WebhookEvent
from whisperer.resources.views import (
    EventQueueViewSet,
    WebhookEventViewSet,
    WebhookViewSet,
)


class WebhookViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = mommy.make(User, username="test_admin_user", is_superuser=True)
        self.dummy_user = mommy.make(User, username="dummy_user", is_superuser=False)
        dummy_user_b = mommy.make(User, username="dummy_userb", is_superuser=False)
        mommy.make(
            Webhook,
            user=self.dummy_user,
            retry_countdown_config={},
            additional_headers={},
            config={},
            _quantity=5,
        )
        mommy.make(
            Webhook,
            user=dummy_user_b,
            retry_countdown_config={},
            additional_headers={},
            config={},
            _quantity=5,
        )

    def test_list_with_admin_user(self):
        request = namedtuple("Request", ["user"])
        view = WebhookViewSet(request=request(user=self.user))
        qs = view.get_queryset()
        self.assertEqual(qs.count(), 10)

    def test_list_with_regular_user(self):
        request = namedtuple("Request", ["user"])
        view = WebhookViewSet(request=request(user=self.dummy_user))
        qs = view.get_queryset()
        self.assertEqual(qs.count(), 5)

    @override_settings(ROOT_URLCONF='whisperer.urls')
    def test_get_registry(self):
        response = self.client.get(reverse("webhook-get-registry"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WebhookEventViewSetTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username="test_admin_user", is_superuser=True)
        self.dummy_user = mommy.make(User, username="dummy_user", is_superuser=False)
        dummy_user_b = mommy.make(User, username="dummy_userb", is_superuser=False)
        webhook_a = mommy.make(
            Webhook,
            user=self.dummy_user,
            retry_countdown_config={},
            additional_headers={},
            config={},
        )
        webhook_b = mommy.make(
            Webhook,
            user=dummy_user_b,
            retry_countdown_config={},
            additional_headers={},
            config={},
        )
        mommy.make(WebhookEvent, webhook=webhook_a, request_payload={}, _quantity=5)
        mommy.make(WebhookEvent, webhook=webhook_b, request_payload={}, _quantity=5)

    def test_list_with_admin_user(self):
        request = namedtuple("Request", ["user"])
        view = WebhookEventViewSet(request=request(user=self.user))
        qs = view.get_queryset()
        self.assertEqual(qs.count(), 10)

    def test_list_with_regular_user(self):
        request = namedtuple("Request", ["user"])
        view = WebhookEventViewSet(request=request(user=self.dummy_user))
        qs = view.get_queryset()
        self.assertEqual(qs.count(), 5)


class EventQueueViewSetTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username="test_admin_user", is_superuser=True)
        mommy.make(EventQueue, event_type="order-created")
        mommy.make(EventQueue, event_type="product-updated")

    def test_list_with_admin_user(self):
        request = namedtuple("Request", ["user"])
        view = EventQueueViewSet(request=request(user=self.user))
        qs = view.get_queryset()
        self.assertEqual(qs.count(), 2)
