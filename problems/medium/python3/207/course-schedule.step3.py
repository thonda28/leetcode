#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        postrequisites_of_courses = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            postrequisites_of_courses[prerequisite].append(course)

        NOT_CHECKED, CHECKING, COMPLETED = 0, 1, 2
        def hasCycle(labels: List[int], course: int) -> bool:
            if labels[course] == CHECKING:
                return True
            if labels[course] == COMPLETED:
                return False
            labels[course] = CHECKING
            for post in postrequisites_of_courses[course]:
                if hasCycle(labels, post):
                    return True
            labels[course] = COMPLETED
            return False

        labels = [NOT_CHECKED for _ in range(numCourses)]
        for course in range(numCourses):
            if hasCycle(labels, course):
                return False
        return True
# @lc code=end
