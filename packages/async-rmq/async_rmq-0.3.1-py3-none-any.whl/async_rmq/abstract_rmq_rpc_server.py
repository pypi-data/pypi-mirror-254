import asyncio
from abc import ABCMeta, abstractmethod
import logging
from aio_pika import Message
from aio_pika.queue import Queue
from aio_pika.message import IncomingMessage
from aio_pika.exchange import Exchange
from aio_pika.abc import AbstractIncomingMessage

logger = logging.getLogger("async_rmq")


class RPCRabbitMQServer(metaclass=ABCMeta):
    def __init__(
            self,
            queue: Queue,
            resp_exchange: Exchange,
            iterator_timeout: int = 5,
            iterator_timeout_sleep: float = 5.0,
    ):
        self.queue = queue
        self.resp_exchange = resp_exchange
        self.iterator_timeout = iterator_timeout
        self.iterator_timeout_sleep = iterator_timeout_sleep
        self.consuming_flag = True

    async def run_rpc_server(self) -> None:

        async with self.queue.iterator() as queue_iterator:
            message: AbstractIncomingMessage

            async for message in queue_iterator:

                try:
                    async with message.process(requeue=False):
                        assert message.reply_to is not None
                        response = await self.process_message(message)

                        await self.resp_exchange.publish(
                            Message(
                                body=response,
                                correlation_id=message.correlation_id,
                            ),
                            routing_key=message.reply_to,
                        )

                except asyncio.exceptions.TimeoutError:
                    await self.on_finish()

                    if self.consuming_flag:
                        await asyncio.sleep(self.iterator_timeout_sleep)

                finally:
                    await self.on_finish()

    @abstractmethod
    async def process_message(self, orig_message: IncomingMessage):
        raise NotImplementedError()

    def stop_consuming(self):
        """Stops the consuming gracefully"""
        self.consuming_flag = False

    async def on_finish(self):
        """Called after the message consuming finished."""
        pass
