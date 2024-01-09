# Given a string array words, return an array of all characters that show up in all
# strings within the words (including duplicates). You may return the answer in any order.


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        n_words = len(words)
        if len(words) == 0:
            return []
        common_c = {}
        for c in words[0]:
            common_c[c] = common_c.get(c, 0) + 1
        for w in words:
            current_c = {}
            for c in w:
                current_c[c] = current_c.get(c, 0) + 1
            for c, n in common_c.items():
                common_c[c] = min(n, current_c.get(c, 0))
        result = []
        print(common_c)
        for c, n in common_c.items():
            result.extend([c] * n)
        return result


words = ["bella", "label", "roller"]
# words = ["cool", "lock", "cook"]


############################################


# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.


# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         balanced_counter = 0
#         left_counter, right_counter = 0, 0
#         for c in s:
#             if c == 'L':
#                 left_counter += 1
#             elif c == 'R':
#                 right_counter += 1
#             if left_counter == right_counter:
#                 balanced_counter += 1
#         return balanced_counter


# s = "RLRRLLRLRL"
# s = "RLRRRLLRLL"
s = "LLLLRRRR"


# balanced_counter = 0
# left_counter, right_counter = 0, 0
# for c in s:
#     if c == 'L':
#         left_counter += 1
#     elif c == 'R':
#         right_counter += 1
#     if left_counter == right_counter:
#         balanced_counter += 1


