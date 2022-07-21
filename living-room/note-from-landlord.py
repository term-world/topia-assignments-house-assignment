import narrator
import json


def load_json(filepath: str) -> dict:
    fh = open(filepath, "r")
    data = json.load(fh)
    fh.close()
    return data


def main():
    flags = load_json(".flags.json")
    print(flags)


if __name__ == "__main__":
    main()