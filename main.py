from pick import pick
from jira import JIRA

# Jira settings
JIRA_URL = ''
JIRA_USERNAME = ''
API_TOKEN = ''


def get_project_key():
    options = ['PUBSUBJS', 'AUTOSAVE', 'LIBELASTIC', 'SGINT']
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
