# Prairielearn Lab Tool

_For people tired of refreshing Prairielearn all the time_

This Python script lists instances opened within the last 2 hours and sorts them into open and closed columns.
You can also search for students. Made using the [Prairielearn api](https://prairielearn.readthedocs.io/en/latest/api/).


## Requirements
 * Python 3+

## Setup
1. Download the repo from github
2. Get your api token from [Prairielearn](https://ca.prairielearn.org/pl/settings). Generate a new token and copy it.
3. Paste your token into `token` field in `config.json`
4. Get the appropriate assessment id for the current lab
   * APSC 160 Lab 4's URL  looks like https://ca.prairielearn.org/pl/course_instance/1678/instructor/assessment/**15959**/questions
   * The assessment id is 15959
5. Paste assessment id into `assessment_id` field in `config.json`

## Usage
1. Run `prairielearn-lab-tool.py` using Python
2. Enter a search term and press enter to search for a string
3. Leave search term blank and press enter to refresh

## Bugs
Probably some


## Notes
Don't spam Prairielearn too much, I don't think it can take it.
