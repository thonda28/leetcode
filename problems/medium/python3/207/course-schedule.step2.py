#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        postrequisites_of_courses = [[] for _ in range(numCourses)]
        indegree_of_courses = [0 for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            postrequisites_of_courses[prerequisite].append(course)
            indegree_of_courses[course] += 1

        non_indegree_courses = []
        for i in range(numCourses):
            if indegree_of_courses[i] == 0:
                non_indegree_courses.append(i)

        num_of_processed_courses = 0
        while non_indegree_courses:
            nic = non_indegree_courses.pop()
            for postrequisites in postrequisites_of_courses[nic]:
                indegree_of_courses[postrequisites] -= 1
                if indegree_of_courses[postrequisites] == 0:
                    non_indegree_courses.append(postrequisites)
            num_of_processed_courses += 1
        return num_of_processed_courses == numCourses
# @lc code=end
