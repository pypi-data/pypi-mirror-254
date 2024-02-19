import argparse
import sys

from cook_containers.src.read_configurations import ReadConfigurations
from cook_containers.src.manage_containers import ContainerManager

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('config_file',help='pass the path to the config file')

    args = parser.parse_args()

    config_file = args.config_file

    configurations = ReadConfigurations.read_configurations(config_file)

    container_manager = ContainerManager(configurations['containers'])

    container_manager.manage_containers()

    return


if __name__== "__main__":
    sys.exit(main())