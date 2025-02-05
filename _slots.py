from memory_profiler import profile

class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class SlotsUserProfile:
    __slots__ = ['username', 'email']

    def __init__(self, username, email):
        self.username = username
        self.email = email

@profile
def profile_creation(my_class): 
    profiles = [my_class(f"user{i}", f"user{i}@example.com") for i in range(1000000)]
    return profiles


profile_creation(UserProfile)
profile_creation(SlotsUserProfile)
