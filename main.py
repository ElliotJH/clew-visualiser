import ConfigParser
import argparse

import scene

def main():
    parser = argparse.ArgumentParser("Visualise clews")
    args = parser.parse_args()

    config = ConfigParser.ConfigParser()
    config.read(["properties.ini"])

    host = config.get("server", "host")
    port = config.getint("server", "port")

    scene.visualise_path(
        scene.position(
            scene.spiral_stair_case(100, 3)))

if __name__ == "__main__":
    main()
