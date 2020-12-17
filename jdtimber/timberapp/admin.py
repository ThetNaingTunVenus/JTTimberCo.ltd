from django.contrib import admin
from .models import InquiryModel,VeneerModel,DeckingModel,LumberModel,MoldingModel,AgedModel

# Register your models here.
# admin.site.register(InquiryModel)
admin.site.register(VeneerModel)
admin.site.register(DeckingModel)
admin.site.register(LumberModel)
admin.site.register(MoldingModel)
admin.site.register(AgedModel)