# https://leetcode.com/problems/group-anagrams/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# anagrams : 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것

# Method 0 : Using dictionary : 5036 ms	22.7 MB
class Solution:
    def frequency(self, string):
        s_new = " ".join(string).split(" ")
        freq = {}
        for s_ in s_new:
            if s_ not in freq.keys():
                freq[s_] = 1
            else:
                freq[s_] += 1
        freq = sorted(freq.items())
        return freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        counts = list()

        # save the dictionary about same anagrams
        for s in strs:
            if s in dic.keys():
                dic[s].append(s)
            elif len(s) <= 1:
                key_freq = self.frequency(s)
                dic[s] = [key_freq, s]
            else:  # len(s) > 1
                s_freq = self.frequency(s)

                early_stop = False
                for key in dic.keys():
                    key_freq = dic[key][0]

                    if s_freq == key_freq:
                        dic[key].append(s)
                        early_stop = True
                        continue

                if early_stop == False:
                    key_freq = self.frequency(s)
                    dic[s] = [key_freq, s]

        # untie the dictionary
        solution = []
        for key in dic.keys():
            solution.append(dic[key][1:])

        return solution

# Method 1 : Using dictionary and Sorting it : 	92 ms	17.7 MB
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # adding the word to dictionary after sorting
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()
