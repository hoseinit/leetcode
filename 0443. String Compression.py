class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            count = 1
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                count += 1
                chars.pop(i + 1)
            if count > 1:
                for digit in str(count):
                    chars.insert(i + 1, digit)
                    i += 1
            i += 1
        return len(chars)
