from Graphs.course_schedule import CourseSchedule
from flags import return_flags

args = return_flags()

def main():
    cs = CourseSchedule()
    # res = cs.canFinish(5, [[1,0], [3, 2], [2, 4], [1, 3]])
    res = cs.canFinish(2, [[1,0], [0, 1]])
    print(res)

if __name__ == "__main__":
    main()
