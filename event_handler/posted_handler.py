from mattermostdriver import Driver
from types import SimpleNamespace
import random
import json


async def respond_posted(mm: Driver, message):
    message_object = json.loads(message, object_hook=lambda d: SimpleNamespace(**d))
    post = json.loads(message_object.data.post, object_hook=lambda d: SimpleNamespace(**d))

    # ignore own messages
    if post.user_id == 'qwrrotfuniyut8djj6e7wppypo':
        return

    if channel_is_not_direct_message(mm, post.channel_id):
        return

    print('Responding to received message:', message)

    match post.message:
        case 'hello':
            await hello_respond(mm, message_object.data.channel_display_name, post.channel_id)
        case 'coffee':
            await coffee_respond(mm, post.channel_id)
        case 'help':
            await help_respond(mm, post.channel_id)


def channel_is_not_direct_message(mm: Driver, channel_name):
    channel_info = mm.channels.get_channel(channel_name)
    return channel_info['type'] != 'D'


async def help_respond(mm, channel_id):
    mm.posts.create_post({
        'channel_id': channel_id,
        'message': "Hey, meatbag! I'm Bender, your friendly neighborhood robot. I'm here to help you with"
                   " all your boring human tasks. Just tell me what you need, and I'll do my best to assist "
                   "you. But remember, I'm not your slave, so don't get any funny ideas. Now, what do you "
                   "want? A **coffee**? or just say **hello**? Try either of those keywords and see what happens."})


async def coffee_respond(mm, channel_id):
    mm.posts.create_post({
        'channel_id': channel_id,
        'message': "Hey, meatbag! You know what you should do? Call up @" + fetch_random_user(
            mm) + " and have a coffee chat. Yeah, I said it. Coffee! I don’t need it, but you humans seem "
                  "to love that bean juice. Who knows, maybe you'll discuss something that doesn’t bore me"
                  " half to death. Do it, or I’ll steal your wallet! Just kidding... "
                  "or am I? *maniacal robot laughter*"
    })


async def hello_respond(mm: Driver, username, channel_id):
    mm.posts.create_post({
        'channel_id': channel_id,
        'message': 'Hi there! ' + username
    })


def fetch_random_user(mm: Driver) -> str:
    town_square_users = mm.channels.get_channel_members('ysr5gcdy6jds8edzcxpcekem1c', params={'per_page': '500'})
    town_square_user_ids = [user['user_id'] for user in town_square_users]
    users = mm.users.get_users_by_ids(options=town_square_user_ids)
    filtered_active_users = [user for user in users if
                             (user.get('delete_at', None) == 0  # user not deleted
                              and user.get('is_bot', None) != True  # user not a bot
                              and user.get('id', None) != 'qwrrotfuniyut8djj6e7wppypo')]  # user not bender
    random_user = (random.choice(filtered_active_users))
    return random_user['username']
