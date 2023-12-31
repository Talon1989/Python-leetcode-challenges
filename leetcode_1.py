import numpy as np


# def backspaceCompare(s, t):
#     idx = 0
#     while idx < len(s):
#         if s[idx] == '#':
#             if idx == 0:
#                 s = s[1:]
#             else:
#                 before = s[:idx-1]
#                 after = s[idx+1:]
#                 s = before + after
#             idx = 0
#         idx += 1
#     idx = 0
#     while idx < (len(t)):
#         if t[idx] == '#':
#             if idx == 0:
#                 t = t[1:]
#             else:
#                 before = t[:idx-1]
#                 after = t[idx+1:]
#                 t = before + after
#             idx = 0
#         idx += 1
#     s = ''.join(char for char in s if char != '#')
#     t = ''.join(char for char in t if char != '#')
#     return s == t


# s = 'ab#c'
# t = 'ad#c'
# s = "c##vnvr"
# t = "#c##vnvr"
s = "ab##"
t = "c#d#"


# BACK-SPACE COMPARE 2
def get_indices(text: str):
    indices = []
    for index, char in enumerate(text):
        if char == '#':
            indices.append(index)
    return np.array(indices)


def remove_chars_at_indices(text: str, indices: set):
    indices = sorted(indices, reverse=True)  # Sort indices in reverse order to avoid shifting issues
    for index in indices:
        if 0 <= index < len(text):
            text = text[:index] + text[index+1:]
    return text


indices_2 = get_indices(s)
indices_1 = indices_2 - 1
indices_s = set(indices_2).union(indices_1)
ss = remove_chars_at_indices(s, indices_s)

indices_2 = get_indices(t)
indices_1 = indices_2 - 1
indices_t = set(indices_2).union(indices_1)
tt = remove_chars_at_indices(t, indices_t)



def backspaceCompare(self, s, t):

    # dealing with s
    indices_s = []
    for index, char in enumerate(s):
        if char == '#':
            indices_s.append(index)
    indices_s_prev = []
    # for value in indices_s:
    #     indices_s_prev.append(value-1)
    for i in range(len(indices_s)):
        try:
            if indices_s[i+1] == indices_s[i] + 1:
                indices_s_prev.append(indices_s[i] - 2)
        except IndexError:
            pass
        indices_s_prev.append(indices_s[i] - 1)
    ind_s = set(indices_s).union(indices_s_prev)
    for index in ind_s:
        if 0 <= index < len(s):
            s = s[:index] + s[index+1:]

    # dealing with t
    indices_t = []
    for index, char in enumerate(t):
        if char == '#':
            indices_t.append(index)
    indices_t_prev = []
    # for value in indices_t:
    #     indices_t_prev.append(value-1)
    for i in range(len(indices_t)):
        try:
            if indices_t[i+1] == indices_t[i] + 1:
                indices_t_prev.append(indices_t[i] - 2)
        except IndexError:
            pass
        indices_t_prev.append(indices_t[i] - 1)
    ind_t = set(indices_t).union(indices_t_prev)
    for index in ind_t:
        if 0 <= index < len(t):
            t = t[:index] + t[index+1:]

    return s == t


# i = 0
# while i < len(s):
#     print(i)
#     print(len(s))
#     print()
#     if i < len(s) - 1 and s[i + 1] == '#':
#         i += 2  # Skip the character before and after 'o'
#     else:
#         s += s[i]
#         i += 1
#
# print(s)


# get all indices of # and all indices of #-1 to remove
# check for sequential ##
