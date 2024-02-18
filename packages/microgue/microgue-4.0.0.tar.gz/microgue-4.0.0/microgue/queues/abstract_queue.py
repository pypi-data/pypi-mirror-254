import boto3
import json
from ..loggers.logger import Logger

logger = Logger()


class DeleteFailed(Exception): pass  # noqa
class ReceiveFailed(Exception): pass  # noqa
class SendFailed(Exception): pass  # noqa
class QueueConnectionFailed(Exception): pass  # noqa


class AbstractQueue:
    # internal use only
    queue = None

    # extension required
    queue_url = None

    class Message:
        def __init__(self, message_data):
            self.id = message_data["ReceiptHandle"]
            self.data = json.loads(message_data["Body"])

    def __init__(self, *args, **kwargs):
        logger.debug(f"{self.__class__.__name__}.__init__", priority=2)
        logger.debug(f"AbstractQueue.queue: {AbstractQueue.queue}")
        try:
            logger.debug("connecting to sqs", priority=3)
            logger.debug(f"queue_url: {self.queue_url}")
            if AbstractQueue.queue is None:
                # share the queue connection at the application level
                AbstractQueue.queue = boto3.client("sqs")
                logger.debug("successfully connected to sqs", priority=3)
            else:
                logger.debug("using existing connection to sqs", priority=3)
        except Exception as e:
            logger.error(f"{self.__class__.__name__}.__init__ - error", priority=3)
            logger.error(f"{e.__class__.__name__}: {str(e)}")
            raise QueueConnectionFailed(str(e))

    def send(self, message):
        logger.debug(f"{self.__class__.__name__}.send", priority=2)
        if type(message) is dict:
            message = json.dumps(message)
        try:
            self.queue.send_message(
                QueueUrl=self.queue_url,
                MessageBody=message
            )
            logger.error(f"{self.__class__.__name__}.send - success", priority=3)
        except Exception as e:
            logger.error(f"{self.__class__.__name__}.send - error", priority=3)
            logger.error(f"{e.__class__.__name__}: {str(e)}")
            raise SendFailed(str(e))
        return True

    def receive(self, max_number_of_messages=1, visibility_timeout=1, wait_time=1):
        logger.debug(f"{self.__class__.__name__}.receive", priority=2)
        logger.debug(f"max_number_of_messages: {max_number_of_messages}")
        logger.debug(f"visibility_timeout: {visibility_timeout}")
        logger.debug(f"wait_time: {wait_time}")

        try:
            response = self.queue.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=max_number_of_messages,
                VisibilityTimeout=visibility_timeout,
                WaitTimeSeconds=wait_time
            )
        except Exception as e:
            logger.error(f"{self.__class__.__name__}.receive - error", priority=3)
            logger.error(f"{e.__class__.__name__}: {str(e)}")
            raise ReceiveFailed(str(e))

        response_messages = response.get("Messages", [])
        messages = []
        for i in range(len(response_messages)):
            try:
                message = self.Message(response_messages[i])
                messages.append(message)
            except:  # noqa
                pass
        number_of_messages_received = len(messages)
        logger.debug(f"number_of_messages_received: {number_of_messages_received}")
        logger.debug(f"messages: {messages}")
        return messages

    def delete(self, message):
        logger.debug(f"{self.__class__.__name__}.delete", priority=2)
        logger.debug(f"message.id: {message.id}")
        logger.debug(f"message.data: {message.data}")

        try:
            self.queue.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=message.id
            )
        except Exception as e:
            logger.error(f"{self.__class__.__name__}.delete - error", priority=3)
            logger.error(f"{e.__class__.__name__}: {str(e)}")
            raise DeleteFailed(str(e))

        return True
