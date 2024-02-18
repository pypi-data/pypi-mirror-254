import asyncio
import json

import websockets


async def _websocket_client(client, connector, prompt, config):
    async with websockets.connect(client.ws_endpoint) as websocket:
        data = json.dumps(
            {
                "prompt": prompt.to_dict(),
                "config": config.to_dict(),
                "speck": client.to_dict(),
            }
        )
        # "connector": client.connector.to_dict()
        await websocket.send(data)

        try:
            print(
                f"[speck] LLM call ({config.provider}:{config.model}) sent to https://getspeck.ai/dash/debug"
            )
            # Wait for a response with a timeout of 5 seconds
            response = await asyncio.wait_for(websocket.recv(), timeout=1800)
            # print(f"Received from server: {json.loads(response)}")
            return json.loads(response)
        except asyncio.TimeoutError:
            # print("No response received from server within 5 seconds")
            pass
    return {}


def run_debug_websocket(client, connector, prompt, config):
    call = _websocket_client(client, connector, prompt, config)

    try:
        return asyncio.run(call)
    except RuntimeError:
        # Jupyter notebook async support
        try:
            import nest_asyncio

            nest_asyncio.apply()

            loop = asyncio.get_running_loop()
            task = loop.create_task(call)
            loop.run_until_complete(task)
            return task.result()
        except ImportError:
            print(
                "Jupyter requires nest_asyncio to be installed. Please install it with `pip install nest_asyncio`"
            )
            return {}


if __name__ == "__main__":
    # Call the synchronous function
    run_debug_websocket(None, None)
