from rest_framework import status

from core.utils.exceptions import DataStudioAPIException


class LabelBulkUpdateError(DataStudioAPIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
