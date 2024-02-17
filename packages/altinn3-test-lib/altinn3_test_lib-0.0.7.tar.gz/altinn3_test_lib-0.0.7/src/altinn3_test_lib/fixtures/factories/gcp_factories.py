import pytest
import google.cloud.pubsub_v1.subscriber.message
from google.pubsub_v1 import PubsubMessage
from google.cloud.pubsub_v1.subscriber.message import Message
from ssb_altinn3_util.models.altinn3_cloud_event import Altinn3CloudEvent


@pytest.fixture(scope="function")
def pubsub_message_factory():
    def create_pubsub_message(
        event: Altinn3CloudEvent,
    ) -> google.cloud.pubsub_v1.subscriber.message.Message:
        """Creates a PubSub message with an event as data"""
        # https://githubmemory.com/repo/googleapis/python-pubsub/issues/485 Create raw protubuf message
        pubsub_message = PubsubMessage.pb()(
            data=bytes(str(event.json()), "UTF-8"), message_id="42"
        )  # .pb() !
        # Convert to subscriber.Message
        return Message(pubsub_message, "0", 0, None)
    return create_pubsub_message
