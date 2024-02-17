from dataclasses import dataclass
from typing import Any


@dataclass
class MockBehavior:
    return_value: Any = None
    side_effect: Any = None
