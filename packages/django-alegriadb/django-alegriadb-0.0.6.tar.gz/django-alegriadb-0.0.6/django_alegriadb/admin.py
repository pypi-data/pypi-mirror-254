from django.contrib import admin, messages
from alegriadb.alegriadb.models import AppsToVerifyModel, RedirectEmail, Verified
from django.db.transaction import atomic
from alegriadb.alegriadb.utils.alegria_admin_funcitons import AlegriaVerifier

@admin.register(AppsToVerifyModel)
class AppsToVerifyModelAdmin(admin.ModelAdmin):
    list_display = ['name','db_external_name','should_verify']

    @atomic
    def verify_app(modeladmin: admin.ModelAdmin, request, queryset):
        try:
            AlegriaVerifier(queryset=queryset)
            msg = "OK..."
            modeladmin.message_user(request, msg, level=messages.SUCCESS)
        except:
            msg = 'Alegria'
            modeladmin.message_user(request, msg, level=messages.ERROR)
            
    actions = ["verify_app",]

@admin.register(RedirectEmail)
class RedirectEmailAdmin(admin.ModelAdmin):
    list_display = ['email',]

@admin.register(Verified)
class VerifiedAdmin(admin.ModelAdmin):
    list_display = ['data','started_at','finished_at']