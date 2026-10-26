class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            letters = 0

            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            count = j - i
            gaps = count - 1

            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = (maxWidth - letters) // gaps
                extra = (maxWidth - letters) % gaps

                parts = []

                for k in range(i, j - 1):
                    parts.append(words[k])
                    parts.append(" " * (spaces + (1 if k - i < extra else 0)))

                parts.append(words[j - 1])
                line = "".join(parts)

            result.append(line)
            i = j

        return result