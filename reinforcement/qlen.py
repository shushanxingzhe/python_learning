import numpy as np
import pandas as pd


np.random.seed(2) # reproducible

N_STATE = 6     # the lenght of 1 dimensional world
ACTIONS = ['left', 'right']     #available actions
EPSILON = 0.9       # greedy policy
ALPHA = 0.1     # learning rate
LAMBDA = 0.9    # discount factor
MAX_EPISODES = 13   # maximum episodes
FRESH_TIME = 0.3        # fresh time for one move

def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states,len(actions))),
        columns=actions
    )
    print(table)
    return table

def choose_action(state, q_talbe):
    state_action = q_talbe.iloc[state,:]
    if (np.random.uniform() > EPSILON) or (state_action.all() ==0):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_action.argmax()
    return action_name

