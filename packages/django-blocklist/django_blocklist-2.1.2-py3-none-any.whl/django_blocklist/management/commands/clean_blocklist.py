"""Remove IPs from the blocklist if they have been inactive for the required cooldown."""
from datetime import timezone
import datetime
import logging

from django.db.models import Min
from django.core.management.base import BaseCommand

from ...models import BlockedIP

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run", action="store_true", help="Preview the removal rather than performing it."
        )

    help = __doc__

    def handle(self, *args, **options):
        dry_run = options.get("dry_run")
        self.verbosity = options.get("verbosity")
        total_at_start = BlockedIP.objects.count()

        if total_at_start == 0:
            self.handle_message("clean_blocklist found 0 BlockedIP entries")
            return

        deletion_count = 0
        shortest_cooldown_in_db = BlockedIP.objects.aggregate(shortest=Min("cooldown"))["shortest"]
        latest_possible_timestamp_of_expired_entries = datetime.datetime.now(
            timezone.utc
        ) - datetime.timedelta(days=shortest_cooldown_in_db)
        for entry in BlockedIP.objects.filter(last_seen__lte=latest_possible_timestamp_of_expired_entries):
            if entry.has_expired():
                deletion_count += 1
                if not dry_run:
                    entry.delete()
        if dry_run:
            message = f"Would have removed {deletion_count} IPs."
        else:
            message = (
                f"Removed {deletion_count} IPs from blocklist; {total_at_start - deletion_count} remain."
            )
            self.handle_message(message)

    def handle_message(self, message):
        logger.info(message)
        if self.verbosity > 0:
            print(message)
