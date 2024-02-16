from typing import Any, Generator
from nomenklatura.entity import CE

from investigraph.model import Context
from investigraph.util import make_proxy

from hashlib import sha1
from datetime import datetime


def handle(ctx: Context, data: dict[str, Any], ix: int):
    slug = "dd-ger-berlin"
    id_ = join_slug(ctx.prefix, slug)
    proxy = make_proxy("Event", id_)

    proxy.id = sha1(str(record).lower().strip().encode()).hexdigest()

    proxy.add("name", record.get("thema"))

    proxy.add("startDate", datetime.strptime(record.get("datum")
        + " " + record.get("von"), "%d.%m.%Y %H:%M").isoformat())
    proxy.add("endDate", datetime.strptime(record.get("datum")
        + " " + record.get("bis"), "%d.%m.%Y %H:%M").isoformat())

    proxy.add("description", "Lfd. Nr. " + record.get("lfdnr"))

    if record.get("strasse_nr") and record.get("plz"):
        finalLocation = record.get("strasse_nr") + ", " + record.get("plz") + " Berlin"
    elif not record.get("strasse_nr") and record.get("plz"):
        finalLocation = record.get("plz") + " Berlin"
    elif not record.get("strasse_nr") and not record.get("plz"):
        finalLocation = "Berlin"
    proxy.add("location", finalLocation)

    proxy.add("locationMentioned", record.get("aufzugsstrecke"))

    yield proxy
