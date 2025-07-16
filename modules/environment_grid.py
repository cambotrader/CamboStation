env_memory = []
def log_environment(context_data):
    env_memory.append(context_data)
def fetch_recent(): return env_memory[-5:]
