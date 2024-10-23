from mattermostdriver import Driver
from dotenv import dotenv_values
from types import SimpleNamespace
import json


def main():
    config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

    mm = Driver({'url': config['server_url'],
                 'login_id': config['bot_username'],
                 'token': config['bot_token'],
                 'scheme': 'https',
                 'port': 443
                 })
    mm.login()
    team = mm.teams.get_team_by_name('HQ')
    print('team')
    print(team)

    # users = mm.users.get_users()
    # print()

    # channel = driver.channels.get_channel_by_name(team['id'], 'channel_name')
    #
    # @mm.on('message')
    # def handle_message(post, **kwargs):
    #     if post['message'] == 'hello':
    #         mm.posts.create_post({
    #             'channel_id': post['channel_id'],
    #             'message': 'Hi there! ' + post['channel_id']
    #         })

    async def my_event_handler(e):
        message = json.loads(e)
        print(message)

        if message.get('event', None) == 'posted':
            await respond_posted(e)

    async def respond_posted(message):
        print('posted')
        message_object = json.loads(message, object_hook=lambda d: SimpleNamespace(**d))
        print(message_object)
        # print(message['data']['post']['message'])
        post = json.loads(message_object.data.post, object_hook=lambda d: SimpleNamespace(**d))

        print(post)

        # ignore own messages
        if post.user_id == 'qwrrotfuniyut8djj6e7wppypo':
            return

        if post.message == 'hello':
            await  hello_respond(message_object.data.channel_display_name, post.channel_id)

    async def hello_respond(username, channel_id):
        mm.posts.create_post({
            'channel_id': channel_id,
            'message': 'Hi there! ' + username
        })

    mm.init_websocket(my_event_handler)


if __name__ == '__main__':
    main()
