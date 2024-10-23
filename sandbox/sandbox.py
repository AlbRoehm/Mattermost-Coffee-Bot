import random

from mattermostdriver import Driver
from dotenv import dotenv_values
from types import SimpleNamespace
import json

if __name__ == '__main__':
    config = dotenv_values("../.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

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

    town_square_users = mm.channels.get_channel_members('ysr5gcdy6jds8edzcxpcekem1c', params={'per_page': '500'})
    print('town_square members')
    print("Number of users in Townsquare", len(town_square_users), town_square_users)

    town_square_user_ids = [user['user_id'] for user in town_square_users]
    print('User IDs in Town Square:')
    print(town_square_user_ids)

    # users = mm.users.get_users(params={'user_ids': town_square_user_ids, 'per_page': '500'})
    # print('User information for number of users', len(users))
    # print(users)
    #
    # filtered_users = [user for user in users if user.get('delete_at', None) == 0]
    #
    # print('Filtered users with delete_at value:')
    # print(filtered_users)
    #
    # filtered_users_count = len(filtered_users)
    # print('Number of filtered users with delete_at value:')
    # print(filtered_users_count)
    #
    # random_user = mm.users.get_user(random.choice(filtered_users)['username'])
    # print('random_user of townsquare')
    # print(random_user)

    # users = mm.users.get_users()
    # print('users')
    # print(users)
    # # Assuming `users` is a list of user dictionaries
    # random_user = random.choice(users)
    # print(random_user)
