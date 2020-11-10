import argparse


def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("install");

    args = parser.parse_args()

    return args












if __name__ == "__main__":
    args = parseArguments();
    print(args);

