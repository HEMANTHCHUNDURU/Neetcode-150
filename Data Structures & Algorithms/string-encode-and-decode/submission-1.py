class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + '#' + string
        return output

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i<len(s):
            j=i
            while s[j]!="#":
                j=j+1
            len_string = int(s[i:j])
            word = s[j+1:j+1+len_string]
            result.append(word)
            i=j+len_string+1
        return result



