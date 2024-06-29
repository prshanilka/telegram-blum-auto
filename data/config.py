# api id, hash
API_ID="29974238"
API_HASH="26bc6eed922dccac2a0821766bd47f00"

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY': [5, 15],   # delay between play in seconds
    'ERROR_PLAY': [60, 180],    # delay between errors in the game in seconds
}
# Use proxies or not
PROXY = False

# Play drop game
PLAY_GAMES = True

# points with each play game; max 280
POINTS = [200, 230]

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Farm points']

# session folder (do not change)
WORKDIR = "sessions/"


ACCOUNT_PER_ONCE = 3
