class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        n = len(students)

        while len(students) > 0:

            if sandwiches[0] in students:
                
                if students[0] == sandwiches[0]:
                    count += 1
                    students.pop(0)
                    sandwiches.pop(0)

                else:
                    front = students.pop(0)
                    students.append(front)

            else:
                break
            
        return(n - count)