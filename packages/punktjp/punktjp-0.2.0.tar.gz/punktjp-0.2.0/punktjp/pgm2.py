def print_prog():
    print(
        """
dfa = {
    'q0': {'a':'q1','b':'q0'},
    'q1': {'a':'q0','b':'q1'}
}
start_state = 'q0'
end_states = {'q1'}
alphabets = {'a','b'}
def design_dfa(input_str):
    cur_state = start_state

    for char in input_str:
        cur_state = dfa[cur_state][char]

    return cur_state in end_states
input_str = input("Enter the String: ")
if design_dfa(input_str):
    print("Accepted")
else:
    print("Rejected")
"""
    )
