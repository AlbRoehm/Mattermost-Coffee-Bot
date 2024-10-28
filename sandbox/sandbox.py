import random

from dotenv import dotenv_values

from main import create_driver

if __name__ == '__main__':
    config = dotenv_values("../.env")

    mm = create_driver(config)
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

    users = mm.users.get_users_by_ids(options=town_square_user_ids)
    print('User information for number of users', len(users))
    print(users)

    filtered_active_users = [user for user in users if
                             (user.get('delete_at', None) == 0 and user.get('is_bot', None) != True)]
    print('Filtered users with delete_at value:', len(filtered_active_users))
    print(filtered_active_users)

    first_names = [user['first_name'] for user in filtered_active_users]
    print('First names of filtered users:')
    print(first_names)

    # filtered_users_count = len(filtered_users)
    # print('Number of filtered users with delete_at value:')
    # print(filtered_users_count)
    #
    random_user = (random.choice(filtered_active_users))
    print('random_user of townsquare')
    print(random_user['username'])

    # users = mm.users.get_users()
    # print('users')
    # print(users)
    # # Assuming `users` is a list of user dictionaries
    # random_user = random.choice(users)
    # print(random_user)
