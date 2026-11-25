class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        result = []

        # Step 1: Handle sign
        if (numerator < 0) != (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Step 2: Integer part
        result.append(str(numerator // denominator))

        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")

        # Step 3: Store remainder positions
        seen = {}

        while remainder != 0:

            if remainder in seen:
                pos = seen[remainder]
                result.insert(pos, "(")
                result.append(")")
                break

            seen[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)