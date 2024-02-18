# coding=utf-8

from ..core.command import Command
from jinja2 import Environment, PackageLoader
from ..utils.utils import *
from ..utils.str_helpers import snake_to_camel, plural_to_singular
from ..utils.file_helpers import create_file, is_file_path_exist
from ..utils.print import *
import os


class ImageFile(object):
    def __init__(self, image_name, image_file):
        self.image_name = image_name
        self.image_file = image_file


class GenerateImageCommand(Command):
    def __init__(self):
        super(GenerateImageCommand, self).__init__()

    def run(self):
        pi = PrintInfo(name="generate image")
        pi.start()
        image_path = "assets/images"
        path = "%s/%s" % (os.getcwd(), image_path)
        list_image_files = []
        if not is_file_path_exist(path):
            print_error("Invalid folder")
            return
        for root, dirs, files in os.walk(path):
            dirs.sort()  # Sort directories
            files.sort()  # Sort files
            for file in files:
                if file.endswith((".png", ".jpg", ".svg")):
                    relative_path = os.path.relpath(root, path)
                    file_name = os.path.splitext(file)[0].replace("-", "_")
                    if relative_path != ".":
                        file_name = f"{relative_path.replace(os.sep, '_')}_{file_name}"
                    list_image_files.append(
                        ImageFile(snake_to_camel(file_name), file).replace(
                            "assets/images/", ""
                        )
                    )
        if not list_image_files:
            print_error("Can't find any image files")
            return
        env = Environment(
            loader=PackageLoader("flutter_gen_templates", "gen"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        template = env.get_template("images.dart")
        content = template.render(image_folder=image_path, files=list_image_files)
        create_file(content, "images", "g.dart", "lib/generated")
        pi.end()
