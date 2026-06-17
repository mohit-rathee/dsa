def greedy_student_count(pages, limit):
    student_count = 1
    current_load = 0
    for page in pages:
        if current_load + page <= limit:
            current_load += page
        else:
            student_count += 1
            current_load = page
    return student_count


def allocate_min_no_of_pages(pages, students):
    print(pages, students)
    low = max(pages)
    high = sum(pages)
    while low < high:
        mid = (low + high) // 2
        # greedy check on mid pages
        req_students = greedy_student_count(pages, mid)
        if req_students <= students:
            # if less students can fit in such configuration, then more students can just be accomodated by spliting books easily
            # valid , check left side
            high = mid
        else:
            # invalid, check righ side
            low = mid + 1
    return low


pages = [12, 34, 67, 90]
students = 2
pages = [25, 46, 28, 49, 24]
students = 4
ans = allocate_min_no_of_pages(pages, students)
print(ans)
