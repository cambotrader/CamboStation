import os

def list_voice_archives(folder='.', filter_by=None):
    logs = []
    for file in os.listdir(folder):
        if file.startswith("voice_archive_") and file.endswith(".txt"):
            path = os.path.join(folder, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if filter_by and filter_by.lower() not in content.lower():
                continue
            logs.append((file, content[:500] + '...'))
    return logs
