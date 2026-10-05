class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) 
            result += "#" 
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        length = ""
        offset = 0
        result = []
        while offset < len(s):
            if s[offset] != "#":
                length += s[offset]
                offset += 1
            else:
                length = int(length)
                result.append(s[offset+1:offset+length+1])
                offset += length + 1
                length = ""
        return result
                

