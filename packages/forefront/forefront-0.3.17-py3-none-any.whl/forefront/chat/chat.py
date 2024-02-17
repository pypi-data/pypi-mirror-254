import requests
import json

class Completions:
    def __init__(self, client):
        self.client = client
        self.default_model = client.default_model
        self.uri='/v1/chat/completions'

    def create(self, model=None, messages = [], **kwargs):
        """
        Create a completion using the chat API.

        :param messages: A list of message dicts with 'role' and 'content'.
        :param kwargs: Additional parameters for the API (e.g., model, temperature).
        :return: The API's response as JSON.
        """
        m = model if model else self.default_model

        # assert model is present
        assert m is not None, "Model is required."

        # assert messages is present
        assert messages is not None, "Messages are required."

        
        payload = {
            "model": m,
            "messages": messages,
            **kwargs
        }

        stream = kwargs.get('stream', False)

        # if stream:
        #     return self._create_stream(payload)
        # else:
        return self._create_non_stream(payload)

    def _create_non_stream(self, payload):
        response = requests.post(
            self.client.api_url + self.uri,
            headers=self.client.headers,
            json=payload
        )
        if response.status_code == 200:
            resp = response.json()
            resp['message'] = resp['choices'][0]['message']
            return Completion(resp)

    # async def _create_stream(self, payload):
    #     async with aiohttp.ClientSession() as session:
    #         async with session.post(
    #             self.client.api_url,
    #             headers=self.client.headers,
    #             json=payload
    #         ) as response:
    #             if response.status:
    #                 async for line in response.content:
    #                     if line:
    #                         try:
    #                             message = json.loads(line.decode('utf-8'))
    #                             if 'choices' in message:
    #                                 yield message
    #                         except json.JSONDecodeError:
    #                             pass



class Chat:
    def __init__(self, client):
        self.completions = Completions(client)
class Completion:
    def __init__(self, data):
        self.choices = [Choice(choice) for choice in data['choices']]
        self.usage = Usage(data['usage'])
        self.message = data['message']['content']

class Choice:
    def __init__(self, data):
        self.message = data['message']
        self.role = data['role']

class Usage:
    def __init__(self, data):
        self.total_tokens = data['total_tokens']
        self.input_tokens = data['input_tokens']
        self.output_tokens = data['output_tokens']
