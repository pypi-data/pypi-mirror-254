import unittest

from pydantic import ValidationError

from netlifyconfig.collection import Collection


class TestBaseCollections(unittest.TestCase):
    def test_required_fields(self):
        """Fields that are required should raise an exception and be of the correct type"""
        with self.assertRaises(ValidationError):
            Collection()
        with self.assertRaises(ValidationError):
            Collection(name='foo')

    def test_empty_fields(self):
        """Empty fields that have a specified default should omit them"""
        bare_minimum = Collection(name='foo', label='foo', fields=[])
        target_dict = {'name': 'foo', 'label': 'foo', 'fields': []}
        self.assertDictEqual(bare_minimum.to_dict(), target_dict)
