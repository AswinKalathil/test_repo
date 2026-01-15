"""
User Metrics Service

This module provides utilities for:
- Validating user activity events
- Aggregating metrics
- Calculating engagement scores
- Exporting results

Designed to be readable, testable, and safe.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class UserEvent:
    user_id: str
    event_type: str
    timestamp: datetime
    metadata: Optional[Dict[str, str]] = None


class ValidationError(Exception):
    pass


class UserMetricsService:
    VALID_EVENTS = {"login", "logout", "purchase", "view"}

    def __init__(self) -> None:
        self
