from fusion_poll import composite_vote
from agent_ghost import vote as ghost_vote
from agent_prophet import vote as prophet_vote
from agent_contrarian import vote as contrarian_vote

signal_cluster = gather_signals()
final_vote = composite_vote(
    contrarian_vote(signal_cluster),
    prophet_vote(signal_cluster),
    ghost_vote(signal_cluster)
)
memory["fusion_consensus"] = final_vote
