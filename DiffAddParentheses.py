class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        
        res = []
        operator_idx = 0
        while operator_idx < len(input):
            while  operator_idx < len(input) and not(input[operator_idx] in ['+', '-', '*']):
                operator_idx += 1
               
            if operator_idx == len(input):
                break
            left_res = self.diffWaysToCompute(input[:operator_idx])
            right_res = self.diffWaysToCompute(input[operator_idx+1:])
            if input[operator_idx] == '+':
                res.extend([x+y for x in left_res for y in right_res])
            elif input[operator_idx] == '-':
                res.extend([x-y for x in left_res for y in right_res])
            elif input[operator_idx] == '*':
                res.extend([x*y for x in left_res for y in right_res])
            operator_idx += 1
        if not res:
            res = [int(input)]
        return res


            