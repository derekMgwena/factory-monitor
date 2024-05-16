from djongo import models

class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Parameter(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.device.name} - {self.name} - {self.value}"
