from __future__ import annotations

from datetime import timedelta
from typing import Callable


class DateDeltaOperation:
    MILLISECONDS: Callable[[int], timedelta] = lambda date_delta: timedelta(milliseconds=date_delta)
    SECONDS: Callable[[int], timedelta] = lambda date_delta: timedelta(seconds=date_delta)
    MINUTES: Callable[[int], timedelta] = lambda date_delta: timedelta(seconds=date_delta * 60)
    HOURS: Callable[[int], timedelta] = lambda date_delta: timedelta(seconds=date_delta * 3600)
    DAYS: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    FORTNIGHT: Callable[[int], timedelta] = lambda date_delta: timedelta(weeks=date_delta * 2)
    WEEKS: Callable[[int], timedelta] = lambda date_delta: timedelta(weeks=date_delta)
    MONTHS: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    TWO_MONTHS: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    THREE_MONTHS: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    FOUR_MONTHS: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    SIX_MONTHS: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    YEARS: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    DECADES: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    CENTURIES: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)
    MILLENNIA: Callable[[int], timedelta] = lambda date_delta: timedelta(days=date_delta)

    @classmethod
    def get_for_text(cls, text) -> Callable[[int], timedelta]:
        return dict(vars(cls)).get(text, lambda date_delta_value: timedelta(days=0))
