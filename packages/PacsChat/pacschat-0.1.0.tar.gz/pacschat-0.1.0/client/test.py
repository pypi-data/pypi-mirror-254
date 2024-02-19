import asyncio
import concurrent.futures
import curses

import _curses


class ChatCLient:
    def __init__(self, addr: str, port: int) -> None:
        self.addr = addr
        self.port = port

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.addr, self.port)
        self.welcome_message = await self.reader.read(100)

        name = input(self.welcome_message.decode())
        self.writer.write(name.encode())
        await self.writer.drain()

    def create_chat_window(self, stdscr: "_curses._CursesWindow"):
        max_y, self.max_x = stdscr.getmaxyx()
        self.max_x = self.max_x - 2

        stdscr.erase()
        stdscr.refresh()

        self.input_height, self.chat_height = 3, max_y - 4

        self.input_window = curses.newwin(
            self.input_height, self.max_x, self.chat_height + 1, 0
        )
        self.input_window.border()
        self.input_window.refresh()

        self.chat_window = curses.newwin(self.chat_height - 1, self.max_x - 2, 1, 1)
        self.chat_window.scrollok(True)
        self.chat_window.refresh()

        self.border_window = curses.newwin(self.chat_height, self.max_x, 0, 0)
        self.border_window.border()
        self.border_window.hline(self.chat_height - 1, 1, "-", self.max_x - 2)
        self.border_window.refresh()

    async def load_history(self):
        num_messages = int((await self.reader.readline()).decode())
        for _ in range(num_messages):
            message = (await self.reader.readline()).decode().strip()
            self.print_msg(message)

    def print_msg(self, message):
        self.border_window.erase()
        self.border_window.border()
        self.border_window.refresh()

        self.chat_window.scroll()
        self.chat_window.addstr(self.chat_height - 3, 1, message)
        self.chat_window.refresh()

        self.border_window.hline(self.chat_height - 1, 1, "-", self.max_x - 2)
        self.border_window.refresh()

    async def update_chat(self):
        while True:
            message = (await self.reader.readline()).decode().strip()
            self.print_msg(message)

    def get_input(self):
        return self.input_window.getstr(1, 3).decode()

    async def send_messages(self):
        while True:
            self.input_window.refresh()
            self.input_window.border()
            self.input_window.addstr(1, 1, "> ")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                message = await asyncio.get_event_loop().run_in_executor(
                    executor, self.get_input
                )

            self.input_window.clear()
            self.writer.write(f"{message}\n".encode())
            await self.writer.drain()

    async def run(self, stdscr):
        await self.connect()
        self.create_chat_window(stdscr)
        await self.load_history()

        # Create tasks for each coroutine
        send_task = asyncio.create_task(self.send_messages())
        update_task = asyncio.create_task(self.update_chat())

        # Use asyncio.gather to run the tasks concurrently
        await asyncio.gather(send_task, update_task)


def main():
    client = ChatCLient("localhost", 8081)
    asyncio.run(curses.wrapper(client.run))


if __name__ == "__main__":
    main()
