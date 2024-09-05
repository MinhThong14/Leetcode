class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        time_minutes = int(time[:2]) * 60 + int(time[3:])
        
        time_minutes += 1
        
        time_chars = set()
        for char in time:
            if char != ":":
                time_chars.add(int(char))
    
        while True:
            if time_minutes == 1440:
                time_minutes = 0
            hours = time_minutes // 60
            minutes = time_minutes % 60
            
            hour_first_digit = hours // 10
            hour_second_digit = hours % 10 
            
            minutes_first_digit = minutes // 10
            minutes_second_digit = minutes % 10
            
            if hour_first_digit in time_chars and hour_second_digit in time_chars and minutes_first_digit in time_chars and minutes_second_digit in time_chars:
                return str(hour_first_digit) + str(hour_second_digit) + ":"+ str(minutes_first_digit) + str(minutes_second_digit)
        
            time_minutes += 1
            
            
        
        