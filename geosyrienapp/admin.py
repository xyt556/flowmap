from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from geosyrienapp.models import WaterConsumption
from geosyrienapp.models import refugees2011, refugees2012, refugees2013, refugees2014, refugees2015, refugees2016, refugees2017, refugees2018

# Register your models here.

# Fuellen der im models.py erstellten Tabelle


class WaterConsumptionAdmin(LeafletGeoAdmin):
    pass


class refAdmin(LeafletGeoAdmin):
    pass


admin.site.register(WaterConsumption, WaterConsumptionAdmin)
admin.site.register(refugees2011, refAdmin)
admin.site.register(refugees2012, refAdmin)
admin.site.register(refugees2013, refAdmin)
admin.site.register(refugees2014, refAdmin)
admin.site.register(refugees2015, refAdmin)
admin.site.register(refugees2016, refAdmin)
admin.site.register(refugees2017, refAdmin)
admin.site.register(refugees2018, refAdmin)
