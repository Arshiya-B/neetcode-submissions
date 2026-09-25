class Solution:

    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, s):
        result = []
        i = 0

        while i < len(s):

            # Find the #
            j = i
            while s[j] != "#":
                j += 1

            # Read the number before #
            length = int(s[i:j])

            # Read exactly 'length' characters
            word = s[j + 1 : j + 1 + length]

            result.append(word)

            # Move to the next encoded string
            i = j + 1 + length

        return result