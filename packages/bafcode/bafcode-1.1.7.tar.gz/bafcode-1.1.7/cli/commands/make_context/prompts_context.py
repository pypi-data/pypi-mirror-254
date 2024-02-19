class PromptContext:
    @staticmethod
    def snake_to_camel(word):
        """Convert snake_case or a format with slashes to CamelCase."""
        formatted_word = word.replace('/', '_')
        return ''.join(x.capitalize() for x in formatted_word.split('_'))

    @staticmethod
    def format_word(word):
        """Format word by replacing slashes with underscores."""
        return word.replace('/', '_')

    @staticmethod
    def context(prompt_name):
        camel_case_name = PromptContext.snake_to_camel(prompt_name)
        formatted_word = PromptContext.format_word(prompt_name)

        file_context = """ 
from core import BafLog
# Optionally, import any other required modules or packages

class {prompt_name}Prompt:  # Replace {prompt_name} with the name of your prompt
    def {function}_prompt(data):
        prompt = {string}
            {prompt_name} Data:
            {{data}}
        {string}
        return prompt.format(data=data)
        """

        return file_context.format(prompt_name=camel_case_name, string='"""', function=formatted_word)
