import httpx
import base64
import os

class DiffusionModule:
    def __init__(self, api_key, chat_id=None):
        self.api_key = api_key
        self.chat_id = chat_id

    @classmethod
    def initialize(cls, api_key):
        """
        Initialize the ChatModule with the global API key.
        """
        cls.global_api_key = api_key

    async def async_generate(self, prompt):
        """
        Send an asynchronous message to the server and save the reply as a PNG file in the output folder.
        """
        if self.api_key is None:
            error_message = "\033[91mError: API key not set. Please set the API key before using the ChatModule.\033[0m"
            print(error_message)
            raise ValueError(error_message)

        endpoint = "https://api.splittic.app/api/generate"
        params = {
            "auth": self.api_key,
            "prompt": prompt,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint, params=params, timeout=99)

            if response.status_code == 200:
                output_path = "output.png"
                with open(output_path, "wb") as output_file:
                    output_file.write(response.content)
                print(f"Image saved at: {output_path}")
            elif response.status_code == 401:
                error_message = "\033[91mError: Unauthorized. Please check your API key.\033[0m"
                print(error_message)
                raise ValueError(error_message)
            elif response.status_code == 500:
                error_message = "\033[91mError: Internal Server Error. Please try again later.\033[0m"
                print(error_message)
                raise ValueError(error_message)
            else:
                error_message = f"\033[91mError: Failed to get reply. Status code: {response.status_code}\033[0m"
                print(error_message)
                raise ValueError(error_message)

    def generate(self, prompt):
        """
        Send a synchronous message to the server and get a reply (InterDiffusion).
        """
        import asyncio
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.async_generate(prompt))