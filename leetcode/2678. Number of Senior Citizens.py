from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for passenger_data in details:
            if int(passenger_data[-4:-2]) > 60:
                counter += 1
        return counter
