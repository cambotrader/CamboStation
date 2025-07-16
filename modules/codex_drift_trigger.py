from conviction_drift import track_drift
codex_drift = track_drift(old_belief_codex, new_belief_codex)
memory["belief_shift"].extend(codex_drift)
