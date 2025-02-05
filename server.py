import asyncio
from aiosmtpd.controller import Controller

class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        print("New email received:")
        print(envelope.content.decode("utf8", errors="replace"))
        return "250 Message accepted"

controller = Controller(CustomHandler(), hostname="localhost", port=1025)
controller.start()
input("Press Enter to stop server...\n")
controller.stop()