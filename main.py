from mattermostdriver import Driver
from dotenv import dotenv_values
import json

from event_handler.posted_handler import respond_posted


def create_driver(config):
    return Driver({'url': config['server_url'],
                   'login_id': config['bot_username'],
                   'token': config['bot_token'],
                   'scheme': 'https',
                   'port': 443
                   })


def main():
    config = dotenv_values(".env")
    mm = create_driver(config)
    mm.login()

    async def my_event_handler(e):
        message = json.loads(e)
        if message.get('event', None) == 'posted':
            await respond_posted(mm, e)

    mm.init_websocket(my_event_handler)


if __name__ == '__main__':
    main()
