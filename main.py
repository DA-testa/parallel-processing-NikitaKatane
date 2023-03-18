# python3

def parallel_processing(n, m, data):
    output = []
    next_free_time = [0] *n 
    threads = list(range(n))
    for job_index , job_time in enumerate (data):
        next_thread = min(threads, key=lambda i:next_free_time[i])
        output.append((next_thread,next_free_time[next_thread]))
        next_free_time[next_thread] +=job_time

    return output

def main():
    n, m =map(int,input().split())
    data=list(map(int,input().split()))
    result = parallel_processing(n ,m ,data)
    for thread, start_time in result:
        print(thread, start_time)



if __name__ == "__main__":
    main()
