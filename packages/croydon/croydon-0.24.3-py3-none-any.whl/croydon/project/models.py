import os
import re
import inspect
from pydantic import BaseModel
from importlib import import_module
from typing import Dict, Literal, Optional, List
from jinja2 import Environment, FileSystemLoader
from .util import normalize_model_name
from . import get_templates_dir


FD_EXPR = re.compile(r"^(\w+)(:(\w+)(\[([^\]]+)\])?)?(!?)$")
SUBTYPED_TYPES = {"ListField", "DictField", "ReferenceField"}
FieldType = Literal[
    "StringField",
    "IntField",
    "FloatField",
    "BoolField",
    "ListField",
    "DictField",
    "ReferenceField",
    "SelfReferenceField",
    "ObjectIdField",
    "DatetimeField",
]


class FieldDescriptor(BaseModel):
    name: str
    field_type: FieldType
    field_subtype: Optional[str] = None
    required: bool = False

    def render(self) -> str:
        args = {}
        decl = self.name
        if self.field_subtype:
            decl += f": {self.field_type}[{self.field_subtype}]"
        decl += f" = {self.field_type}("

        if self.field_type == "ReferenceField":
            args["reference_model"] = self.field_subtype
        if self.required:
            args["required"] = "True"

        if args:
            decl += ", ".join([f"{k}={v}" for k, v in args.items()])

        decl += ")"
        return decl

    @property
    def py_type(self) -> str:
        match self.field_type:
            case "StringField":
                return "str"
            case "IntField":
                return "int"
            case "FloatField":
                return "float"
            case "BoolField":
                return "bool"
            case "ListField":
                return "List[str]"
            case "DictField":
                return "Dict[str, Any]"
            case "ReferenceField" | "SelfReferenceField" | "ObjectIdField" | "DatetimeField":
                return "str"

    def render_pydantic(self) -> str:
        return f"{self.name}: {self.py_type}"


def find_models(app_models_path: str) -> Dict[str, str]:
    from croydon.models import StorableModel

    model_imports = {}
    for _, _, files in os.walk(app_models_path):
        for filename in files:
            if filename.endswith(".py"):
                modname = "app.models." + filename[:-3].replace("/", ".")
                if modname.endswith(".__init__"):
                    modname = modname[:-9]
                module = import_module(modname)
                for item_name in dir(module):
                    item = getattr(module, item_name)
                    if inspect.isclass(item) and issubclass(item, StorableModel):
                        if item.__name__ not in model_imports:
                            model_imports[item.__name__] = item.__module__
    return model_imports


def parse_field_descriptor(fd: str) -> FieldDescriptor:
    match = FD_EXPR.findall(fd)
    if not match:
        raise ValueError(f'invalid field descriptor "{fd}"')

    tokens = match[0]

    fname, _, ftype, _, fsubtype, excl = tokens
    match ftype.lower():
        case "":
            field_type = "StringField"
        case "str" | "string" | "stringfield":
            field_type = "StringField"
        case "int" | "integer" | "integerfield":
            field_type = "IntField"
        case "bool" | "boolean" | "boolfield":
            field_type = "BoolField"
        case "float" | "floatfield":
            field_type = "FloatField"
        case "objid" | "objectid" | "objectidfield":
            field_type = "ObjectIdField"
        case "list" | "listfield":
            field_type = "ListField"
        case "dict" | "dictfield":
            field_type = "DictField"
        case "date" | "datetime" | "timestamp" | "ts" | "dt":
            field_type = "DatetimeField"
        case "ref" | "reference" | "referencefield":
            field_type = "ReferenceField"
        case "self" | "selfreference" | "selfreferencefield":
            field_type = "SelfReferenceField"
        case _:
            raise ValueError(f'unknown field type "{ftype}"')

    if fsubtype and field_type not in SUBTYPED_TYPES:
        raise ValueError(f"type {field_type} can't have subtypes")
    if not fsubtype and field_type == "ReferenceField":
        raise ValueError(f"type ReferenceField must have a subtype")

    required = False
    if excl:
        required = True

    return FieldDescriptor(
        name=fname,
        field_type=field_type,
        field_subtype=fsubtype or None,
        required=required,
    )


def render_model(
    entity_name: str,
    fields: List[str],
    models_dir: str,
    *,
    overwrite: bool = False,
    key: Optional[str] = None,
) -> None:
    filename = os.path.join(models_dir, f"{entity_name}.py")
    if not overwrite:
        if os.path.exists(filename):
            raise ValueError(
                f"file {filename} already exists, use --overwrite to overwrite it"
            )

    model_name = normalize_model_name(entity_name)
    collection = model_name.lower() + "s"
    fds = [parse_field_descriptor(field) for field in fields]

    field_types = {fd.field_type for fd in fds}
    field_subtypes = {fd.field_subtype for fd in fds if fd.field_subtype}
    subtype_imports = []
    if field_subtypes:
        models = find_models(models_dir)
        for stype in field_subtypes:
            if stype in models:
                subtype_imports.append((stype, models[stype]))

    env = Environment(loader=FileSystemLoader(get_templates_dir()))
    tmpl = env.get_template("model.py.tmpl")
    render = tmpl.render(
        field_types=field_types,
        collection=collection,
        fds=fds,
        subtype_imports=subtype_imports,
        key=key,
        class_name=model_name,
    )

    with open(filename, "w") as output:
        output.write(render)
