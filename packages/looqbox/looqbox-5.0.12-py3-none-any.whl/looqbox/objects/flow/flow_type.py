from __future__ import annotations

from enum import Enum


class FlowType(Enum):
    """Enum to define the flow type."""
    LOOQ_TEST_CONN = "LOOQ_TEST_CONN"
    LOOQ_RESPONSE = "LOOQ_RESPONSE"
    LOOQ_RELOAD_DATABASE_CONNECTIONS = "LOOQ_RELOAD_DATABASE_CONNECTIONS"
    LOOQ_RESPONSE_FORM = "LOOQ_RESPONSE_FORM"
