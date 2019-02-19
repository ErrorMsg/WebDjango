from django.contrib import admin
from .models import *

# Register your models here.


class RuseWisdomInline(admin.TabularInline):
    model = RuseWisdomCard
    extra = 1


class PowerWisdomInline(admin.TabularInline):
    model = PowerWisdomCard
    extra = 1


class WisdomCardAdmin(admin.ModelAdmin):
    fieldsets = (
        ('general info', {
            'fields': ('name', 'pic')
        }),
        ('type info', {
            'fields': ('pattern', 'point', 'effect')
        }),
        ('advance info', {
            'classes': ('collapse', ),
            'fields': ('special', ),
        })
    )
    inlines = [RuseWisdomInline, PowerWisdomInline]
    list_display = ('name', 'short_description', 'effect')

    # class Media():
    #     js = ('static/admin.js',)

# admin.site.register(Card)
admin.site.register(HeroCard)
admin.site.register(BasicCard)
admin.site.register(EquipCard)
#admin.site.register(WeaponCard)
#admin.site.register(HorseCard)
#admin.site.register(ShieldCard)
#admin.site.register(MeasureCard)
admin.site.register(WisdomCard, WisdomCardAdmin)
# admin.site.register(ImmedWisdomCard)
# admin.site.register(DelayWisdomCard)
# admin.site.register(RuseWisdomCard)
# admin.site.register(PowerWisdomCard)
admin.site.register(BadCard)
