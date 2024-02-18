def print_prog():
    print(
        """
nfa = {
    ("q0", "a"): {"q0", "q1"},
    ("q0", "b"): {"q0"},
    ("q1", "a"): {"q2"},
    ("q1", "b"): {"q2"},
    ("q2", "a"): {"q3"},
    ("q2", "b"): {"q3"},
}
start_state = {"q0"}
end_states = {"q3"}


def dfs(current_states, input_str, index):
    if index == len(input_str):
        return current_states & end_states
    return any(
        dfs(nfa.get((state, input_str[index]), set()), input_str, index + 1)
        for state in current_states
    )


input_str = input("Enter the string: ")
print("Accepted" if dfs(start_state, input_str, 0) else "Rejected")

"""
    )
