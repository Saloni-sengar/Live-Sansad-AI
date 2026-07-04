from django.contrib import admin
from .models import ParliamentSpeech

class SpeechAdmin(admin.ModelAdmin):

    list_display = ('id','mp','title','date')

    search_fields = ('title','speech_text')


admin.site.register(ParliamentSpeech,SpeechAdmin)