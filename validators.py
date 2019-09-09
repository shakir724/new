from django.core.exceptions import ValidationError
from django.core.validators import  URLValidator
from django.utils.translation import ugettext_lazy as _
import re

def validateUrl(value):
    validate = URLValidator()
    try:
        validate(value)
    except ValidationError:
        raise ValidationError("URL does not Exists")
    return value

def validateSite(value):
    if not ((".com" in value) or (".in" in value)):
        raise ValidationError("A valid site must be entered in")
    else:
        return value


def validateChar(value):
    if re.findall('\d', value) or re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
        raise ValidationError("The name must contain Characters only")
    else:
        return value 

# def validatePhone(value):
#     if re.findall('[A-Z]', value) or re.findall('[a-z]', value) or re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
#         raise ValidationError("Phone Number must contain Numbers Only")
#     else:
#         return value 

def validateNo(value):
    if re.findall('[A-Z]', value) or re.findall('[a-z]', value) or re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
        raise ValidationError("Must contain Numbers Only")
    else:
        return value 