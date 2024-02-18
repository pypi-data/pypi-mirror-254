# coding=utf-8

from subprocess import call

from ..utils.utils import *
from ..core.command import Command, CommandOption
from jinja2 import Environment, PackageLoader
from ..utils.file_helpers import create_file, is_file_path_exist
from ..utils.str_helpers import snake_to_camel, plural_to_singular
from flutter_gen.utils.dart_helpers import format_dart_file_code


class Component(object):
    class ComponentType:
        BASE = "base"


class ComponentCommand(Command):
    def __init__(self, parent_name, component_name):
        super(ComponentCommand, self).__init__()
        self.parent_name = parent_name
        self.component_name = component_name

    def get_project_package_name(self):
        try:
            name = get_current_dart_package_name()
            print("Current package name: %s" % name)
            return name.strip()
        except (IOError, OSError) as e:
            logError("Please run this command in flutter folder.")
            exit(1)

    def add_line_after_last_import(self, directory, filename, new_line):
        for root, dirs, files in os.walk(directory):
            if filename in files:
                file_path = os.path.join(root, filename)
                with open(file_path, "r") as file:
                    lines = file.readlines()

                # Check if the line already exists in the file
                if new_line in lines:
                    return "Line already exists in the file."

                # Find the last import line
                last_import_index = None
                for i, line in enumerate(lines):
                    if line.startswith("import "):
                        last_import_index = i

                # Insert the new line after the last import line
                if last_import_index is not None:
                    lines.insert(last_import_index + 1, new_line + "\n")
                    # Write the changes back to the file
                    with open(file_path, "w") as file:
                        file.writelines(lines)
                    print(f"Line added successfully to {file_path}.")
                    return
            print("File not found in the specified directory.")
            return

    def create_files(self):
        env = Environment(
            loader=PackageLoader("flutter_gen_templates", "gen"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        template = env.get_template("component.dart")
        content = template.render(
            extension_name=snake_to_camel(self.component_name.capitalize()),
            parent=self.parent_name,
            parent_cap=snake_to_camel(self.parent_name.capitalize()),
        )
        create_file(
            content,
            self.component_name,
            "dart",
            "lib/scenes/%s/components" % (self.parent_name),
        )
        self.add_line_after_last_import(
            "lib/scenes/%s" % (self.parent_name),
            "%s_view.dart" % (self.parent_name),
            "part 'components/%s.dart';" % (self.component_name),
        )
        format_dart_file_code("lib/scenes/%s_view.dart" % (self.parent_name))
        exit(0)
