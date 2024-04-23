#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        postrequisites_of_courses = [[] for _ in range(numCourses)]
        num_prerequisites_of_courses = [0 for _ in range(numCourses)]

        for course, pre in prerequisites:
            postrequisites_of_courses[pre].append(course)
            num_prerequisites_of_courses[course] += 1

        visited = set()
        for i in range(numCourses):
            if num_prerequisites_of_courses[i] == 0:
                self.reducePrereqisite(postrequisites_of_courses, num_prerequisites_of_courses, visited, i)
        return not any(num_prerequisites_of_courses)

    def reducePrereqisite(self, postrequisites_of_courses: List[List[int]], num_prerequisites_of_courses: List[int], visited: Set[int], course: int):
        if course in visited:
            return
        visited.add(course)
        for post in postrequisites_of_courses[course]:
            num_prerequisites_of_courses[post] -= 1
            if num_prerequisites_of_courses[post] == 0:
                self.reducePrereqisite(postrequisites_of_courses, num_prerequisites_of_courses, visited, post)

# @lc code=end
