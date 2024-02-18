class LocaleItem(object):
    def __init__(self, name, value, key):
        self.name = name
        self.value = value
        self.key = key


def get_keys(some_dictionary, list=[], separator="_", parent=None):
    if isinstance(some_dictionary, str):
        return
    for key, value in some_dictionary.items():
        if parent is None:
            path = "{}".format(key)
        else:
            path = "{}{}{}".format(parent, separator, key)
        if key not in list:
            list.append(path)
        if isinstance(value, dict):
            get_keys(value, list, separator, parent=path)
        else:
            pass


def get_localization(
    some_dictionary,
    localization_items,
    parent=None,
):
    if isinstance(some_dictionary, dict):
        for key, value in some_dictionary.items():
            if parent is None:
                name = "{}".format(key)
                path = "{}".format(key)
            else:
                name = "{}{}{}".format(parent, "_", key).replace(".", "_")
                path = "{}{}{}".format(parent, ".", key)

            if key not in localization_items:
                locale_item = LocaleItem(name, value, path)
                localization_items.append(locale_item)
            if isinstance(value, dict):
                get_localization(
                    value,
                    localization_items,
                    parent=path,
                )
            else:
                pass
