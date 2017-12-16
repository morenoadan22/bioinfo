import sys
import dna.utils as utils

Debug = False


def viterbi(observations, states, start_probability, transition_probability, emission_probability):
    # The trellis consists of nodes for each possible state at each step in the hidden sequence.
    # Each node has a probability.
    # The edges connecting the nodes are transitions between states.
    trellis = [{}]
    # The current path through the trellis.
    path = {}

    # Add the probabilities of beginning the sequence with each possible state
    for state in states:
        trellis[0][state] = start_probability[state] * emission_probability[state][observations[0]]
        path[state] = [state]

    # Add probabilities for each subsequent state transitioning to each state.
    for observations_index in range(1, len(observations)):
        # Add a new path for the added step in the sequence.
        trellis.append({})
        new_path = {}
        # For each possible state,
        for state in states:
            # Find the most probable state of:
            # The previous most probable state's probability *
            # the probability of the previous most probable state transitioning to the predicted state *
            # The probability that the current observation corresponds to the predicted state
            (probability, possible_state) = max(
                [(trellis[observations_index - 1][y0] * transition_probability[y0][state] * emission_probability[state][observations[observations_index]], y0) for y0 in states])

            # Add the probability of the state occuring at this step of the sequence to the trellis.
            trellis[observations_index][state] = probability
            # Add the state to the current path
            new_path[state] = path[possible_state] + [state]

        path = new_path

    # Make a list of the paths that traverse the entire observation sequence and their probabilities,
    # and select the most probable.
    (probability, state) = max([(trellis[len(observations) - 1][state], state) for state in states])
    # The most probable path, and its probability.
    return (probability, path[state])


if __name__ == '__main__':
    obs = ['x', 'y', 'x', 'z', 'z', 'x', 'y', 'x', 'y', 'y']
    states = ('A', 'B')
    start_p = {'A': 0.5, 'B': 0.5}
    trans_p = {
        'A': {'A': 0.641, 'B': 0.359},
        'B': {'A': 0.729, 'B': 0.271}
    }
    emit_p = {
        'A': {'x': 0.117, 'y': 0.629, 'z': 0.192},
        'B': {'x': 0.097, 'y': 0.42, 'z': 0.483}
    }

    if len(sys.argv) >= 2:
        data = utils.read_file_lines(sys.argv[1])
        obs = list(data[0].strip())
        alpha = data[2].strip().split()
        states = data[4].strip().split()
        start_p = {key: 1 / len(states) for key in states}
        transitions = (data[7].strip().split()[1:], data[8].strip().split()[1:], data[9].strip().split()[1:])
        trans_p = {}
        for i in range(len(transitions)):
            t_row = {}
            for s, t_weight in zip(states, transitions[i]):
                t_row[s] = float(t_weight)
            trans_p[states[i]] = t_row
        emissions = ([data[12].strip().split()[1:], data[13].strip().split()[1:], data[14].strip().split()[1:]])
        emit_p = {}
        for i in range(len(emissions)):
            emit_row = {}
            for a, e_weight in zip(alpha, emissions[i]):
                emit_row[a] = float(e_weight)
            emit_p[states[i]] = emit_row

    print(obs)
    print(states)
    print(start_p)
    print(trans_p)
    print(emit_p)

    actual = ''.join(viterbi(obs,
                             states,
                             start_p,
                             trans_p,
                             emit_p)[1])

    if Debug:
        expected = 'AAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBAAA'
        print('expected: {}'.format(expected))
        print('actual: {}'.format(actual))
        print('assert = {}'.format(expected == actual))
    else:
        print(actual)
