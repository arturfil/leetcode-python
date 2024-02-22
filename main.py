from Graphs.course_schedule import CourseSchedule
from Matrix.rotate_image import RotateImage
from Strings.group_anagrams import GroupAnagrams
from SystemsDesign.rate_limiter import APIRateLimiter
from flags import return_flags
from random_problem import choose_random

args = return_flags()

def main():
# choose_random(args.exclude, args.category)
    rate_limiter = APIRateLimiter()
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())
    print(rate_limiter.allow_request())

if __name__ == "__main__":
    main()
