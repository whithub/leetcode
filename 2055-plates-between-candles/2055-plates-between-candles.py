class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Binary Search Solution using candle indices..
        candles = []
        for i, c in enumerate(s):
            if c == "|":
                candles.append(i)

        if not candles:
            return [0]

        results = []
        for start_idx, end_idx in queries:
            # find the index of the next candle using binary search on the candle indices list...
            #   i.e. the result is the index of the element in the `candles` index list..
            idx_of_closest_starting_candle = self.binary_search(start_idx, candles)
                # ^^ for the start_idx, the next candle's index in the string, must be at or greater than the query start_idx
            idx_of_closest_closing_candle = self.binary_search(end_idx, candles)
                # ^^ for the end_idx, the next candle's index in the string, must be at or lesser than the query end_idx

            # decrement the right index by one since the binary search is right-biased
            if idx_of_closest_closing_candle > 0 and end_idx < candles[idx_of_closest_closing_candle]:
                idx_of_closest_closing_candle -= 1
    
            if idx_of_closest_starting_candle > idx_of_closest_closing_candle:
                results.append(0)
                continue
            
            # the distance of two candles - the count of candles between the range
            closing_candle_idx = candles[idx_of_closest_closing_candle]
            opening_candle_idx = candles[idx_of_closest_starting_candle]
            idx_difference = idx_of_closest_closing_candle - idx_of_closest_starting_candle
            
            results.append(
                closing_candle_idx - 
                opening_candle_idx - 
                idx_difference
            )

        return results

    def binary_search(self, target_idx: int, candles: List[int]):
        l, r = 0, len(candles) - 1
        while l < r:
            mid = (l + r) // 2
            if candles[mid] < target_idx:
                l = mid + 1
            elif candles[mid] > target_idx:
                r = mid
            else:
                return mid # i.e. l
        return r


        
        # Linear solution: SLOW!
        # results = []

        # for span in queries:
        #     start = span[0]
        #     end = span[1]
        #     substring = s[start:end+1]

        #     open_candle_counter = 0
        #     close_candle_counter = 0
        #     max_plate_count = 0
        #     sub_plate_count = 0
        #     for char in substring:
        #         if char == '|' and open_candle_counter == 0:
        #             open_candle_counter += 1
        #         elif char == '|' and open_candle_counter > close_candle_counter:
        #             close_candle_counter += 1

        #         if open_candle_counter > 0 and char == '*':
        #             sub_plate_count += 1
                
        #         if open_candle_counter > 0 and (open_candle_counter == close_candle_counter):
        #             max_plate_count += sub_plate_count
        #             sub_plate_count = 0
        #             open_candle_counter = 1
        #             close_candle_counter = 0

        #     results.append(max_plate_count)

        # return results


        # # for each range/span in queries:
        # #   find subtring of s determined by the span
        # #   iterate through substring, once I hit a candle I can start plate counter
        # #           if I hit a "closing" candle, solidify the plate count -- max_plate_count and sub_plate_count
        # #           if I don't hit a closing candle, sub_plate_count = 0.
        # #       open_candle_counter and close_candle_counter?
        # #   once done with range iteration, add max_plate_count to a results list
        # # return results once done with queries iteration