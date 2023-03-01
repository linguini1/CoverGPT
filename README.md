# GPTCover
### Matteo Golin

Cover letters take quite a bit of time to tailor to specific job postings. I noticed during my application process that
my cover letter didn't seem to make a world of difference when applying to postings. Most of the advice I received 
was that it is far more effective to cast your net wide than to spend time tailoring applications to each job.

Unfortunately, Carleton's job board requires a cover letter to be submitted as part of your application. Cover letters
at Carleton take on a standard format, which makes it difficult to have one standardized cover letter for each job. Even
with only the company name changing, it was enough work to manually change that field every time. To get around this,
I started submitting blank PDFs in the cover letter field so I could send out more applications per day. I figured there
had to be a better option.

Since ChatGPT does a pretty good job of writing cover letters, at least as a starting point, having an AI written letter
is already a leg up from a blank PDF. So I wanted to standardize a pipeline for creating AI cover letters.

This program takes some job parameters and the job posting to create a ChatGPT prompt to write a cover letter for the 
specific job. This auto-prompt is parameterized and has been tested through trial and error. It does not claim to be
perfect.

## Installation
- Python 3.11+
- Modules in `requirements.txt`
- A connection to ChatGPT

Note that this application does not use the OpenAI API to generate cover letters. That would be far superior in terms of
integration, but I do not intend to spend money on API access just for a small program used to make my life easier. For
now, copy-pasting into the online chat will have to do.

## Warnings
I do not endorse using AI written cover letters to apply for positions. Results are not guaranteed, and companies may
already have systems in place for detecting AI written cover letters. ChatGPT may also produce content which is false,
does not accomplish what you want, etc. [Read the OpenAI disclaimer](https://openai.com/terms/).

I recommend that if you use this tool, you modify the cover letter that was written for you, both to ensure correctness
and to ensure that the work is your own in case that is of significance to your potential employer.

## Usage


## Future Development
In the future it would be nice to integrate this with the GPT3 API to prevent copy-pasting between ChatGPT and the 
application.

It would also be very convenient to integrate this with the GitHub API to allow users to pull already written
descriptions of their personal projects + technologies that could be included in the cover letter when relevant.
