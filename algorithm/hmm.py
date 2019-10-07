import tensorflow as tf
import tensorflow_probability as tfp

sess = tf.Session()

tfd = tfp.distributions
'''
states = ('Rainy', 'Sunny', 'Cloudy')

observations = ('Walk', 'Shop', 'Clean', 'Clean')

start_probability = {'Rainy': 0.5, 'Sunny': 0.3, 'Cloudy': 0.2}

transition_probability = {
    'Rainy': {'Rainy': 0.5, 'Sunny': 0.2, 'Cloudy': 0.3},
    'Sunny': {'Rainy': 0.1, 'Sunny': 0.6, 'Cloudy': 0.3},
    'Cloudy': {'Rainy': 0.4, 'Sunny': 0.3, 'Cloudy': 0.3},
}

emission_probability = {
    'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5},
    'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1},
    'Cloudy': {'Walk': 0.3, 'Shop': 0.4, 'Clean': 0.3},
}
'''

hidden_map = ['Rainy', 'Sunny', 'Cloudy']
state_map = ['Walk', 'Shop', 'Clean']
initial_distribution = tfd.Categorical(probs=[0.5, 0.3, 0.2])

transition_distribution = tfd.Categorical(probs=[
                                                [0.5, 0.2, 0.3],
                                                [0.1, 0.6, 0.3],
                                                [0.4, 0.3, 0.3],
                                                ])

observation_distribution = tfd.Categorical(probs=[
                                                [0.1, 0.4, 0.5],
                                                [0.6, 0.3, 0.1],
                                                [0.3, 0.4, 0.3],
                                                ])

observed_states = ['Walk', 'Shop', 'Clean', 'Clean', 'Shop', 'Shop', 'Walk']
encode_observed_states = []
for state in observed_states:
    encode_observed_states.append(state_map.index(state))
    
# This gives the hidden Markov model:
model = tfd.HiddenMarkovModel(
    initial_distribution=initial_distribution,
    transition_distribution=transition_distribution,
    observation_distribution=observation_distribution,
    num_steps=len(encode_observed_states)
    )

# We can now compute the most probable sequence of hidden states:

result = model.posterior_mode(encode_observed_states)
res = sess.run(result)

hidden_states = []
for state in res:
    hidden_states.append(hidden_map[state])


print('observed_states: ',observed_states)
print('hidden_states:   ',hidden_states)

prob = model.prob(encode_observed_states)
print('prob: ', sess.run(prob))


