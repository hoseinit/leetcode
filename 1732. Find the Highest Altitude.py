class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        currentAltitude = 0

        for i in range(len(gain)):
            currentAltitude += gain[i]
            maxAltitude = max(maxAltitude, currentAltitude)

        return maxAltitude
