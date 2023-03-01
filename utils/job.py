# Contains classes for job posting information
__author__ = "Matteo Golin"

# Imports
from dataclasses import dataclass
from typing import Optional

# Constants


# Employer
@dataclass
class Employer:
    """Represents a prospect employer."""

    name: str
    address: str
    hiring_manager: Optional[str] = None  # Not always known

    def __post_init__(self):
        """Replace hiring manager with appropriate name if it is None."""
        if self.hiring_manager is None or self.hiring_manager == "":
            self.hiring_manager = "Hiring Manager"

    def __str__(self):
        return f"Company name: {self.name}"


# Job posting
@dataclass
class JobPosting:
    """Represents a prospect job posting."""

    employer: Employer
    position: str
    raw_posting: str
