# Contains the class for applicant information
__author__ = "Matteo Golin"

# Imports
from dataclasses import dataclass, field
from typing import Any, Self
import json

# Constants
JSON = dict[str, Any]


# Education
@dataclass
class Education:
    """Represents an applicant's education."""

    degree: str
    gpa: str
    institution: str

    @classmethod
    def from_json(cls, data: JSON) -> Self:
        """Returns a populated Education object from JSON data."""
        return cls(
            degree=data.get("degree"),
            gpa=data.get("gpa"),
            institution=data.get("institution")
        )

    def __str__(self):
        return f"{self.degree} from {self.institution}"


# Position
@dataclass
class Position:
    """Describes positions held by the applicant."""

    title: str
    organization: str
    description: str

    @classmethod
    def from_json(cls, data: JSON) -> Self:
        """Returns a populated Position object from JSON data."""

        return cls(
            title=data.get("title"),
            organization=data.get("organization"),
            description=data.get("description")
        )

    def __str__(self):
        return f"Position title: {self.title}\nPlace of work: {self.organization}\n" \
               f"Position description: {self.description}"


# Applicant
@dataclass
class Applicant:
    """Represents the applicant profile."""

    name: str
    education: Education
    skills: list[str] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)
    positions: list[Position] = field(default_factory=list)

    @classmethod
    def from_json(cls, json_file: str) -> Self:
        """Returns a populated Applicant object from the data in an applicant profile JSON file."""

        with open(json_file, 'r') as file:
            data = json.load(file)

        # Unpack positions
        positions = []
        for position in data.get("positions", []):
            positions.append(Position.from_json(position))

        return cls(
            name=data.get("name"),
            education=Education.from_json(data.get("education")),
            skills=data.get("skills"),
            languages=data.get("languages"),
            positions=positions
        )

    def __str__(self):

        skills = ", ".join(self.skills)
        languages = ", ".join(self.skills)
        positions = "\n".join([str(p) for p in self.positions])

        return f"Applicant name: {self.name}\nApplicant skills: {skills}\n" \
               f"Applicant speaks the following languages: {languages}\n" \
               f"Applicant education: {self.education}\nPositions the applicant has previously held: \n{positions}"
