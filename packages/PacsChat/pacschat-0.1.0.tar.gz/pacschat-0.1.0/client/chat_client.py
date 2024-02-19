import asyncio
import concurrent.futures
from typing import Protocol


class InputWindow(Protocol):
    def refresh(self) -> None: ...

    def get_input_message(self) -> bytes: ...


class ChatWindow(Protocol):
    def add_message(self, message: str): ...


class ChatClient:
    def __init__(self, addr: str, port: int) -> None:
        self.addr = addr
        self.port = port

    async def _send_str(self, message: bytes):
        try:
            self.writer.write(message)
            await self.writer.drain()
            return True
        except OSError as err:
            print("Sending message failed with the exception: ", err.__repr__())
            return False

    async def connect(self):
        try:
            self.reader, self.writer = await asyncio.open_connection(
                self.addr, self.port
            )
            name = input((await self.reader.read(100)).decode())
            print("name: ", name)
            return await self._send_str(name.encode())

        except OSError as err:
            print("Connecting to server failed with the exception: ", err.__repr__())
            return False

    async def send_messages(self, input_window: InputWindow):
        while True:
            input_window.refresh()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                message = await asyncio.get_event_loop().run_in_executor(
                    executor, input_window.get_input_message
                )

            await self._send_str(message)

    async def update_chat(self, chat_window: ChatWindow):
        while True:
            message = (await self.reader.readline()).decode().strip()
            chat_window.add_message(message)

    async def load_history(self, chat_window: ChatWindow) -> bool:
        try:
            num_messages = int((await self.reader.readline()).decode())
            for _ in range(num_messages):
                message = (await self.reader.readline()).decode().strip()
                chat_window.add_message(message)
            return True

        except OSError as err:
            print("Loading history failed with the exception: ", err.__repr__())
            return False

    async def cleanup(self):
        self.writer.close()
        return await self.writer.wait_closed()

    async def run(self, chat_window: ChatWindow, input_window: InputWindow):
        if not await self.connect():
            return

        if not await self.load_history(chat_window):
            return

        try:
            send_task = asyncio.create_task(self.send_messages(input_window))
            update_task = asyncio.create_task(self.update_chat(chat_window))
            await asyncio.gather(send_task, update_task)

        except Exception as e:
            print("Connection to the server was lost.", e.__repr__())

        finally:
            print("closing the connection.")
            await self.cleanup()
