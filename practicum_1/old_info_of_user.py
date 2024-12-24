def old_info_of_user(users, username):
    game_count = users[username]["game_count"]
    max_score = users[username]["result"]
    return game_count, max_score
