class Solution:
    def StudentSandwich(self,students:list,sandwich:list)->list:
        StudentCount=len(students)
        counter=0
        while students and counter<StudentCount:
            if not students:
                return None
            if not sandwich:
                return students
            self.left=students[0]
            self.right=students[-1]

            if self.left==sandwich[0]:
                students=students[1:]
                sandwich=sandwich[1:]
                counter=0
            else:
                students=students[1:]
                students.append(self.left)
            counter=counter+1
            print('counter:',counter,'students',students,'sandwich:',sandwich)
        return len(students)
    

ss1=Solution()
print(ss1.StudentSandwich([1,1,1,1],[0,1,1,1]))


            
            



