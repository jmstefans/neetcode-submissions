class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += string
            result += "␟"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        curString = ""
        for character in s:
            if character != "␟":
                curString += character
            else:
                result.append(curString)
                curString = ""
        return result