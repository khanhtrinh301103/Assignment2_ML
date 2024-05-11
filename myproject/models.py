from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')

    def __str__(self):
        return f"Image {self.id}"
