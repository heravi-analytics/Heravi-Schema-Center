import glob
import os
import json

from SchemaValidator import ValidationError
import SchemaValidator as validator


class SchemaHandler:

    def __init__(self):
        self.schemas = {}
        self.loadSchemas()

    def loadSchemas(self):
        path = 'schema'
        for filename in glob.glob(os.path.join(path, '*.json')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
                data = json.load(f)
                try:
                    self.validateSchema(data)
                except ValidationError as error:
                    print("[Validation Exception] " + ":".join((data['name'], data['version'])) + f' has an error {error}')
                    continue
                self.schemas[":".join((data['name'], data['version']))] = data
        return self.schemas

    def validateSchema(self, schema):
        validator.validateName(schema['name'])
        validator.validateProperties(schema['properties'])
