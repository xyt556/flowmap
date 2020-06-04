from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from geosyrienapp.models import refugees2011, refugees2012, refugees2013, refugees2014, refugees2015, refugees2016, refugees2017, refugees2018


class refAdmin(LeafletGeoAdmin):
    pass


# admin.site.register(refugees2011, refAdmin)
# admin.site.register(refugees2012, refAdmin)
# admin.site.register(refugees2013, refAdmin)
# admin.site.register(refugees2014, refAdmin)
# admin.site.register(refugees2015, refAdmin)
# admin.site.register(refugees2016, refAdmin)
# admin.site.register(refugees2017, refAdmin)
# admin.site.register(refugees2018, refAdmin)

df2011 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2011.xlsx', sheet_name="2011", na_values=None)
df2012 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2012.xlsx', sheet_name="2012", na_values=None)
df2013 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2013.xlsx', sheet_name="2013", na_values=None)
df2014 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2014.xlsx', sheet_name="2014", na_values=None)
df2015 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2015.xlsx', sheet_name="2015", na_values=None)
df2016 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2016.xlsx', sheet_name="2016", na_values=None)
df2017 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2017.xlsx', sheet_name="2017", na_values=None)
df2018 = pd.read_excel(
    '/Users/hoangvutuyen/Documents/python_scripts/geoprojekt/2018.xlsx', sheet_name="2018", na_values=None)

for index, row in df2011.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2011(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()

for index, row in df2012.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2012(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()

for index, row in df2013.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2013(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()

for index, row in df2014.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2014(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()

for index, row in df2015.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2015(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()

for index, row in df2016.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2016(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()

for index, row in df2017.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2017(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()

for index, row in df2018.iterrows():
    Id = index
    land = row['Land']
    pop = row['Gesamtbevoelkerung des Landes']
    refRatio = row['Fluechtlinge pro 10.000 Einwohner']
    refTotal = row['gefluechtete total']
    male = row['maennlich total']
    female = row['weiblich total']
    u18 = row['Kinder unter 18 Jahren']
    u18erstantrag = row['Kinder unter 18 Jahren Erstantrag']
    u34 = row['<34 Jahren']
    u34erstantrag = row['< 34 Jahren Erstantrag']
    u64 = row['< 64 Jahren']
    u64erstantrag = row['< 64 Jahren Erstantrag']
    ue65 = row['> 65 Jahren']
    ue65erstantrag = row['> 65 Jahren Erstantrag']
    unknown = row['unbekannt']
    erstantrag = row['Erstantrag']
    folgeantrag = row['Folgeantrag']
    Longitude = row['e_longitude']
    Latitude = row['e_latitude']

    refugees2018(Id=Id, land=land, pop=pop, refRatio=refRatio, refTotal=refTotal, male=male, female=female,
                 u18=u18, u18erstantrag=u18erstantrag, u34=u34, u34erstantrag=u34erstantrag, u64=u64, u64erstantrag=u64erstantrag,
                 ue65=ue65, ue65erstantrag=ue65erstantrag, unknown=unknown, erstantrag=erstantrag, folgeantrag=folgeantrag, geom=Point(Longitude, Latitude)).save()
