class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create a hashmap that is 26 units long to keep track of each letter
        #for each string in the input, create a count array of size 26 with all zeros
        # for each character c in the string increment count for that specific letter
        #convert count array to tuple
        #
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())