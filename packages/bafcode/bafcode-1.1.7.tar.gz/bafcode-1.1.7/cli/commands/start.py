import subprocess

def start_baf():
    try:
        # Logic to start the framework or application.
        print("Starting the BafCode...")
        # Attempt to start app.py
        subprocess.check_call(['python', 'app.py'])

        print("BafCode started successfully!")

    except FileNotFoundError:
        print("Error: Python interpreter not found or 'app.py' doesn't exist.")
    except subprocess.CalledProcessError:
        print("Error: There was an issue running 'app.py'.")
    except Exception as e:
        # This is a general exception which will catch any unexpected errors.
        # It's a good practice to also log this error for troubleshooting.
        print(f"An unexpected error occurred: {e}")

