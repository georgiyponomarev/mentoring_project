from django.test import TestCase
from .models import FileFieldModel
from django.core.files.uploadedfile import SimpleUploadedFile

import hashlib

# Create your tests here.
class FileFieldModelTestCase(TestCase):
    def test_calculate_hash(self):
        # Create a test file
        test_file_content = b"Test file content"
        test_file = SimpleUploadedFile("test.txt", test_file_content)

        # Create an instance of YourModel with the test file
        instance = FileFieldModel(file=test_file)
        instance.save()

        # Calculate hash and assert
        expected_hash = hashlib.sha256(test_file_content).hexdigest()
        self.assertEqual(instance.calculate_hash(), expected_hash)
