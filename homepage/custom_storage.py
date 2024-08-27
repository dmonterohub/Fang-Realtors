from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify

class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # Remove space from the original filename
        name = name.replace(' ', '_')
        # Call parent method to generate a unique filename
        return super().get_available_name(name, max_length)