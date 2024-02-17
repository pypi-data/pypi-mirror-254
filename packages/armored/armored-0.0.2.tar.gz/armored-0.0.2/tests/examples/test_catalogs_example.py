import unittest

import yaml

from armored.catalogs import Schema


class CatalogExample(unittest.TestCase):
    def test_schema_parser(self):
        config = yaml.safe_load(
            """
        name: "warehouse"
        objects:
          - name: "customer_master"
            schemas:
              - name: "id"
                dtype: "integer"
                pk: true
              - name: "name"
                dtype: "varchar( 256 )"
                nullable: false
        """
        )
        schema = Schema.model_validate(config)
        self.assertEqual(1, len(schema.objects))
