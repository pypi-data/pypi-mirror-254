"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from rest_framework.exceptions import APIException, ValidationError
from rest_framework import status
from lxml.etree import XMLSyntaxError


class LabelStudioError(Exception):
    pass


class DataStudioAPIException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Unknown error'


class DataStudioDatabaseException(DataStudioAPIException):
    default_detail = 'Error executing database query'


class DataStudioDatabaseLockedException(DataStudioAPIException):
    default_detail = "Sqlite <a href='https://docs.djangoproject.com/en/3.1/ref/databases/#database-is-locked-errors'>doesn't operate well</a> on multiple transactions. \
    Please be patient and try update your pages, or ping us on Slack to  get more about production-ready db"


class ProjectExistException(DataStudioAPIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = 'Project with the same title already exists'


class DataStudioErrorSentryIgnored(Exception):
    pass


class LabelStudioAPIExceptionSentryIgnored(DataStudioAPIException):
    pass


class LabelStudioValidationErrorSentryIgnored(ValidationError):
    pass


class LabelStudioXMLSyntaxErrorSentryIgnored(Exception):
    pass


class InvalidUploadUrlError(DataStudioAPIException):
    default_detail = 'The provided URL was not valid. URLs must begin with http:// or https://, and cannot be local IPs.'
    status_code = status.HTTP_403_FORBIDDEN
