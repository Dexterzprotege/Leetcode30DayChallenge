#Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

#Example 1:
#Input: S = "ab#c", T = "ad#c"
#Output: true
#Explanation: Both S and T become "ac".

#Example 2:
#Input: S = "ab##", T = "c#d#"
#Output: true
#Explanation: Both S and T become "".

#Example 3:
#Input: S = "a##c", T = "#a#c"
#Output: true
#Explanation: Both S and T become "c".

#Example 4:
#Input: S = "a#c", T = "b"
#Output: false
#Explanation: S becomes "c" while T becomes "b".

#Note:
#1 <= S.length <= 200
#1 <= T.length <= 200
#S and T only contain lowercase letters and '#' characters.
#Follow up: Can you solve it in O(N) time and O(1) space?

#Approach 1:
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = [] 
        t = []
        for i in S:
            if i == "#":
                if len(s)!=0:
                    s.pop()
            else:
                s.append(i)
        for i in T:
            if i=="#":
                if len(t)!=0:
                    t.pop()
            else:
                t.append(i)
        ss = ''.join(s)
        tt = ''.join(t)
        print(ss,tt)
        if ss == tt:
            return True
        else:
            return False
            
#O(N) time and O(1) Space
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def compress(S):  
            s = 0
            num_back_space = 0
            idx = len(S)-1
            while idx >= 0:
                if S[idx] != "#":
                    if num_back_space == 0:
                        s += ord(S[idx])
                    else:
                        num_back_space -= 1
                else:
                    num_back_space += 1
                idx -= 1
            return s
        return compress(S)==compress(T)
  
