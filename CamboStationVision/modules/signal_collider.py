collider_log = []
def collide_signals(signalA, signalB):
    result = "merge" if signalA == signalB else "conflict"
    collider_log.append({
        "signalA": signalA,
        "signalB": signalB,
        "result": result,
        "timestamp": timestamp_now()
    })
    return collider_log[-1]
