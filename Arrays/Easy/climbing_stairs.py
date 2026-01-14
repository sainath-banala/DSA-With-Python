"""
Docstring for Arrays.Easy.climbing_stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Step 1: Only 1 way (take one 1-step). -> input: 1 output: 1

Step 2: 2 ways (1+1 or one 2-step). -> input:2 output: 2

Step 3: 3 ways (1+1+1, 1+2, or 2+1). -> input: 3 output: 3

Step 4: 5 ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2). -> input: 4 output: 5

If we see the above pattern: it was like, 1, 2, 3, 5, ... which fibannoci number:
Intuition: To reach step n, you must have arrived from either step n-1 (via a 1-step jump) or step n-2 (via a 2-step jump). 
Therefore, the total ways to reach n is simply the sum of the ways to reach those two previous steps. 
Start with the base cases (Step 1=1, Step 2=2) and build up to n by adding the previous two results.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        """if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)"""
        from_step_1 = 1
        from_step_2 = 2
        if n==1:
            return from_step_1
        elif n == 2:
            return from_step_2
        else:
            for i in range(3, n+1):
                temp = from_step_1
                from_step_1 = from_step_2
                from_step_2 = from_step_2 + temp
            
            return from_step_2

if __name__ == "__main__":
    solution = Solution()
    step_number = int(input("Enter the step number: "))
    possible_ways_to_reach_step = solution.climbStairs(step_number)
    print(f"Total possible ways to return {step_number}th step is: {possible_ways_to_reach_step}")