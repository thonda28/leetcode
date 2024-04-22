#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        constraint_map, num_of_constraint_map = dict(), dict()
        for after, before in prerequisites:
            if before not in constraint_map:
                constraint_map[before] = []
            constraint_map[before].append(after)
            if after not in num_of_constraint_map:
                num_of_constraint_map[after] = 0
            num_of_constraint_map[after] += 1

        no_constraint_courses = []
        for i in range(numCourses):
            if i not in num_of_constraint_map:
                no_constraint_courses.append(i)

        taking_order = []
        while no_constraint_courses:
            course = no_constraint_courses.pop()
            taking_order.append(course)
            if course not in constraint_map:
                continue
            for constraint in constraint_map[course]:
                num_of_constraint_map[constraint] -= 1
                if num_of_constraint_map[constraint] == 0:
                    no_constraint_courses.append(constraint)
        return len(taking_order) == numCourses
# @lc code=end
