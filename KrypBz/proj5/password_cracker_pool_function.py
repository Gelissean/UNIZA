def unlock_users_pool(user):
    user.attempt_unlocking()
    return user