
####### fuckkkk needs to tackle reading strings from yaml for example let's say someone passes in "$PATH:$some_new_path" I need to print this as it is i.e. '"$PATH:$some_new_path"'
#### one way to handle this is I can escape the double quoted string in my program. Parse all the keys and look for  ruamel.yaml.scalarstring.DoubleQuotedScalarString and escape it
##### another way is that I could use this walk tree routine and escape double quotes https://stackoverflow.com/questions/50802218/python-3-5-how-to-print-a-value-with-double-quotes-in-yaml?rq=3



class CreateContainerTemplate:

	def __init__(self, configuration):
		self._configuration = configuration
		self._container_template = self._create_container_template()

	_method_mapping = {
			'add' : '_add_files',
			'args' : '_add_runtime_arguments',
			'cmd' : '_default_commands',
			'copy' : '_copy_onto_image',
			'entrypoint' : '_default_executables',
			'ports' : '_expose_ports',
			'env'  : '_add_environement_variables',
			'base_images' : '_add_images',
			'label' : '_add_metadata',
			'run'  : '_add_run_commands',
			'shell' : '_set_default_shell',
			'user' : '_declare_user',
			'workdir' : '_setup_working_directory',
			'volumes' : '_create_volume_mounts',
			'path': '_default_method'

			}

	def generate_container_template(self):
		self._add_configurations_to_template()
		self._container_template.close()

		return 		

	def _create_container_template(self):
		if self._configuration.get("path"):
			container_template = open(self._configuration.get("path"), 'a')

		return container_template
      # get path of wherever the code is being called from


	def _add_configurations_to_template(self):
		for keys in self._configuration:
			if self._configuration.get(keys) and keys!="path": # handle condition where an empty list is being passed
				method = getattr(self, self._method_mapping[keys])
				method(self._configuration[keys])

	def _add_files(self, data):
		files = [f"ADD {''.join(files.keys())} {'.'.join(files.values())} " for files in data]
		self._write_to_template(files)

	def _add_runtime_arguments(self, data):
		runtime_arguments = [self._add_argument_with_default_value(argument) if isinstance(argument, dict) else f"ARG {argument}" for argument in data ]
		self._write_to_template(runtime_arguments)

	def _add_argument_with_default_value(self, argument):
		return f"ARG {''.join(argument.keys())} = {''.join(argument.values())}"

	def _add_images(self, data):
		images = [f"FROM {image}" for image in data]
		self._write_to_template(images)

	def _add_environement_variables(self, data): # handle condition where values against env var are empty
		environemnt_variables = [f"ENVIRONEMNT {''.join(pairs.keys())} = {''.join(pairs.values())}" for pairs in data]
		self._write_to_template(environemnt_variables)

	def _copy_onto_image(self, data):
		files_to_copy = [f"COPY {''.join(pairs.keys())} = {''.join(pairs.values())}" for pairs in data]
		self._write_to_template(files_to_copy)

	def _setup_working_directory(self, data):
		working_directory = f"WORKDIR {data}"
		self._write_to_template(working_directory)

	def _expose_ports(self, data):
		ports_to_expose = [f"EXPOSE {ports}" for ports in data]
		self._write_to_template(ports_to_expose)

	def _add_metadata(self, data):
		labels = [f"LABELS {''.join(labels.keys())} = {''.join(labels.values())}" for labels in data]
		self._write_to_template(labels)

	def _declare_user(self, data):
		user_to_declare = f"USER {data}"
		self._write_to_template(user_to_declare)

	def _create_volume_mounts(self, data):
		volume_mount_point = [f"VOLUME {mount_points} " for mount_points in data]
		self._write_to_template(volume_mount_point)

	def _default_executables(self, data):
		default_executables = f"ENTRYPOINT {data}"
		self._write_to_template(default_executables)

	def _default_commands(self, data):
		default_commands = f"CMD {data}"
		self._write_to_template(default_commands)

	def _add_run_commands(self, data):
		run_commands = [f"RUN {commands}" for commands in data]
		self._write_to_template(run_commands)

	def _set_default_shell(self, data):
		default_shell = f"SHELL {data}"
		self._write_to_template(default_shell)

	def _write_to_template(self, data):
		if isinstance(data, list):
			self._container_template.writelines([lines+"\n" for lines in data])
			self._container_template.write("\n")
		else:
			self._container_template.writelines(data+"\n")
			self._container_template.write("\n")
