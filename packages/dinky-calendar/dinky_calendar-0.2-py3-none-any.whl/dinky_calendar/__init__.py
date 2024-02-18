import pluggy
import caldav
from dinky.display_configuration import DisplayConfiguration
from icalendar import Calendar
from dateutil import tz
import datetime
from PIL import Image, ImageFont, ImageDraw
import pkg_resources
from io import BytesIO
from typing import List

from dinky.layouts.layout_configuration import Zone

hookimpl = pluggy.HookimplMarker("dinky")

class DinkyCalendarPlugin:
    primary_color = "#264653"

    def __init__(self, urls: List[str], username: str, password: str, timezone: str):
        self.urls = urls
        self.username = username
        self.password = password
        self.timezone = timezone

    def _get_events(self):
        all_calendars = []
        for url in self.urls:
            with caldav.DAVClient(url=url, username=self.username, password=self.password) as client:
                cal = client.calendar(url=url)
                today = datetime.datetime.now()
                events = cal.search(
                    start=datetime.datetime(today.year, today.month, today.day),
                    end=today + datetime.timedelta(days=5),
                    event=True,
                    expand=True,
                    sort_keys=("dtstart", "dtend")
                )

                response = []
                for event in events:
                    gcal = Calendar.from_ical(event.data)
                    for event in gcal.walk():
                        if event.name == "VEVENT":
                            start_utc = event.get('dtstart').dt
                            end_utc = event.get('dtend').dt
                            if not hasattr(start_utc, "hour") and not hasattr(end_utc, "hour"):
                                start_local = datetime.datetime.combine(start_utc, datetime.time(0, 0), tzinfo=tz.gettz(self.timezone))
                                end_local = datetime.datetime.combine(end_utc, datetime.time(0, 0), tzinfo=tz.gettz(self.timezone))
                                time = "All Day"
                            else:
                                start_utc = start_utc.replace(tzinfo=tz.gettz('UTC'))
                                start_local = start_utc.astimezone(tz.gettz(self.timezone))
                                end_utc = end_utc.replace(tzinfo=tz.gettz('UTC'))
                                end_local = end_utc.astimezone(tz.gettz(self.timezone))
                                time = f"{start_local.strftime('%H:%M')}-{end_local.strftime('%H:%M')}"
                            response.append({
                                "title": event.get('summary', ""),
                                "location": event.get('location', ""),
                                "start": start_local,
                                "end": end_local,
                                "time": time
                            })
                all_calendars.extend(response)
        return all_calendars

    @hookimpl
    def dinky_draw(self, zone: Zone, fullscreen: DisplayConfiguration):
        # Events
        events = self._get_events()

        # Fonts
        font_data = pkg_resources.resource_stream('dinky_calendar', 'fonts/Roboto-Regular.ttf')
        font_bytes = BytesIO(font_data.read())
        font_date = ImageFont.truetype(font_bytes, 36)
        font_bytes.seek(0)
        font_regular = ImageFont.truetype(font_bytes, 14)
        font_data = pkg_resources.resource_stream('dinky_calendar', 'fonts/Roboto-Bold.ttf')
        font_bytes = BytesIO(font_data.read())
        font_weekday = ImageFont.truetype(font_bytes, 24)
        font_bytes.seek(0)
        font_title = ImageFont.truetype(font_bytes, 14)

        # Panel
        # filter events for events that are happening today using the filter() function
        today = datetime.datetime.today()
        todays_events = list(filter(lambda event: event.get('start') and event.get('start').date() == today.date(), events))
        im_panel = Image.new('RGB', (zone.width, zone.height), (255, 255, 255))
        draw = ImageDraw.Draw(im_panel)
        draw.rectangle((zone.padding, zone.padding, zone.width - zone.padding, zone.padding + 55), fill=self.primary_color)

        draw.text((zone.padding + 5, zone.padding + 5), today.strftime('%b %d'), font=font_date, fill="white")
        draw.text((zone.width - 60, zone.padding + 5), today.strftime('%a'), font=font_weekday, fill="white")

        for i, event in enumerate(todays_events):
            draw.text((zone.padding + 5, 55 + zone.padding + 5 + (40 * i)), event["title"], font=font_title, fill=self.primary_color)
            draw.text((zone.padding + 5, 55 + zone.padding + 5 + (40 * i) + 18), f'{event["time"]} {event["location"]}', font=font_regular, fill="black")

        # Fullscreen
        im_fullscreen = Image.new('RGB', (fullscreen.width, fullscreen.height), (255, 255, 255))
        draw = ImageDraw.Draw(im_fullscreen)
        draw.rectangle((zone.padding, zone.padding, fullscreen.width - zone.padding, zone.padding + 55), fill=self.primary_color)

        for i in range(5):
            draw.text((zone.padding + 5 + i * 155, zone.padding + 5), (today + datetime.timedelta(days=i)).strftime('%b %d'), font=font_date, fill="white")
            todays_events = list(filter(lambda event: event.get('start') and event.get('start').date() == (today + datetime.timedelta(days=i)).date(), events))

            for j, event in enumerate(todays_events):
                draw.text((zone.padding + 5 + i * 155, 55 + zone.padding + 5 + (58 * j) + 00), event["title"], font=font_title, fill=self.primary_color)
                draw.text((zone.padding + 5 + i * 155, 55 + zone.padding + 5 + (58 * j) + 18), event["time"], font=font_regular, fill="black")
                draw.text((zone.padding + 5 + i * 155, 55 + zone.padding + 5 + (58 * j) + 36), event["location"], font=font_regular, fill="black")

        return im_panel, im_fullscreen
