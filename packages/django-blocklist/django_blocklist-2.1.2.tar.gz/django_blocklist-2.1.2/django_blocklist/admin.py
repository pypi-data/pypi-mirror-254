from datetime import timezone
import datetime

from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import BlockedIP


@admin.display(description="Reason")
def reason_truncated(entry: BlockedIP) -> str:
    return entry.reason[:20] + ("..." if len(entry.reason) > 20 else "")


@admin.display(description="Cooldown")
def cooldown(entry: BlockedIP) -> str:
    return f"{entry.cooldown} days"


@admin.display(description="Days left")
def days_left(entry: BlockedIP) -> str:
    if entry.last_seen:
        remaining = f"{entry.cooldown - (datetime.datetime.now(timezone.utc) - entry.last_seen).days}"
    else:
        remaining = ""
    return remaining


@admin.action(permissions=["view"])
def look_up_first_selected_IP(modeladmin, request, queryset):
    obj = queryset[0]
    return HttpResponseRedirect(f"https://whatismyipaddress.com/ip/{obj.ip}")


class BlockedIPAdmin(admin.ModelAdmin):
    list_display = ["ip", "first_seen", "last_seen", "tally", cooldown, days_left, reason_truncated]
    list_filter = ["first_seen", "last_seen", "cooldown", "reason"]
    search_fields = ["ip", "reason"]
    actions = [look_up_first_selected_IP]

    class Meta:
        model = BlockedIP


admin.site.register(BlockedIP, BlockedIPAdmin)
