from ConfigParser import SafeConfigParser as ConfigParser
import argparse

import numpy as np

import scene
import read_ios
import read_android

def main():
    parser = argparse.ArgumentParser("Visualise clews")
    args = parser.parse_args()

    config = ConfigParser()
    config.read(["properties.ini"])

    host = config.get("server", "host")
    port = config.getint("server", "port")

    pos = scene.position(read_android.retrieve_test("test_android.tsv"))[:]
    #pos = scene.position(scene.spiral_stair_case(100, 3))
    
    scene.visualise_path(pos)

if __name__ == "__main__":
    main()
