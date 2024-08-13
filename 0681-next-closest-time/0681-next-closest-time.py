class Solution:
    def nextClosestTime(self, time: str) -> str:
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        
        while True:
            cur = (cur+1) % (24*60)
            is_allowed = True
            for block in divmod(cur,60):
                for digit in divmod(block, 10):
                    if digit not in allowed:
                        is_allowed = False
                        break
            if is_allowed:
                return "{:02d}:{:02d}".format(*divmod(cur, 60))