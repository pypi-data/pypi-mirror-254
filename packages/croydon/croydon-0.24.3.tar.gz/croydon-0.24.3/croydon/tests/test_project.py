from unittest import TestCase
from croydon.project.models import parse_field_descriptor
from croydon.project.util import normalize_model_name


class TestProject(TestCase):
    def test_parse_invalid_subtyped(self):
        with self.assertRaises(ValueError):
            parse_field_descriptor("name:str[subtype]")

    def test_parse_non_subtyped_ref(self):
        with self.assertRaises(ValueError):
            parse_field_descriptor("user_id:ref")

    def test_parse_no_type(self):
        fd = parse_field_descriptor("name")
        self.assertEqual(fd.name, "name")
        self.assertEqual(fd.field_type, "StringField")
        self.assertEqual(fd.field_subtype, None)

    def test_various_types(self):
        fd = parse_field_descriptor("count:int")
        self.assertEqual(fd.name, "count")
        self.assertEqual(fd.field_type, "IntField")
        self.assertEqual(fd.field_subtype, None)
        self.assertFalse(fd.required)

        fd = parse_field_descriptor("user_id:ref[User]!")
        self.assertEqual(fd.name, "user_id")
        self.assertEqual(fd.field_type, "ReferenceField")
        self.assertEqual(fd.field_subtype, "User")
        self.assertTrue(fd.required)

    def test_render(self):
        fd = parse_field_descriptor("user_id:ref[User]!")
        self.assertEqual(
            "user_id: ReferenceField[User] = ReferenceField(reference_model=User, required=True)",
            fd.render(),
        )

    def test_normalize(self):
        self.assertEqual("UserDef", normalize_model_name("user_def"))
        self.assertEqual("UserDef", normalize_model_name("UserDef"))
        self.assertEqual("UserDef", normalize_model_name("User_Def"))
