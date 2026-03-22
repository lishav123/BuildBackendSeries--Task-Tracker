import os
import json
import functools

def file_tool(filename):
    def wrapped(func):

        @functools.wraps(func)
        def inner_function(*args, **kwargs):
            file_exists = os.path.exists(filename)
            data = []

            if not file_exists:
                with open(filename, "w") as f:
                    json.dump([], f)

            with open(filename, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

            kwargs['data'] = data
            res = func(*args, **kwargs)

            data = res if res is not None else data
            kwargs['data'] = data

            with open(filename, "w") as f:
                json.dump(kwargs["data"], f, indent=4)

        return inner_function
    return wrapped


if __name__ == '__main__':
    @file_tool("command.json")
    def add(data):
        return {"Hello": "Helloww World"}

    add()