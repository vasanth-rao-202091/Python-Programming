#Job sequencing with deadlines
def job_sequence(tuple_1,max_deadline):
    arr = sorted(tuple_1, key = lambda x:x[2], reverse = True)
    print(arr)
    j_exe = []
    max_profit = 0

    for a in range(len(arr) - 1):
        if arr[a][2] == arr[a+1][2]:
            max_item = arr[a]
            break
    for  i in range(max_deadline):
        max_item = (max_item[0],0,0)
        for item in arr:
            if item[2] == i+1:
                if item[1] > max_item[1]:
                    max_item = item
        j_exe.append(max_item)
    return[i[0] for i in j_exe]

print("Enter name of the jobs: ")
jobs = [str(i) for i in input().split()]
print("Enter Deadlines: ")
deadlines = [int(i) for i in input().split()]
print("Now enter the profits: ")
profits = [int(i) for i in input().split()]

tuple_1 = [(jobs[i],profits[i],deadlines[i]) for i in range(0, len(jobs))]
print(job_sequence(tuple_1,max(deadlines)))
