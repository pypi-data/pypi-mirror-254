



class ToolContext:
    @staticmethod
    def snake_to_camel(word):
     formatted_word = word.replace('/', '_')
    
     return ''.join(x.capitalize() for x in formatted_word.split('_'))
    
    def format_word(word):
        formatted_word = word.replace('/', '_')
        return formatted_word
    
    def context(tool_name):
        camel_case_name = ToolContext.snake_to_camel(tool_name)
        formatted_word = ToolContext.format_word(tool_name)
        file_context= """ 
from core import BafLog
from prompts import {tool_name}Prompt
from api import {tool_name}API

# Optionally, import any other required modules or packages
# E.g., from api import YourAPI
# E.g., from prompts import YourPrompt

class {tool_name}:
  def __init__(self):
     self.logger = BafLog

  def execute(self,task, data):
    # Process data here
    response = {tool_name}API.process(data)

    prompt = {tool_name}Prompt.{prompt_function}(response)
    return prompt


        """

        return file_context.format(tool_name=camel_case_name, prompt_function=formatted_word + "_prompt")