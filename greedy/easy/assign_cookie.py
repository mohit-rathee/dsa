class Solution:
    def assign_cookie(self, students,cookies):
        # print(students,cookies)
        students=sorted(students)
        cookies=sorted(cookies)

        student_count=0
        i=0
        for cookie in cookies:
            if i>=len(students):
                break
            if students[i]<=cookie:
                # assign cookie
                student_count+=1
                i+=1
            # else cookie won't be assigned
        print(student_count)
        return student_count


sol = Solution()
students = [20, 10, 40] 
cookies = [100,210,1]
sol.assign_cookie(students,cookies)
