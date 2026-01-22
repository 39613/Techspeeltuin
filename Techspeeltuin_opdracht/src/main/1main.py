import asyncio
import websockets
import random

async def read_sensor():
    return round(random.uniform(10, 100), 2)

async def main():
    async with websockets.connect("ws://localhost:8080") as ws:
        while True:
            distance = await read_sensor()
            await ws.send(json.dumps({"distance": distance}))
            await asyncio.sleep(0.1)

asyncio.run(main())
