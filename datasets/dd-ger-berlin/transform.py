from typing import Any, Generator
from nomenklatura.entity import CE

from investigraph.model import Context

from hashlib import sha1
from datetime import datetime


def handle(ctx: Context, data: dict[str, Any], ix: int):
    slug = "dd-ger-berlin"
    id_ = ctx.make_slug(slug)
    proxy = ctx.make_proxy("Event", id_)

    proxy.id = sha1(str(data.get("thema") + data.get("datum")).lower().strip().encode()).hexdigest()

    proxy.add("name", data.get("thema"))

    proxy.add("startDate", datetime.strptime(data.get("datum")
        + " " + data.get("von"), "%d.%m.%Y %H:%M").isoformat())
    proxy.add("endDate", datetime.strptime(data.get("datum")
        + " " + data.get("bis"), "%d.%m.%Y %H:%M").isoformat())

    proxy.add("description", "Lfd. Nr. " + data.get("lfdnr"))

    if data.get("strasse_nr") and data.get("plz"):
        finalLocation = data.get("strasse_nr") + ", " + data.get("plz") + " Berlin"
    elif not data.get("strasse_nr") and data.get("plz"):
        finalLocation = data.get("plz") + " Berlin"
    elif not data.get("strasse_nr") and not data.get("plz"):
        finalLocation = "Berlin"
    proxy.add("location", finalLocation)

    proxy.add("locationMentioned", data.get("aufzugsstrecke"))

    yield proxy
