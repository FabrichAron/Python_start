def change_user_info(users, username, score):
    old_score = users[username]["result"]
    old_game_count = users[username]["game_count"]
    if old_score > score:
        users[username] = {"result": old_score, "game_count": old_game_count + 1}
        return users
    else:
        users[username] = {"result": score, "game_count": old_game_count + 1}
        return users
