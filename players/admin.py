from django.contrib import admin
from .models import Players, Message

class MessageInline(admin.StackedInline):
    model = Message
    extra = 1



@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ['caption','image']
    list_display_links = ['caption']
    search_fields= ['id','caption']
    inlines = [MessageInline]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user','photo','post','message']
    autocomplete_fields = ['post']



# Register your models here.
