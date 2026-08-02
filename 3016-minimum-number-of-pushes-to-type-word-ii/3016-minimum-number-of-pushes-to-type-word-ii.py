class Solution:
    def minimumPushes(self, word: str) -> int:

        # Step 1: Count frequencies manually
        freq = {}

        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Get only the frequencies
        counts = list(freq.values())

        # Step 3: Sort in descending order
        counts.sort(reverse=True)

        ans = 0

        # Step 4: Calculate total pushes
        for i in range(len(counts)):
            pushes = (i // 8) + 1
            ans += counts[i] * pushes

        return ans