import re


class ValidationError(Exception):
    def __init__(self, *args):
        if args[0]:
            self.message = args[0]
        else:
            self.message = None


acceptableTypes = ["string", "number"]


def checkType(input, type):
    if not isinstance(input, type):
        raise ValidationError(f'The type of {input} should be {type}')


def checkMatch(match, exceptionText):
    if not bool(match):
        raise ValidationError(exceptionText)


def checkStringType(key, parameters):
    if 'maxLength' in parameters:
        if not (0 < parameters['maxLength'] < 600):
            raise ValidationError(f'for property key {key}, maxLength should be between 0 and 600')


def checkNumberType(key, parameters):
    pass


checkBasedOnType = {
    "string": checkStringType,
    "number": checkNumberType
}


def validateName(name):
    checkType(name, str)
    nameRegex = re.compile('^[a-z\-]+$', re.I)
    match = nameRegex.match(str(name))
    checkMatch(match, "The name is not acceptable please just use lower-case letters and -")


def validateProperties(properties):
    for key in properties:
        parameters = properties[key]
        if parameters['type'] not in acceptableTypes:
            raise ValidationError(f'for {key} the type of {parameters["type"]} is undefined')
        checkBasedOnType[parameters['type']](key, parameters)
