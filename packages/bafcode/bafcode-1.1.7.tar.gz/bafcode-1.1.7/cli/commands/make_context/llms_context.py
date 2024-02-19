



class LlmContext:
    @staticmethod
    def snake_to_camel(word):
     formatted_word = word.replace('/', '_')
    
     return ''.join(x.capitalize() for x in formatted_word.split('_'))
    
    def format_word(word):
        formatted_word = word.replace('/', '_')
        return formatted_word
    
    def context(llm_name):
        camel_case_name = LlmContext.snake_to_camel(llm_name)
        formatted_word = LlmContext.format_word(llm_name)
        file_context= """ 
 
from core import BafLog
from config import Config
# Optionally, import any other required modules or packages
# E.g., from api import YourLLMAPI


class {llm_name}LLM:
    def __init__(self):
      self.logger = BafLog

# Initialize your LLM API config here
       

    def process(self,message,prompt,data):
    
      if not prompt:
       self.logger.error("No prompt provided for {llm_name} LLM.")
       raise ValueError("A prompt is required for processing.")

      try:
         # use your LLM API and pass in the prompt and message to process here
         response = 'Use your LLM API here e.g., YourLLMAPI.process(prompt,message)'
         return response
         # Response should be a string e.g., "This is a response from the LLM API."

      except Exception as e:
         self.logger.error(f"Error processing with {llm_name} LLM: {str(e)}")
         return {
          'message': "Error processing with LLM.",
          'status': "error"
              }


        """

        return file_context.replace("{llm_name}", camel_case_name)