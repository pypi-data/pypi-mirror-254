from .commands import setup, start, generate_key, make

def main():
    import sys

    if len(sys.argv) < 2:
        print("\033[94mPlease provide a command. Options: setup, start, generate-key, make\033[0m")
        return

    command = sys.argv[1]
    if command == "setup":
        if len(sys.argv) < 3:
            print("\033[94mPlease provide a project name. E.g., bafcode setup 'project name'\033[0m")
            return
        project_name = sys.argv[2]
        setup.setup(project_name)
    elif command == "start":
        start.start_baf()
    elif command == "generate:key":
        generate_key.generate_fernet_key()
    elif command == "make":
        if len(sys.argv) < 4:
            print("For the 'make' command, please specify a type and a name. E.g., make tool email")
            return
        type_ = sys.argv[2]
        name = sys.argv[3]
        if type_ == "tool":
            make.make(type_,name)
            make.make('api',name)
            make.make('prompt',name)
        elif type_ == "api":
            make.make(type_,name)
        elif type_ == "prompt":
            make.make(type_,name)
        elif type_ == "llm":
            make.make(type_,name)
        else:
            print(f"Unknown type for 'make' command: {type_}")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
