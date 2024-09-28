class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        for i in range(len(names)):
            names[i] = (heights[i], names[i])
        names.sort()
        names.reverse()
        for i in range(len(names)):
            names[i] = names[i][1]
        return names
