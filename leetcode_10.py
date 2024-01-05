# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd",
# and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because
# it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.


# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/


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


# s = "barfoothefoobarman"
# words = ["foo", "bar"]
# s = 'wordgoodgoodgoodbestword'
# words = ["word", "good", "best", "word"]
s = "wordgoodgoodgoodbestword"
# words = ["word", "good", "best", "good"]

words = [  # 18! = 6_402_373_705_728_000 so we cannot use this approach
    "dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg",
    "ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"
]


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


def gen_permutations(words):
    n = len(words)
    if n == 0:
        return [[]]
    result = []
    for perm in gen_permutations(words[:-1]):
        for i in range(n):
            new_perm = perm[:]
            new_perm.insert(i, words[n - 1])
            result.append(new_perm)
    return result


results = []
permutations = gen_permutations(words)
# checkblock_length = len(permutations[0]) * len(permutations[0][0])
# endpoint = len(s) - checkblock_length
# for i in range(endpoint+1):
#     # print(i)
#     for perm in permutations:
#         if s[i:i + checkblock_length] == ''.join(perm):
#             if i not in results:
#                 results.append(i)
#             continue
# print(results)


# NEW APPROACH:
# from the list of words check directly if the first is present in the w,
# if so get the indices and pop the word from the words list,
# then go left and right to check other words and so on and so on
