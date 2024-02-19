import subprocess
import os
import shutil

def setup(project_name):
    try:
        # Cloning the git repository into a directory with a custom name
        print(f"Cloning the BafCode repository into {project_name}...")
        subprocess.check_call(['git', 'clone', 'https://github.com/aitelabrandig/bafcode.git', project_name])
        print("Cloning completed successfully!")

    except subprocess.CalledProcessError:
        print("Error: Failed to clone the BafCode repository. Ensure you have 'git' installed and internet access.")
        return


    try:
        # Installing the requirements
        print("Installing the requirements...")
        subprocess.check_call(['pip', 'install', '-r', f'{project_name}/src/requirements.txt'])
        print("Requirements installed successfully!")

    except subprocess.CalledProcessError:
        print("Error: Failed to install the required packages. Ensure you have 'pip' installed.")
        return

    try:
        # Change directory to run the baf command
        print(f"Changing directory to '{project_name}/src/'...")
        os.chdir(f'{project_name}/src/')
    except OSError:
        print(f"Error: Failed to change directory to '{project_name}/src/'. Ensure the repository was cloned and renamed correctly.")
        return

    # Copy .env.example to .env
    try:
        print("Copying .env.example to .env...")
        shutil.copy2('.env.example', '.env')
        print(".env file created successfully!")
    except (shutil.Error, FileNotFoundError) as e:
        print(f"Error: Failed to copy .env.example to .env. Details: {e}")
        return

    try:
        # Run the baf command
        print("Generating Baf key...")
        subprocess.check_call(['bafcode', 'generate:key'])
        print("Baf key generated successfully!")

    except subprocess.CalledProcessError:
        print("Error: Failed to generate the Baf key. Ensure the 'baf' command is in the PATH.")
