import os
import json

def file_tool(filename):

    file_exists = os.path.exists(filename)

    def inner_function(*args, **kwargs):

        commands = kwargs['commands']
        model = kwargs['model']

        if not file_exists:
            with open(filename, "w") as f:
                json.dump(commands, f)

        with open(filename, "r") as f:
            data = json.load(f)

        if commands == "add":
            with open(filename, "w") as f:
                json.dump(data, f)

        print(data)

    return inner_function

if __name__ == '__main__':
    inner_tool = file_tool("./commands.json")
    inner_tool(commands="add", model="model")

