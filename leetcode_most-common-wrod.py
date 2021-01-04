# https://leetcode.com/problems/most-common-word/
# 0 번째 외의 방법은 전부 "파이썬 알고리즘 인터뷰"를 참조함

# Method 0 : Using List comprehension : 36 ms	14.5 MB
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        # pre-processing
        paragraph=re.sub('[^a-z ]',' ',paragraph)
        # remove banned words
        words=[word for word in paragraph.split(" ") if word not in banned+['']]
        # most-common-word
        freq={}
        for word in words:
            if word not in freq.keys():
                freq[word]=1
            else:
                freq[word]+=1
        freq=sorted(freq.items(),reverse=True,key=lambda x:x[1])
        for key,_ in freq:
            return key

# Method 1: List comprehension, counter : 	36 ms	14.3 MB
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]
        counts = collections.Counter(words)

        # return the frist index of the most common word
        return counts.most_common(1)[0][0]