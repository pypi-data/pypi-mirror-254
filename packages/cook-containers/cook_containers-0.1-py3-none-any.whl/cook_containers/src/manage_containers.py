import logging
import os 

from cook_containers.src.create_container_template import CreateContainerTemplate

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)



class ContainerManager:
    def __init__(self, configurations) -> None:
        self.configurations = configurations

    def manage_containers(self):
        for configuration in self.configurations:
            try:
                container_template = CreateContainerTemplate(configuration['dockerfile'])
                container_template.generate_container_template()
            except Exception as e:
                LOGGER.error(f"Failed to build dockerfile because of following error {e}")
                self._cleanup_container_template(configuration['dockerfile'].get('path'))
                raise 
            else:
                self._log_success(configuration['dockerfile'].get('path'),configuration.get('name') )

    def _cleanup_container_template(self, path):
        try: 
            os.remove(path)
        except Exception as e:
            LOGGER.error(f"Failed to delete the failed dockerfile at path {path} due to error {e}")
        else:
            LOGGER.info(f"Deleted the failed dockerfile at path: {path}")


    def _log_success(self,path, name=None):
        LOGGER.info(f"Successfully created the dockerfile for {name} as per provided configutations at path: {path} ")
