from enum import Enum

_ABSOLUTE = {'DAYS', 'DAY', 'HOURS', 'HOUR', 'WEEKS', 'WEEK', 'MINUTES', 'MINUTE', 'SECONDS', 'SECOND', 'MONTHS',
                'MONTH', 'YEARS', 'YEAR', 'DECADES', 'DECADE', 'CENTURIES', 'CENTURY', 'MILLENNIA', 'MILLENNIUM'}
_RELATIVE = {'BIMESTER', 'TRIMESTER', 'QUARTER', 'SEMESTER', 'YEAR_DAY', 'MONTH_DAY', 'WEEK_DAY', 'WEEK_YEAR',
             'WEEK_MONTH', 'DAY_HOURS', 'DAY_MINUTES', 'HOUR_MINUTES', 'HOUR_SECONDS', 'DAY_SECONDS', 'MINUTE_SECONDS'}


class TemporalGranularity(Enum):
    # Absolute date
    DAYS = "DAYS"
    DAY = "DAY"
    HOURS = "HOURS"
    HOUR = "HOUR"
    WEEKS = "WEEKS"
    WEEK = "WEEK"
    MINUTES = "MINUTES"
    MINUTE = "MINUTE"
    SECONDS = "SECONDS"
    SECOND = "SECOND"
    MONTHS = "MONTHS"
    MONTH = "MONTH"
    YEARS = "YEARS"
    YEAR = "YEAR"
    DECADES = "DECADES"
    DECADE = "DECADE"
    CENTURIES = "CENTURIES"
    CENTURY = "CENTURY"
    MILLENNIA = "MILLENNIA"
    MILLENNIUM = "MILLENNIUM"

    # Relative date
    BIMESTER = "BIMESTER"
    TRIMESTER = "TRIMESTER"
    QUARTER = "QUARTER"
    SEMESTER = "SEMESTER"
    YEAR_DAY = "YEAR_DAY"
    MONTH_DAY = "MONTH_DAY"
    WEEK_DAY = "WEEK_DAY"
    WEEK_YEAR = "WEEK_YEAR"
    WEEK_MONTH = "WEEK_MONTH"
    DAY_HOURS = "DAY_HOURS"
    DAY_MINUTES = "DAY_MINUTES"
    HOUR_MINUTES = "HOUR_MINUTES"
    HOUR_SECONDS = "HOUR_SECONDS"
    DAY_SECONDS = "DAY_SECONDS"
    MINUTE_SECONDS = "MINUTE_SECONDS"

    def is_abs(self):
        """
        Verifica se a granularidade é absoluta.
        """
        return self.name in _ABSOLUTE

    def is_relative(self):
        """
        Verifica se a granularidade é relativa.
        """
        return self.name in _RELATIVE
