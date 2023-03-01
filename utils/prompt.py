# Contains the logic for creating a ChatGPT prompt
__author__ = "Matteo Golin"

# Imports
from utils.applicant import Applicant
from utils.job import JobPosting
from enum import StrEnum


# Constants
class Fields(StrEnum):
    """Lists the fields that are present in the prompt template."""

    APPLICANT = "[APPLICANT]"
    JOB_POSTING = "[JOB POSTING]"
    APPLICANT_INFO = "[APPLICANT INFO]"
    EMPLOYER_INFO = "[EMPLOYER INFO]"
    POSITION = "[POSITION]"
    EMPLOYER = "[EMPLOYER]"


# Logic
def chatgpt_prompt(applicant: Applicant, job_posting: JobPosting, prompt_template: str) -> str:
    """Returns a prompt generated using job posting and applicant information."""

    # Load template
    with open(prompt_template, 'r') as file:
        template = file.read()

    # Populate template
    template = template.replace(Fields.APPLICANT, applicant.name)
    template = template.replace(Fields.EMPLOYER, job_posting.employer.name)
    template = template.replace(Fields.POSITION, job_posting.position)
    template = template.replace(Fields.JOB_POSTING, job_posting.raw_posting)
    template = template.replace(Fields.EMPLOYER_INFO, str(job_posting.employer))
    template = template.replace(Fields.APPLICANT_INFO, str(applicant))

    return template
