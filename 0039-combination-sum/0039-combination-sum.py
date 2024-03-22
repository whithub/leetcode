class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr_combo = []

        def dfs(idx, curr_combo, total):
            if total == 0:
                res.append(curr_combo.copy())
            if total < 0:
                return
            
            for i in range(idx, len(candidates)):
                num = candidates[i]
                curr_combo.append(num)
                dfs(i, curr_combo, total - num)
                curr_combo.pop()

        dfs(0, curr_combo, target)

        return res

# -------------------------------------------------------
#       Option #1
#         results = []

#         def backtrack(remain, combos, start):
#             if remain == 0:
#                 # make a deep copy of the current combination
#                 results.append(list(combos))
#                 return
#             elif remain < 0:
#                 # exceed the scope, stop exploration.
#                 return
#             for i in range(start, len(candidates)):
#                 # add the number into the combination
#                 combos.append(candidates[i])
#                 # give the current number another chance, rather than moving on
#                 backtrack(remain - candidates[i], combos, i)
#                 # backtrack, remove the number from the combination
#                 #   -- this is needed b/c we've essentially appended a candidates[i] to `combos` list, then found out that "remain < 0" in the prev backtrack() call, therefore, remove it.
#                 combos.pop()

#         backtrack(target, [], 0)

#         return results


# # Output:
# # candidates = [2,3,6,7]
# # target = 7
# # results = []

# # def backtrack(remain, combos, start):
# #     if remain == 0:
# #         print("A:", combos)
# #         results.append(list(combos))
# #         return
# #
# #     elif remain < 0:
# #         print("B:", combos)
# #         return
# #
# #     for i in range(start, len(candidates)):
# #         print("C:", combos)
# #         combos.append(candidates[i])
# #
# #         print("D:", combos)
# #         backtrack(remain - candidates[i], combos, i)
# #
# #         print("E:", combos)
# #         combos.pop()
# #         print("F:", combos)
# # >>> 
# # >>> 
# # backtrack(target, [], 0)
# # C: []
# # D: [2]
# # C: [2]
# # D: [2, 2]
# # C: [2, 2]
# # D: [2, 2, 2]
# # C: [2, 2, 2]
# # D: [2, 2, 2, 2]
# # B: [2, 2, 2, 2]
# # E: [2, 2, 2, 2]
# # F: [2, 2, 2]
# # C: [2, 2, 2]
# # D: [2, 2, 2, 3]
# # B: [2, 2, 2, 3]
# # E: [2, 2, 2, 3]
# # F: [2, 2, 2]
# # C: [2, 2, 2]
# # D: [2, 2, 2, 6]
# # B: [2, 2, 2, 6]
# # E: [2, 2, 2, 6]
# # F: [2, 2, 2]
# # C: [2, 2, 2]
# # D: [2, 2, 2, 7]
# # B: [2, 2, 2, 7]
# # E: [2, 2, 2, 7]
# # F: [2, 2, 2]
# # E: [2, 2, 2]
# # F: [2, 2]
# # C: [2, 2]
# # D: [2, 2, 3]
# # A: [2, 2, 3]
# # E: [2, 2, 3]
# # F: [2, 2]
# # C: [2, 2]
# # D: [2, 2, 6]
# # B: [2, 2, 6]
# # E: [2, 2, 6]
# # F: [2, 2]
# # C: [2, 2]
# # D: [2, 2, 7]
# # B: [2, 2, 7]
# # E: [2, 2, 7]
# # F: [2, 2]
# # E: [2, 2]
# # F: [2]
# # C: [2]
# # D: [2, 3]
# # C: [2, 3]
# # D: [2, 3, 3]
# # B: [2, 3, 3]
# # E: [2, 3, 3]
# # F: [2, 3]
# # C: [2, 3]
# # D: [2, 3, 6]
# # B: [2, 3, 6]
# # E: [2, 3, 6]
# # F: [2, 3]
# # C: [2, 3]
# # D: [2, 3, 7]
# # B: [2, 3, 7]
# # E: [2, 3, 7]
# # F: [2, 3]
# # E: [2, 3]
# # F: [2]
# # C: [2]
# # D: [2, 6]
# # B: [2, 6]
# # E: [2, 6]
# # F: [2]
# # C: [2]
# # D: [2, 7]
# # B: [2, 7]
# # E: [2, 7]
# # F: [2]
# # E: [2]
# # F: []
# # C: []
# # D: [3]
# # C: [3]
# # D: [3, 3]
# # C: [3, 3]
# # D: [3, 3, 3]
# # B: [3, 3, 3]
# # E: [3, 3, 3]
# # F: [3, 3]
# # C: [3, 3]
# # D: [3, 3, 6]
# # B: [3, 3, 6]
# # E: [3, 3, 6]
# # F: [3, 3]
# # C: [3, 3]
# # D: [3, 3, 7]
# # B: [3, 3, 7]
# # E: [3, 3, 7]
# # F: [3, 3]
# # E: [3, 3]
# # F: [3]
# # C: [3]
# # D: [3, 6]
# # B: [3, 6]
# # E: [3, 6]
# # F: [3]
# # C: [3]
# # D: [3, 7]
# # B: [3, 7]
# # E: [3, 7]
# # F: [3]
# # E: [3]
# # F: []
# # C: []
# # D: [6]
# # C: [6]
# # D: [6, 6]
# # B: [6, 6]
# # E: [6, 6]
# # F: [6]
# # C: [6]
# # D: [6, 7]
# # B: [6, 7]
# # E: [6, 7]
# # F: [6]
# # E: [6]
# # F: []
# # C: []
# # D: [7]
# # A: [7]
# # E: [7]
# # F: []
# # >>> results
# # [[2, 2, 3], [7]]