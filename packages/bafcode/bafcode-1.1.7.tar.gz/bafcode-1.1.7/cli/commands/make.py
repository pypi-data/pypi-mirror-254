import os
import sys
from .make_context import ApiContext, LlmContext, PromptContext, ToolContext


def add_to_tool_mapping(directory, class_name):
    init_file = os.path.join(directory, "__init__.py")

    # make the first letter of the class name lowercase
    name = class_name[0].lower() + class_name[1:]
    
    # Form the mapping entry
    mapping_entry = f'    "{name}": {class_name},\n'

    # Read the current content of the __init__.py file
    with open(init_file, "r") as f:
        content = f.readlines()

    # Find the line where the "}" of the command_mapping dictionary is
    closing_brace_index = None
    for index, line in enumerate(content):
        if line.strip() == "}":
            closing_brace_index = index
            break

    if closing_brace_index is not None:
        content.insert(closing_brace_index, mapping_entry)

        # Write the modified content back to the __init__.py file
        with open(init_file, "w") as f:
            f.writelines(content)

    print(f"Added tool mapping for '{class_name}' to {init_file}")



def add_import_to_init(directory, class_name, file_path):
    init_file = os.path.join(directory, "__init__.py")

    # Read the current content of the __init__.py file
    with open(init_file, "r") as f:
        content = f.readlines()

    # Form the import statement
    relative_path = file_path.replace(".py", "").replace("\\", ".")  # Convert path to Python module format
    imported_path = relative_path.replace("/", ".")
    import_statement = f"from .{imported_path} import {class_name}\n"

    # Find the right position for the new import statement (after other imports)
    import_position = 0
    for index, line in enumerate(content):
        if line.startswith("from .") and "import" in line:
            import_position = index

    # Insert the import statement at the right position
    content.insert(import_position + 1, import_statement)

    # Write the modified content back to the __init__.py file
    with open(init_file, "w") as f:
        f.writelines(content)

    print(f"Added import for '{class_name}' to {init_file}")



def create_file(path,context):
    # Ensure the directory exists
    directory = os.path.dirname(path)
    print(f"Attempting to create directory: {directory}")  # Add this line
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Check if file already exists
    if os.path.exists(path):
        print(f"Error: File '{path}' already exists.")
        return

    # Create the file
    with open(path, 'w') as f:
        f.write(context)
    print(f"File '{path}' created successfully!")

def make(type_,name):
    print(f"sys.argv: {sys.argv}")  # Debug: print the full sys.argv


    if type_ == "tool":
        base_dir = "tools"
        full_path = os.path.join(base_dir, name + ".py")
        file_context = ToolContext.context(name)
        create_file(full_path,file_context)
        class_name = ToolContext.snake_to_camel(name)
        add_import_to_init(base_dir, class_name, name)
        add_to_tool_mapping(base_dir, class_name)

    elif type_ == "api":
        base_dir = "api"
        full_path = os.path.join(base_dir, name + ".py")
        file_context = ApiContext.context(name)
        create_file(full_path,file_context)
        class_name = ToolContext.snake_to_camel(name)
        api_class_name = class_name + "API"
        add_import_to_init(base_dir, api_class_name, name)

    elif type_ == "prompt":
        base_dir = "prompts"
        full_path = os.path.join(base_dir, name + ".py")
        file_context = PromptContext.context(name)
        create_file(full_path,file_context)
        class_name = ToolContext.snake_to_camel(name)
        prompt_class_name = class_name + "Prompt"
        add_import_to_init(base_dir, prompt_class_name, name)
    elif type_ == "llm":
        base_dir = "llms"
        full_path = os.path.join(base_dir, name + ".py")
        file_context = LlmContext.context(name)
        create_file(full_path,file_context)
        class_name = ToolContext.snake_to_camel(name)
        llm_class_name = class_name + "LLM"
        add_import_to_init(base_dir, llm_class_name, name)
    else:
        print(f"Error: Unknown type_ '{type_}'")
        sys.exit(1)
