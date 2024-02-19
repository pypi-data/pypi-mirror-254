from cryptography.fernet import Fernet
import os

def generate_fernet_key():
    key = Fernet.generate_key().decode()

    try:
        # Check if .env exists
        if os.path.exists('.env'):
            with open('.env', 'r') as file:
                lines = file.readlines()

            # Check if FRAMEWORK_SECRET_KEY is in the .env
            key_found = False
            for index, line in enumerate(lines):
                if line.startswith('FRAMEWORK_SECRET_KEY='):
                    lines[index] = f'FRAMEWORK_SECRET_KEY={key}\n'
                    key_found = True
                    break

            # If not found, append to the end of the file
            if not key_found:
                lines.append(f'FRAMEWORK_SECRET_KEY={key}\n')

            # Write the updated lines back to the file
            with open('.env', 'w') as file:
                file.writelines(lines)

        else:  # Raise an exception if .env doesn't exist
            raise FileNotFoundError(".env file not found.")

    except FileNotFoundError:
        print("Error: .env file not found.")
        print("Ensure you are in the 'src' folder of the framework and that the .env file exists.")
        return

    print(f"Generated key: {key}")

