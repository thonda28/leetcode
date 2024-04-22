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

        for course, prerequisite in prerequisites:
            postrequisites_of_courses[prerequisite].append(course)
            num_prerequisites_of_courses[course] += 1

        independent_courses = []
        for i in range(numCourses):
            if num_prerequisites_of_courses[i] == 0:
                independent_courses.append(i)

        num_of_processed_courses = 0
        while independent_courses:
            ic = independent_courses.pop()
            for postrequisites in postrequisites_of_courses[ic]:
                num_prerequisites_of_courses[postrequisites] -= 1
                if num_prerequisites_of_courses[postrequisites] == 0:
                    independent_courses.append(postrequisites)
            num_of_processed_courses += 1
        return num_of_processed_courses == numCourses
# @lc code=end
