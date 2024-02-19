import logging

from ruamel.yaml import YAML

class ReadConfigurations():

    @classmethod
    def read_configurations(cls, file_name):
        yaml = YAML()
        yaml.preserve_quotes = True        
        try: 
            with open(file_name, 'r') as _file:
                configurations=yaml.load(_file)
            
            return configurations
        except yaml.YAMLError as exc:
            logging.error(f"Error reading YAML file: {exc}")
        except FileNotFoundError:
            logging.error("File not found.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            
