from getDateTimeInfo import get_datetime
from getSenseHatStats import get_stats
import json

stats = {}
stats["DateTime"] = get_datetime()
stats["Sense_Hat"] = get_stats()
stats_json = json.dumps(stats)

print stats_json
