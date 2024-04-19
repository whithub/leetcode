class Solution:
    MOD = (10**9+7)

    def countTexts(self, pressedKeys: str) -> int:
        key_combos = set(['2','22','222','3','33','333','4','44','444','5','55','555','6','66','666','7','77','777','7777','8','88','888','9','99','999','9999'])

        n = len(pressedKeys)+1
        cuml_msg_counts = [0]*n
        cuml_msg_counts[0] = 1

        for end in range(1, n):
            for begin in range(end-1,-1,-1):
                if pressedKeys[begin:end] not in key_combos:
                    break

                cuml_msg_counts[end] = (cuml_msg_counts[end] + cuml_msg_counts[begin]) % self.MOD

        return cuml_msg_counts[-1]



        # Print in console:
        # for end in range(1, n):
        #     for begin in range(end-1,-1,-1):
        #         if pressedKeys[begin:end] not in key_combos:
        #             break
        #         print("begin:", begin)
        #         print("end:", end)
        #         print("total:", cuml_msg_counts[end] + cuml_msg_counts[begin])
        #         cuml_msg_counts[end] = (cuml_msg_counts[end] + cuml_msg_counts[begin]) % MOD
        #         print("cuml_msg_counts:", cuml_msg_counts)
        #         print("-------------------------------")