from django.db import models

from enum import Enum

class DeviceChoice(Enum):   # A subclass of Enum
    Mobile = "Mobile"
    Laptop = "Laptop"

CHOICES = (
    ('Mobile', 'Mobile'),
    ('Laptop','Laptop'),
)
  
class Item(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    # device_type = models.CharField(blank=True, null=True,
    #   max_length=6,
    #   choices=[(tag, tag.value) for tag in DeviceChoice]  # Choices is a list of Tuple
    # )
    device_type = models.CharField(max_length=255, choices=CHOICES, null=True)
    
    def __str__(self) -> str:
        return self.name
