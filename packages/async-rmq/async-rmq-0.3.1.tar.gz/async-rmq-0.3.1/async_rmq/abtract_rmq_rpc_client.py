import asyncio
import uuid
from abc import ABCMeta, abstractmethod
from typing import MutableMapping
import async_rmq.rmq_functions as rmq_functions
from aio_pika import Message
from aio_pika.abc import (
    AbstractChannel, AbstractConnection, AbstractIncomingMessage, AbstractQueue,
)


class RpcClient(metaclass=ABCMeta):
    connection: AbstractConnection
    channel: AbstractChannel
    callback_queue: AbstractQueue
    loop: asyncio.AbstractEventLoop

    def __init__(self) -> None:
        self.futures: MutableMapping[str, asyncio.Future] = {}
        self.loop = asyncio.get_running_loop()

    async def connect(self,
                      resp_queue_name,
                      resp_exchange_name,
                      pub_queue_name,
                      pub_exchange_name,
                      host,
                      port,
                      login,
                      password,
                      vhost,
                      content_type: str = "application/json") -> "RpcClient":
        self.connection = await rmq_functions.get_rmq_connection(host, port, login, password, vhost, self.loop)
        self.channel = await self.connection.channel()
        self.callback_queue = await self.channel.declare_queue(resp_queue_name, exclusive=True)
        self.pub_queue_name = pub_queue_name
        self.pub_exchange = await self.channel.get_exchange(pub_exchange_name)
        await self.callback_queue.bind(resp_exchange_name, resp_queue_name)
        await self.callback_queue.consume(self.on_response, no_ack=True)
        self.content_type = content_type

        return self

    async def on_response(self, message: AbstractIncomingMessage) -> None:

        if message.correlation_id is None:
            print(f"Bad message {message!r}")
            return

        future: asyncio.Future = self.futures.pop(message.correlation_id)
        future.set_result(message.body)

    async def call(self, *args) -> int:
        correlation_id = str(uuid.uuid4())
        future = self.loop.create_future()
        self.futures[correlation_id] = future

        msg_data = self.prepare_msg_data(*args)

        await self.pub_exchange.publish(
            Message(
                msg_data,
                content_type=self.content_type,
                correlation_id=correlation_id,
                reply_to=self.callback_queue.name,
            ),
            routing_key=self.pub_queue_name
        )

        return await future

    @abstractmethod
    def prepare_msg_data(self, args):
        raise NotImplementedError()
