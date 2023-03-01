# Contains the logic for filling out a cover letter
__author__ = "Matteo Golin"

# Imports
import datetime as dt
from dataclasses import dataclass
from enum import StrEnum
from utils.applicant import Applicant
from utils.job import JobPosting


# Constants
class Fields(StrEnum):
    """Contains the tokens used to signify parameterized template fields."""

    # Short fields
    DATE = "[DATE]"
    EMPLOYER = "[EMPLOYER]"
    EMPLOYER_ADDRESS = "[EMPLOYER ADDRESS]"
    POSITION = "[POSITION]"
    HIRING_MANAGER = "[HIRING MANAGER]"
    APPLICANT = "[APPLICANT]"

    # Long fields
    SKILLS = "[SKILLS SUMMARY]"
    MAIN = "[MAIN BODY]"
    INTEREST = "[SHOW INTEREST]"
    SUMMARY = "[SUMMARY]"


# Letter
@dataclass
class CoverLetter:

    applicant: Applicant
    job_posting: JobPosting
    template_file: str

    def __post_init__(self):
        """Loads the template."""
        with open(self.template_file, 'r') as file:
            self.__template = file.read()

    def populate_boiler_plate(self) -> None:
        """Fills out the boilerplate information to the template"""

        self.__template = self.__template.replace(Fields.DATE, dt.date.today().isoformat())
        self.__template = self.__template.replace(Fields.EMPLOYER, self.job_posting.employer.name)
        self.__template = self.__template.replace(Fields.EMPLOYER_ADDRESS, self.job_posting.employer.address)
        self.__template = self.__template.replace(Fields.POSITION, self.job_posting.position)
        self.__template = self.__template.replace(Fields.APPLICANT, self.applicant.name)
        self.__template = self.__template.replace(Fields.HIRING_MANAGER, self.job_posting.employer.hiring_manager)

    def add_gpt_response(self, response: str) -> None:
        """Parses and adds the response given by ChatGPT to the cover letter template."""

        response, part_4 = response.split("Part 4:")
        response, part_3 = response.split("Part 3:")
        response, part_2 = response.split("Part 2:")
        response, part_1 = response.split("Part 1:")

        self.__template = self.__template.replace(Fields.SKILLS, part_1.strip())
        self.__template = self.__template.replace(Fields.MAIN, part_2.strip())
        self.__template = self.__template.replace(Fields.INTEREST, part_3.strip())
        self.__template = self.__template.replace(Fields.SUMMARY, part_4.strip())

    def save(self, filepath: str) -> None:
        """Saves the cover letter to a .txt file."""

        with open(filepath, 'w') as file:
            file.write(self.__template)

    def __str__(self):
        return self.__template
