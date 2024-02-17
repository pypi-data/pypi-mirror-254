import os.path
from argparse import ArgumentParser, Namespace
from croydon.command import Command
from croydon.project.util import normalize_model_name
from croydon.project.models import parse_field_descriptor, find_models
from croydon import ctx


class New(Command):
    NAME = "new"
    HELP = "create new entities"
    ASYNC_RUN = False

    args: Namespace
    entity_name: str

    def init_argument_parser(self, parser: ArgumentParser) -> None:
        sub = parser.add_subparsers(dest="entity", required=True)
        model = sub.add_parser(name="model")
        model.add_argument("name", nargs=1, help="model name")
        model.add_argument("fields", nargs="*", help="model fields configuration")
        model.add_argument("-k", "--key", type=str, help="key field name")
        model.add_argument(
            "-w",
            "--overwrite",
            action="store_true",
            help="overwrite existing entity if it exists",
        )

        controller = sub.add_parser(name="controller")
        controller.add_argument("name", nargs=1, help="controller name")
        controller.add_argument("-p", "--prefix", help="api prefix", default="/api/v1")
        controller.add_argument(
            "-w",
            "--overwrite",
            action="store_true",
            help="overwrite existing entity if it exists",
        )

    async def setup(self, args: Namespace) -> None:
        self.args = args
        self.entity_name = self.args.name[0]

    def setup_model(self) -> None:
        models_dir = os.path.join(ctx.project_dir, "app/models")
        filename = os.path.join(models_dir, f"{self.entity_name}.py")
        if not self.args.overwrite:
            if os.path.exists(filename):
                raise ValueError(
                    f"file {filename} already exists, use --overwrite to overwrite it"
                )

        model_name = normalize_model_name(self.entity_name)
        collection = model_name.lower() + "s"
        fds = [parse_field_descriptor(field) for field in self.args.fields]

        field_types = {fd.field_type for fd in fds}
        field_subtypes = {fd.field_subtype for fd in fds if fd.field_subtype}

        with open(filename, "w") as output:
            output.write("from croydon.models import StorableModel\n")
            output.write(
                "from croydon.models.fields import " + ", ".join(field_types) + "\n"
            )

            if field_subtypes:
                models = find_models(models_dir)
                for stype in field_subtypes:
                    if stype in models:
                        output.write(f"from {models[stype]} import {stype}\n")

            output.write("\n\n")
            output.write(f"class {model_name}(StorableModel):\n\n")
            output.write(f'    COLLECTION = "{collection}"\n')
            if self.args.key:
                output.write(f'    KEY_FIELD = "{self.args.key}"\n\n')
            for fd in fds:
                output.write(f"    {fd.render()}\n")

    def setup_controller(self) -> None:
        raise NotImplementedError("controller setup is not implemented yet")

    def run_sync(self) -> None:
        try:
            match self.args.entity:
                case "model":
                    self.setup_model()
                case "controller":
                    self.setup_controller()
        except ValueError as e:
            print(e)
