#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

# So soll die Tabelle der Datenbank aussehen


class WaterConsumption(models.Model):
    Id = models.IntegerField(primary_key=True)
    Suburb = models.CharField(max_length=100)
    NoOfSingleResProp = models.IntegerField()
    AvgMonthlyKL = models.IntegerField()
    AvgMonthlyKLPredicted = models.IntegerField()
    PredictionAccuracy = models.IntegerField()
    Month = models.CharField(max_length=50)
    Year = models.IntegerField()
    DateTime = models.DateTimeField()
    geom = models.PointField()

    def __str__(self):
        return self.Suburb

    class Meta:
        verbose_name_plural = 'WaterConsumption'


class refugees2011(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2011'


class refugees2012(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2012'


class refugees2013(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2013'


class refugees2014(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2014'


class refugees2015(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2015'


class refugees2016(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2016'


class refugees2017(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2017'


class refugees2018(models.Model):
    Id = models.IntegerField(primary_key=True)
    land = models.CharField(max_length=100)
    pop = models.FloatField(null=True, blank=True)
    refRatio = models.FloatField(null=True, blank=True)
    refTotal = models.FloatField(null=True, blank=True)
    male = models.FloatField(null=True, blank=True)
    female = models.FloatField(null=True, blank=True)
    u18 = models.FloatField(null=True, blank=True)
    u18erstantrag = models.FloatField(null=True, blank=True)
    u34 = models.FloatField(null=True, blank=True)
    u34erstantrag = models.FloatField(null=True, blank=True)
    u64 = models.FloatField(null=True, blank=True)
    u64erstantrag = models.FloatField(null=True, blank=True)
    ue65 = models.FloatField(null=True, blank=True)
    ue65erstantrag = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
    erstantrag = models.FloatField(null=True, blank=True)
    folgeantrag = models.FloatField(null=True, blank=True)
    haltung = models.TextField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.land

    class Meta:
        verbose_name_plural = 'refugees2018'
