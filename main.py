# Fills out a cover letter template and provides a ChatGPT prompt to create the cover letter
__author__ = "Matteo Golin"

# Imports
from utils.applicant import Applicant
from utils.job import JobPosting, Employer
from utils.letter import CoverLetter
from utils.prompt import chatgpt_prompt
from cli import parser
import os
from typing import Optional

# Constants
APPLICANT_PROFILE: str = "./applicant-profile.json"
LETTER_TEMPLATE_FILE: str = "./resources/letter_template.txt"
PROMPT_TEMPLATE_FILE: str = "./resources/prompt.txt"


# Logic separations
def prompt_logic(applicant: Applicant, job_posting: JobPosting, outfile: Optional[str]) -> None:
    """Executes the logic for creating a prompt."""

    prompt = chatgpt_prompt(applicant, job_posting, PROMPT_TEMPLATE_FILE)  # Create prompt

    if outfile:
        with open(outfile, "a") as file:
            file.write(prompt)
        exit()

    # Otherwise just print
    print(f"{'Prompt Follows':=^100}")
    print(prompt)


# Main
def main():

    # Unpack arguments
    args = vars(parser.parse_args())
    print(args)
    subcommand = args.get("subcommand")

    if subcommand is None:
        raise SystemExit("Use -h for a list of commands.")

    job_posting_file = args.get("job file")
    output_file = args.get("o")

    # Load applicant
    applicant = Applicant.from_json(APPLICANT_PROFILE)

    # Get job posting information
    employer = Employer(
        name=input("Company name: "),
        address=input("Company address: "),
        hiring_manager=input("Hiring manager (hit enter if unknown): ")
    )

    with open(job_posting_file, 'r') as file:
        job_posting = JobPosting(
            employer=employer,
            position=input("Position name: "),
            raw_posting=file.read()
        )

    # Decide what to do with command
    if subcommand == "letter":

        # If continuous, generate the prompt first
        if args.get("c"):
            prompt_logic(applicant, job_posting, outfile=None)

        # Wait for user to fill out the gpt file before
        input("Take a moment to paste ChatGPT's response into the 'gpt file' before hitting Enter: ")

        # Create cover letter
        letter = CoverLetter(
            applicant=applicant,
            job_posting=job_posting,
            template_file=LETTER_TEMPLATE_FILE
        )

        # Open GPT response
        gpt_file = args.get("gpt file")
        with open(gpt_file, 'r') as file:
            gpt_response = file.read().strip()

        # Add GPT generated text to template
        letter.populate_boiler_plate()
        letter.add_gpt_response(gpt_response)

        if output_file:
            letter.save(output_file)
        else:
            if not os.path.exists("./letters"):
                os.mkdir("./letters")
            letter.save(f"./letters/{letter.job_posting.position}.txt")

    if subcommand == "prompt":
        prompt_logic(applicant, job_posting, output_file)

    
if __name__ == "__main__":
    main()
