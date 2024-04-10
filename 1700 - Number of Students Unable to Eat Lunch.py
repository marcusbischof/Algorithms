# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:
# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

# Example 1:

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.

# Example 2:

# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3

# Constraints:

# 1 <= students.length, sandwiches.length <= 100
# students.length == sandwiches.length
# sandwiches[i] is 0 or 1.
# students[i] is 0 or 1.


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Use a stack and a queue to arrange the "lunch line". Continue to process the queue until either:
        #   - 1) we cycle through the entire length of the queue without a single sandwich being eaten.
        #   - 2) we empty the stack OR the queue (no sandwiches left OR no students left in line).
        # Answer is the # of students still in the queue once we're done with lunch.

        sandwiches = deque(sandwiches) # Based on example, this is a Queue and NOT a Stack.
        students = deque(students)

        while students and sandwiches:
            numStudents = len(students)
            sandwichEaten = False

            for i in range(numStudents):
                curStudent = students.popleft()
                if curStudent == sandwiches[0]:
                    sandwiches.popleft()
                    sandwichEaten = True
                else:
                    students.append(curStudent)
            if sandwichEaten == False:
                return len(students)

        return len(students)

# Time Complexity: O(n * m) -> Worst case would have each student in q being offered each sandwich once.
# Space Complexity: O(n + m) -> Store each sandwich and each student on separate stacks.