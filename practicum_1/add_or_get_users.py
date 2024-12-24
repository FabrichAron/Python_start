def add_or_get_users(users, username):
    if username not in users:
        users[username] = {"result": 0, "game_count": 0}
    return users
