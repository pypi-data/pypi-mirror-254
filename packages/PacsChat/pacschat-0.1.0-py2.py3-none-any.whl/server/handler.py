import asyncio
import random
import string

from server.stores import RecentMessagesStore, StreamWriterStore

ID_LEN = 5


class RequestHandler:
    def __init__(self, history: int):
        self.writers_store = StreamWriterStore()
        self.recent_messages_store = RecentMessagesStore(history)

    async def callback(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ):
        id = None
        try:
            writer.write("Hello from py-chatter 🤩. Please Enter your name: ".encode())
            await writer.drain()

            name = (await reader.read(100)).decode().strip()
            id = (
                name
                + "-"
                + "".join(random.choice(string.ascii_letters) for i in range(ID_LEN))
            )
            print(f"New client connected with id: {id}")

            await self.writers_store.add_writer(writer)
            await self.recent_messages_store.send_recent_messages(writer)

            while True:
                message = (await reader.readline()).decode().strip()
                if message == "":
                    continue

                if message == "exit":
                    writer.write("Bye bye 👋👋".encode())
                    await writer.drain()
                    break

                print(f"New message from {id}: {message}")
                await self.recent_messages_store.add_message(f"{id}: {message}")
                await self.writers_store.broadcast(f"{id}: {message}")

        except asyncio.CancelledError as e:
            print(f"cancelled error occurred, details: ", e.__repr__())

        finally:
            await self.writers_store.remove_writer(writer)
            writer.close()
            await writer.wait_closed()
