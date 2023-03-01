# Contains the commands for the CLI that will run the program
__author__ = "Matteo Golin"

# Imports
import argparse
import os

# Constants
DESCRIPTION: str = "A command line tool to help generate cover letters from a template and a pre-populated ChatGPT " \
                   "prompt."


# Filepath validator
def file_path_exists(arg) -> str:
    """Checks if a passed filepath argument is a valid filepath."""
    if not os.path.exists(arg):
        raise ValueError(f"{arg} is not a valid filepath!")
    else:
        return arg


def file_path_valid(arg) -> str:
    """Checks if a passed file path could exist."""

    try:
        file = open(arg, 'w')
        file.close()
        return arg
    except FileNotFoundError:
        raise ValueError(f"{arg} is not a valid filepath!")


# Parser
parser = argparse.ArgumentParser(description=DESCRIPTION)
subparsers = parser.add_subparsers(dest="subcommand")

# Commands
generate_prompt = subparsers.add_parser("prompt", help="Generates a ChatGPT prompt for writing the cover letter.")

generate_prompt.add_argument(
    "job file",
    help="Path to the .txt file containing the job posting.",
    type=file_path_exists
)

generate_prompt.add_argument(
    "-o",
    help="Output .txt file for the prompt. If not given, prompt is printed to the console.",
    type=file_path_valid
)

generate_letter = subparsers.add_parser(
    "letter",
    help="Fills out a cover letter template with applicant info and the response given by ChatGPT."
)

generate_letter.add_argument(
    "job file",
    help="Path to the .txt file containing the job posting.",
    type=file_path_exists
)

generate_letter.add_argument(
    "gpt file",
    type=file_path_exists,
    help="Path to the .txt file containing the response provided by ChatGPT."
)

generate_letter.add_argument(
    "-o",
    help="Output .txt file for the letter. If not given, the letter is written to the /letters directory.",
    type=file_path_valid,
)

generate_letter.add_argument(
    "-c",
    help="Makes the prompt and letter generation continuous. Paste ChatGPT's response into the 'gpt file' parameter "
         "when prompted. Then continue.",
    action="store_true"
)
