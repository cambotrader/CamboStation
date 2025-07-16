def composite_vote(contrarian, prophet, ghost):
    votes = {"BUY": 0, "SELL": 0, "PASS": 0}
    for vote in [contrarian, prophet, ghost]:
        votes[vote] += 1
    return max(votes, key=votes.get)
