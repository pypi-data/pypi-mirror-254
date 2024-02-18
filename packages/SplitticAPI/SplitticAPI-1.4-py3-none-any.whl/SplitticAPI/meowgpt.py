import httpx

class ChatModule:
    def __init__(self, api_key, chat_id=None):
        self.api_key = api_key
        self.chat_id = chat_id if chat_id else self.generate_chat_id()

    @classmethod
    def initialize(cls, api_key):
        """
        Initialize the ChatModule with the global API key.
        """
        cls.global_api_key = api_key

    @staticmethod
    def generate_chat_id():
        """
        Generate a unique chat ID.
        """
        import uuid
        return str(uuid.uuid4())

    async def async_reply(self, message):
        """
        Send an asynchronous message to the server and get a reply.
        """
        if self.api_key is None:
            error_message = "\033[91mError: API key not set. Please set the API key before using the ChatModule.\033[0m"
            print(error_message)
            raise ValueError(error_message)

        endpoint = "https://api.splittic.app/api/reply"
        params = {
            "auth": self.api_key,
            "message": message,
            "chatid": self.chat_id,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint, params=params, timeout=99)

            if response.status_code == 200:
                return response.text
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

    def reply(self, message):
        """
        Send a synchronous message to the server and get a reply.
        """
        import asyncio

        # Run the asynchronous method in an event loop
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.async_reply(message))

    @classmethod
    def create_chat(cls, api_key):
        """
        Create a new ChatModule instance with a unique chat ID.
        """
        return cls(api_key)
