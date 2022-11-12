# multiclipboard
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


# writing data to json file
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# reading data
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not Exist.")

    elif command == "list":
        print(data)
    else:
        print("unknown command")
else:
    print("Please pass Exactly one command")


