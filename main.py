from ConfigParser import SafeConfigParser as ConfigParser
import argparse

import scene
import read_ios

def main():
    parser = argparse.ArgumentParser("Visualise clews")
    args = parser.parse_args()

    config = ConfigParser()
    config.read(["properties.ini"])

    host = config.get("server", "host")
    port = config.getint("server", "port")

    scene.visualise_path(scene.position(read_ios.retrieve_test("test_1")))

if __name__ == "__main__":
    main()
