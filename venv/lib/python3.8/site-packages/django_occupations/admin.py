from django.contrib import admin
from .models import ONetAlternateTitle, ONetOccupation, SOCDetailedOccupation, SOCBroadOccupation, SOCMinorGroup, SOCMajorGroup, SOCIntermediateAggregationGroup, SOCHighLevelAggregationGroup

admin.site.register(ONetAlternateTitle)
admin.site.register(ONetOccupation)
admin.site.register(SOCDetailedOccupation)
admin.site.register(SOCBroadOccupation)
admin.site.register(SOCMinorGroup)
admin.site.register(SOCMajorGroup)
admin.site.register(SOCIntermediateAggregationGroup)
admin.site.register(SOCHighLevelAggregationGroup)
