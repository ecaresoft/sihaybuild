from slackclient import SlackClient

def build_passed(build):
    repo = build.repo.name
    branch = build.branch
    committer = build.committer
    token = build.repo.slack_token
    channel = build.repo.slack_channel

    if not token or not channel:
        return "Slack Integration not set"

    message = [
        {
            'fallback': "Build passed on %s/%s by %s" % (repo, branch, committer),
            'pretext': 'Build Passed',
            'author_name': committer,
            'author_icon': "https://avatars.githubusercontent.com/%s" % committer,
            'color': 'good',
            'fields': [
                {
                    'title': 'Repo',
                    'value': repo,
                    'short': True,
                },
                {
                    'title': 'Branch',
                    'value': branch,
                    'short': True
                }
            ]
        }
    ]

    __slack_post(token, channel, message)

def build_failed(build, command):
    repo = build.repo.name
    branch = build.branch
    committer = build.committer
    token = build.repo.slack_token
    channel = build.repo.slack_channel

    if not token or not channel:
        return "Slack Integration not set"

    message = [
        {
            'fallback': "Build failed on %s/%s by %s" % (repo, branch, committer),
            'pretext': 'Build Failed',
            'author_name': committer,
            'author_icon': "https://avatars.githubusercontent.com/%s" % committer,
            'color': 'danger',
            'fields': [
                {
                    'title': 'Command',
                    'value': command
                },
                {
                    'title': 'Repo',
                    'value': repo,
                    'short': True,
                },
                {
                    'title': 'Branch',
                    'value': branch,
                    'short': True
                }
            ]
        }
    ]

    __slack_post(token, channel, message)

def __slack_post(token, channel, message):
    client = SlackClient(token)

    client.api_call(
        'chat.postMessage',
        channel="#%s" % channel,
        attachments=message
    )
