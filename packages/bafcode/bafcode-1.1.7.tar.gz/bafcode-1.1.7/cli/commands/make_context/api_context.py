



class ApiContext:
    @staticmethod
    def snake_to_camel(word):
     formatted_word = word.replace('/', '_')
    
     return ''.join(x.capitalize() for x in formatted_word.split('_'))
    
    def format_word(word):
        formatted_word = word.replace('/', '_')
        return formatted_word
    

    def context(api_name):
        camel_case_name = ApiContext.snake_to_camel(api_name)
        formatted_word = ApiContext.format_word(api_name)
        file_context= """ 
import requests
from core import BafLog

# YOUR_API_ENDPOINT = "https://fakerapi.it/api/v1/texts?_quantity=1&_characters=500"  # Placeholder email API endpoint
logger = BafLog

class {api_name}API:
    def process(task, data):
                
        response = requests.get('YOUR_API_ENDPOINT', params=data)

        # Handle API response
        if response.status_code != 200:
         logger.error(f"Error fetching last {api_name} data. API response: {response.text}")
         raise Exception(f"Error fetching last {api_name} data. API response: {response.text}")

        your_data_variable = response.json()
        return your_data_variable
        """

        return file_context.replace("{api_name}", camel_case_name)