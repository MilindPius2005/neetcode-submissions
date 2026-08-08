class Solution:
    def groupAnagrams(self, strs):

        group = {}

        for s in strs:

            # Count a,b,c,...z
            count = [0] * 26

            for c in s:

                # Convert character to index 0-25
                index = ord(c) - ord("a")

                # Increase frequency
                count[index] += 1

            # Convert list to tuple so it can be a key
            key = tuple(count)

            # Create group if it doesn't exist
            if key not in group:
                group[key] = []

            # Add the word to its group
            group[key].append(s)

        return list(group.values())