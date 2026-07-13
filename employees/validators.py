import os
from django.core.exceptions import ValidationError

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]
DOCUMENT_EXTENSIONS = [".pdf"]

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


def validate_image(file):
    ext = os.path.splitext(file.name)[1].lower()

    if ext not in IMAGE_EXTENSIONS:
        raise ValidationError("Only JPG and PNG images are allowed.")

    if file.size > MAX_FILE_SIZE:
        raise ValidationError("Image size should not exceed 5 MB.")


def validate_document(file):
    ext = os.path.splitext(file.name)[1].lower()

    if ext not in DOCUMENT_EXTENSIONS:
        raise ValidationError("Only PDF documents are allowed.")

    if file.size > MAX_FILE_SIZE:
        raise ValidationError("Document size should not exceed 5 MB.")