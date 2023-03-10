from django.http import HttpResponse


class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles Generic, Unexpected or Unkwon Webhook Event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handels Stripe Payment Succeeded Webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles Stripe Payment Intent & Payment Failed Webhooks
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
