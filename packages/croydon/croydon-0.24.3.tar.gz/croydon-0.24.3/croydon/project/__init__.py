import os


def get_templates_dir():
    module_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(module_dir, "templates")
