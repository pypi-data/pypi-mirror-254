SplitticAPI
===========

The SplitticAPI Library provides a convenient Python interface for
interacting with the Splittic API, enabling users to seamlessly
integrate Splittic's AI functionality into their applications. The
library is designed to be user-friendly and versatile, supporting both
asynchronous and synchronous programming.

Installation
------------

To install the SplitticAPI Library, use the following command:

.. code:: bash

   pip install SplitticAPI

Getting Started
---------------

1. **Obtain API Key:**

   -  Visit the `FreeAI Discord
      server <https://discord.gg/W4bwWX3HJx>`__.
   -  Retrieve your API key from the #api channel.

2. **Initialize ChatModule:**

   -  Import the ``ChatModule`` class from ``SplitticAPI.meowgpt``.
   -  Set the global API key using ``ChatModule.initialize(api_key)``.

3. **Create a Chat Instance:**

   -  Create a new chat instance using
      ``ChatModule.create_chat(api_key)``.
   -  Each instance automatically generates a unique chat ID.

4. **Send Messages:**

   -  Use the ``reply(message)`` method to send a synchronous message
      and receive a reply.
   -  Optionally, use the ``async_reply(message)`` method for
      asynchronous interactions.

5. **Generate Images with DiffusionModule:**

   -  Import the ``DiffusionModule`` class from
      ``SplitticAPI.interdiffusion``.
   -  Initialize ``DiffusionModule`` with your API key.
   -  Use the ``generate()`` method for synchronous image generation.
   -  Alternatively, use ``async_generate()`` for asynchronous image
      generation.
   -  The generated image is saved as “output.png” by default.

Example
-------

.. code:: python

   from SplitticAPI.meowgpt import ChatModule
   from SplitticAPI.interdiffusion import DiffusionModule

   # Set the global API key
   api_key = "your_api_key_here"
   ChatModule.initialize(api_key)

   # Create a ChatModule instance with a unique chat ID
   chat_instance = ChatModule.create_chat(api_key)

   # Send a synchronous message and get a reply
   def main():
       reply = chat_instance.reply("Hi")
       print(reply)

       # Generate an image synchronously
       diffusion_module = DiffusionModule(api_key)
       diffusion_module.generate()

   # Run the program
   if __name__ == "__main__":
       main()

For more detailed information, refer to the `official Splittic API
documentation <https://api.splittic.app>`__.

License
-------

This library is released under the `MIT
License <https://github.com/CutyCat2000/splitticapi/blob/main/LICENSE>`__.
Feel free to use, modify, and distribute it according to your needs.
