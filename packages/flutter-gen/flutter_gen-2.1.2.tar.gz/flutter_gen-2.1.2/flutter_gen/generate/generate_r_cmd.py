# coding=utf-8

from os import read
from flutter_gen.config.config_cmd import ConfigCommand
from ..core.command import Command
from jinja2 import Environment, PackageLoader
from ..utils.str_helpers import snake_to_camel
from ..utils.file_helpers import *
from ..utils.json_helpers import get_localization
from ..utils.print import *
from ..utils.file_helpers import create_file, is_file_path_exist
import os


class ImageFile(object):
    def __init__(self, image_name, image_file):
        self.image_name = image_name
        self.image_file = image_file


class FontData(object):
    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name


class GenerateRCommand(Command):
    def __init__(self):
        super(GenerateRCommand, self).__init__()

    def run(self):
        pi = PrintInfo(name="generate localization - images - colors")
        pi.start()
        # Localization
        localization_items = []
        translations_path = "assets/i18n"
        try:
            for file in os.listdir(translations_path):
                if file.endswith(".json"):
                    name = os.path.basename(file)
                    if name == "en-US.json":
                        json = read_json("%s/en-US.json" % translations_path)
                        break
                    else:
                        json = read_json("%s/%s" % (translations_path, file))
        except FileNotFoundError:
            print_error("i18n file not found")
            return

        localization_items = []
        get_localization(json, localization_items)

        # Images
        image_path = "assets/images"
        path = "%s/%s" % (os.getcwd(), image_path)
        list_image_files = []
        if not is_file_path_exist(path):
            print_error("Invalid folder")
            return
        for root, dirs, files in os.walk(image_path):
            dirs.sort()  # Sort directories
            files.sort()  # Sort files
            for file in files:
                if file.endswith((".png", ".jpg", ".svg")):
                    relative_path = os.path.relpath(root, path)
                    file_name = os.path.splitext(file)[0].replace("-", "_")
                    if relative_path != ".":
                        file_name = f"{relative_path.replace(os.sep, '_')}_{file_name}"
                    if platform == "darwin":
                        file_url = os.path.join(root, file)
                    else:
                        file_url = os.path.join(root, file).replace("\\", "/")
                    list_image_files.append(
                        ImageFile(
                            snake_to_camel(file_name),
                            file_url.replace("assets/images/", ""),
                        )
                    )
        if not list_image_files:
            print_error("Can't find any image files")

        # Read the original colors
        original_colors = []
        with open("./assets/color/colors.txt", "r") as f:
            for line in f:
                original_color = line.strip().replace("#", "").upper()
                original_colors.append(original_color)

        # Remove duplicates and sort
        colors = list(set(original_colors))
        colors.sort()

        # Check if colors are different from original colors
        if colors != original_colors:
            # Write to the file
            with open("./assets/color/colors.txt", "w") as f:
                for color in colors:
                    f.write("#" + color + "\n")

        # Fonts
        fonts = []
        pubspec_text = read("pubspec.yaml")
        pubspec_data = yaml.safe_load(pubspec_text)
        flutter = pubspec_data["flutter"]
        if "fonts" in flutter:
            for font in flutter["fonts"]:
                family_name = font["family"]
                name = family_name[0].lower() + family_name[1:]
                fonts.append(FontData(name, family_name))
        else:
            print_error("No fonts available")

        # Write file
        env = Environment(
            loader=PackageLoader("flutter_gen_templates", "gen"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        template = env.get_template("r.dart")
        content = template.render(
            image_folder=image_path,
            files=list_image_files,
            localization_items=localization_items,
            colors=colors,
            fonts=fonts,
        )

        create_file(content, "r", "g.dart", "lib/generated")
        pi.end()
