class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        l = []
        deck.sort(reverse = True)
        for i in deck:
            l = [i]+l[-1:]+l[:-1]
        return l