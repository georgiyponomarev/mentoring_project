from django.db import models
import hashlib


# Create your models here.
class FileFieldModel(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=254)

    # def save(self, *args, **kwargs):
    #     # Override save method to prevent actual file saving
    #     pass

    def calculate_hash(self):
        """This method returns the SHA256 hash of the file passed into it"""
        # make a hash object
        hash = hashlib.sha256()
        # open file for reading in binary mode
        with self.file.open('rb') as file:
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                hash.update(chunk)

        # return the hex representation of digest
        return hash.hexdigest()
