# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd",
# and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because
# it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.


# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/


# CAN'T DO THIS SORRY


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        results = []
        permutations = self.gen_permutations(words)
        checkblock_length = len(permutations[0]) * len(permutations[0][0])
        endpoint = len(s) - checkblock_length
        for i in range(endpoint + 1):
            for perm in permutations:
                if s[i:i + checkblock_length] == ''.join(perm):
                    if i not in results:
                        results.append(i)
                    continue
        return results

    def gen_permutations(self, words):
        n = len(words)
        if n == 0:
            return [[]]
        permutations = []
        for perm in self.gen_permutations(words[:-1]):
            for i in range(n):
                new_perm = perm[:]
                new_perm.insert(i, words[n - 1])
                permutations.append(new_perm)
        return permutations


s = "barfoothefoobarman"
words = ["foo", "bar"]


# s = 'wordgoodgoodgoodbestword'
# words = ["word", "good", "best", "word"]


# words = [  # 18! = 6_402_373_705_728_000 permutations so we cannot use this approach
#     "dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg",
#     "ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"
# ]


# def generate_permutations(n):
#     if n == 0:
#         return [[]]
#     result = []
#     for perm in generate_permutations(n-1):
#         for i in range(n):
#             new_perm = perm[:]
#             new_perm.insert(i, n-1)
#             result.append(new_perm)
#     return result


# NEW APPROACH:  ISSUE: can't check appended indices are 'unique', could be repetition of same word
# simply check if a word is present at any indices and put the indices down,
# repeat for all the words
# check if there's a succession of indices as long as the whole concat words list,
# if so that's a permutation of words
# as indices append a string like '6-7-8-9' then use split on - to get a list, then turn into int and concat
#
#
# results = []
# length = len(words[0])
# for w in words:
#     for i in range(len(s) - length):
#         if w == s[i:i+length]:
#             r = '-'.join(str(j) for j in range(i, i+length))
#             results.append(r)


# NEW APPROACH:
# from the list of words check directly if the first is present in the w,
# if so get the indices and pop the word from the words list,
# then go left and right to check other words and so on and so on


length = len(words[0])
indices = []
ww = words[:]
w = words[-1]
for i in range(len(s)):
    if s[i:i+length] == w:
        indices.append(i)
ww.pop()
block_1 = [indices[0], indices[0]+length]
block_2 = [indices[1], indices[1]+length]


def func(block, word):
    flag = True
    new_indices = block[:]
    # check left
    if block[0] - length >= 0:
        if s[block[0]-length: block[0]] == word:
            new_indices.insert(0, block[0] - length)
            flag = False
    # check right
    if flag and block[-1] + length < len(s):
        if flag and s[block[-1]: block[-1] + length] == word:
            new_indices.append(block[-1] + length)
    return [new_indices[0], new_indices[-1]]


a = func(block_1, words[0])


# def func(warudo, indices, s):
#     def check_left(w, idx):
#         try:
#             if s[idx-4:idx] == w:
#                 indices.append
#     def check_right(w):
#         pass

