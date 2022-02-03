import os
from dotenv import load_dotenv
from pick import pick
from jira import JIRA

load_dotenv()

# Jira settings
JIRA_URL = os.getenv('JIRA_URL')
JIRA_USERNAME = os.getenv('JIRA_USERNAME')
API_TOKEN = os.getenv('API_TOKEN')


def get_project_key():
    options = os.getenv('PROJECT_KEYS').split('|')
    option, index = pick(options, 'Escolha o projeto: ')
    return option


def get_issue_type():
    options = ['Task', 'Bug', 'Epic']
    option, index = pick(options, 'Escolha o tipo do problema: ')
    return option


def generate_description(title, description):
    if not description:
        return title
    return description


if __name__ == '__main__':
    jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_USERNAME, API_TOKEN))
    issue_project = get_project_key()
    issue_key = get_issue_type()
    title = input('Titulo: ')
    description = generate_description(title, input('Descrição: '))

    new_issue = jira.create_issue(fields={
        'project': {'key': issue_project},
        'summary': title,
        'description': description + '\n [AUTO-GENERATED]',
        'issuetype': {'name': issue_key},
    })

    print('Created issue ', new_issue)
