from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class Event(PostApiRequest, GetApiRequest):
    """
    Events are our way of letting you know when something interesting happens in your workspace.
    When an interesting events occurs, we create a new Event object. For example, when a payment succeeds,
    we create a payment.succeeded event; and when a message delivery fails, we create an message.failed event.
    Note that many API requests may cause multiple events to be created. For example, if you create a new message,
    you will receive both a message.sent event and either a message.failed or message.delivered event.
    Events occur when the state of another API resource changes. The state of that resource at the time of the change is
    embedded in the event's data field. For example, a message.sent event will contain a message, and a payment.failed event will contain a payment.
    As with other API resources, you can use endpoints to retrieve an individual event or a list of events from the API.
    We also have a separate webhooks API for sending the Event objects directly to an endpoint on your server. Webhooks are managed in your workspace,
    and our Using Webhooks guide will help you get setup.
    NOTE: Access to events through the Retrieve Event API is guaranteed only for the last 30 days.
    """

    @classmethod
    def get_events(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get events

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/events",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_event(cls, event, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get event

        :param event:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/events/{event}".format(event=event),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
