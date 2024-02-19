import os
import unittest
from unittest import skipIf
from unittest.mock import MagicMock, patch
from llm_wrap.llms import gpt_api
import openai
import httpx

USE_ACTUAL_LLM_API = False
def skip_if_no_api():
    return skipIf(not USE_ACTUAL_LLM_API, "Skipping this test because USE_ACTUAL_LLM_API is False")

class TestGptApi(unittest.TestCase):

    def setUp(self):
        self.original_is_azure = os.getenv('IS_AZURE')
        self.original_production = os.getenv('LLM_WRAP_PRODUCTION')
        os.environ['IS_AZURE'] = 'False'
        os.environ['LLM_WRAP_PRODUCTION'] = 'False'

    def tearDown(self):
        if self.original_is_azure is None:
            os.environ.pop('IS_AZURE', None)
        else:
            os.environ['IS_AZURE'] = self.original_is_azure

        if self.original_production is None:
            os.environ.pop('LLM_WRAP_PRODUCTION', None)
        else:
            os.environ['LLM_WRAP_PRODUCTION'] = self.original_production

    @skip_if_no_api()
    def test_generate_ai_stream(self):
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = ''
        for char in gpt_api.generate_ai_stream(messages, is_json=False):
            response += char
        self.assertIsInstance(response, str)

    @skip_if_no_api()
    def test_generate_ai_stream_empty_messages(self):
        messages = []
        with self.assertRaises(Exception):
            next(gpt_api.generate_ai_stream(messages))

    @skip_if_no_api()
    def test_generate_ai_stream_invalid_message_format(self):
        messages = [{'role': 'user'}]
        with self.assertRaises(Exception):
            next(gpt_api.generate_ai_stream(messages))

    @skip_if_no_api()
    def test_generate_ai_stream_json(self):
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Give me 50 random digits in JSON format'}]
        response = ''
        for char in gpt_api.generate_ai_stream(messages, is_json=True):
            response += char
        self.assertIsInstance(response, str)
        self.assertTrue(response.startswith('{') and response.endswith('}'))

    @skip_if_no_api()
    def test_chatCompletion(self):
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = gpt_api.chatCompletion(messages)
        response_txt = response.choices[0].message.content
        self.assertIsInstance(response_txt, str)

    @skip_if_no_api()
    def test_chatCompletion_invalid_message_format(self):
        messages = [{'role': 'user'}]
        with self.assertRaises(Exception):
            gpt_api.chatCompletion(messages)

    @patch('openai.resources.chat.Completions.create')
    def test_generate_ai_stream_api_error(self, mock_create):
        mock_create.side_effect = Exception('API error')
        messages = [{'role': 'user', 'content': 'Hello, AI!'}]
        with self.assertRaises(Exception):
            next(gpt_api.generate_ai_stream(messages))

    @patch('openai.resources.chat.Completions.create')
    def test_chatCompletion_api_error(self, mock_create):
        mock_create.side_effect = Exception('API error')
        messages = [{'role': 'user', 'content': 'Hello, AI!'}]
        with self.assertRaises(Exception):
            gpt_api.chatCompletion(messages)

import os
import unittest
from unittest.mock import patch
from llm_wrap.llms import gpt_api

class TestGptApi2(unittest.TestCase):

    def setUp(self):
        self.original_is_azure = os.getenv('IS_AZURE')
        self.original_production = os.getenv('LLM_WRAP_PRODUCTION')

    def tearDown(self):
        if self.original_is_azure is None:
            os.environ.pop('IS_AZURE', None)
        else:
            os.environ['IS_AZURE'] = self.original_is_azure

        if self.original_production is None:
            os.environ.pop('LLM_WRAP_PRODUCTION', None)
        else:
            os.environ['LLM_WRAP_PRODUCTION'] = self.original_production

    @skip_if_no_api()
    def test_generate_ai_stream_production(self):
        os.environ['IS_AZURE'] = 'False'
        os.environ['LLM_WRAP_PRODUCTION'] = 'True'
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = ''
        for char in gpt_api.generate_ai_stream(messages, is_json=False):
            response += char
        self.assertIsInstance(response, str)

    @skip_if_no_api()
    def test_chatCompletion_azure(self):
        os.environ['IS_AZURE'] = 'True'
        os.environ['LLM_WRAP_PRODUCTION'] = 'True'
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = gpt_api.chatCompletion(messages)
        response_txt = response.choices[0].message.content
        self.assertIsInstance(response_txt, str)

    @skip_if_no_api()
    def test_chatCompletion_openAI(self):
        os.environ['IS_AZURE'] = 'False'
        os.environ['LLM_WRAP_PRODUCTION'] = 'True'
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = gpt_api.chatCompletion(messages)
        response_txt = response.choices[0].message.content
        self.assertIsInstance(response_txt, str)

    @skip_if_no_api()
    def test_chatCompletion_openAI_production(self):
        os.environ['IS_AZURE'] = 'True'
        os.environ['LLM_WRAP_PRODUCTION'] = 'True'
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = gpt_api.chatCompletion(messages)
        response_txt = response.choices[0].message.content
        self.assertIsInstance(response_txt, str)

    @skip_if_no_api()
    def test_chatCompletion_azure_dev(self):
        os.environ['IS_AZURE'] = 'True'
        os.environ['LLM_WRAP_PRODUCTION'] = 'False'
        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = gpt_api.chatCompletion(messages)
        response_txt = response.choices[0].message.content
        self.assertIsInstance(response_txt, str)

from unittest.mock import MagicMock
from llm_wrap.llms import gpt_api

class TestGptApi3(unittest.TestCase):

    @patch('openai.resources.chat.Completions.create')
    def test_generate_ai_stream(self, mock_create):
        # Mock the response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].delta = MagicMock()
        mock_response.choices[0].delta.content = "test content"
        mock_response.choices[0].finish_reason = 'stop'
        mock_create.return_value = [mock_response]

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = ''
        for char in gpt_api.generate_ai_stream(messages, is_json=False):
            response += char

        self.assertEqual(response, "test content")

    @patch('openai.resources.chat.Completions.create')
    def test_generate_ai_stream_no_choices(self, mock_create):
        # Mock the response
        mock_response = MagicMock()
        mock_response.choices = []
        mock_create.return_value = [mock_response]

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        with self.assertRaises(StopIteration):
            next(gpt_api.generate_ai_stream(messages, is_json=False))

    @patch('openai.resources.chat.Completions.create')
    def test_generate_ai_stream_no_delta(self, mock_create):
        # Mock the response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].delta = None
        mock_response.choices[0].finish_reason = 'stop'
        mock_create.return_value = [mock_response]

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        with self.assertRaises(StopIteration):
            next(gpt_api.generate_ai_stream(messages, is_json=False))

from unittest.mock import MagicMock, patch, ANY
from llm_wrap.llms import gpt_api

class TestGptApi4(unittest.TestCase):

    @patch('openai.resources.chat.Completions.create')
    def test_chatCompletion_with_max_tokens(self, mock_create):
        # Mock the response
        mock_response = MagicMock()
        mock_create.return_value = mock_response

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = gpt_api.chatCompletion(messages, max_tokens=100)

        # Check that the create method was called with the correct max_tokens parameter
        mock_create.assert_called_once_with(
            messages=messages,
            temperature=0.5,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            model=ANY,
            max_tokens=100
        )

        # Check that the response is the mock response
        self.assertEqual(response, mock_response)

from unittest.mock import MagicMock, patch
from llm_wrap.llms import gpt_api

class TestGptApiRetry(unittest.TestCase):

    @patch('openai.resources.chat.Completions.create')
    def test_chatCompletion_retry_success(self, mock_create):
        # Mock the response
        mock_response = MagicMock()
        mock_create.side_effect = [Exception('API error'), mock_response]

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        response = gpt_api.chatCompletion(messages, retries=1)

        # Check that the create method was called twice (one failure, one success)
        self.assertEqual(mock_create.call_count, 2)

        # Check that the response is the mock response
        self.assertEqual(response, mock_response)

    @patch('openai.resources.chat.Completions.create')
    def test_chatCompletion_retry_failure(self, mock_create):
        # Mock the response
        mock_create.side_effect = Exception('API error')

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        with self.assertRaises(Exception):
            gpt_api.chatCompletion(messages, retries=1)

        # Check that the create method was called twice (two failures)
        self.assertEqual(mock_create.call_count, 2)

    @patch('openai.resources.chat.Completions.create')
    def test_chatCompletion_no_retry(self, mock_create):
        # Mock the response
        mock_create.side_effect = Exception('API error')

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        with self.assertRaises(Exception):
            gpt_api.chatCompletion(messages)

        # Check that the create method was called once
        self.assertEqual(mock_create.call_count, 1)

    @patch('openai.resources.chat.Completions.create')
    def test_chatCompletion_rate_limit_error(self, mock_create):
        # Mock the request and response
        mock_request = httpx.Request('POST', 'http://testserver/')
        mock_response = httpx.Response(429, request=mock_request)
        mock_create.side_effect = openai.RateLimitError('Rate limit exceeded', response=mock_response, body=None)

        messages = [{"role": "system", "content": "You are a helpful assistant."},{'role': 'user', 'content': 'Hello, AI!'}]
        with self.assertRaises(openai.RateLimitError):
            gpt_api.chatCompletion(messages, retries=1)

        # Check that the create method was called once
        self.assertEqual(mock_create.call_count, 1)

if __name__ == '__main__':
    unittest.main()
