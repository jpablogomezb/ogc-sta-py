from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=480)
    properties = models.JSONField(null=True, blank=True)
    # Locations
    # HistoricalLocations
    # Datastream

    @property
    def iot_id(self):
        return self.id


# class Location(models.Model):
#     name
#     description
#     encodingType
#     Location



 