from collections import deque

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = None
        self.turnaround_time = None
        self.waiting_time = None

def print_gantt_chart(gantt, algorithm):
    print(f"\nGantt Chart ({algorithm}):")
    print(" | ".join(f"P{pid}" for pid, _ in gantt))
    print("0", end="")
    for _, t in gantt:
        print(f" {' ' * (len(str(t)))}{t}", end="")
    print("\n")

def calculate_metrics(processes):
    total_tat = total_wt = 0
    n = len(processes)
    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        total_tat += p.turnaround_time
        total_wt += p.waiting_time

    avg_tat = total_tat / n
    avg_wt = total_wt / n
    return avg_tat, avg_wt

def reset_processes(processes, original_processes):
    for i, p in enumerate(processes):
        p.arrival_time = original_processes[i].arrival_time
        p.burst_time = original_processes[i].burst_time
        p.priority = original_processes[i].priority
        p.remaining_time = original_processes[i].burst_time
        p.start_time = None
        p.completion_time = None
        p.turnaround_time = None
        p.waiting_time = None

def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    gantt = []
    current_time = 0

    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        if not gantt or gantt[-1][0] != p.pid:
            gantt.append((p.pid, current_time))
        p.start_time = current_time
        p.completion_time = current_time + p.burst_time
        current_time += p.burst_time

    avg_tat, avg_wt = calculate_metrics(processes)
    return gantt, avg_tat, avg_wt

def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    ready_queue = []
    gantt = []
    current_time = 0
    completed = 0
    n = len(processes)

    while completed < n:
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue and p.completion_time is None:
                ready_queue.append(p)
        ready_queue.sort(key=lambda x: x.burst_time)
        if ready_queue:
            p = ready_queue.pop(0)
            if not gantt or gantt[-1][0] != p.pid:
                gantt.append((p.pid, current_time))
            p.start_time = current_time
            p.completion_time = current_time + p.burst_time
            current_time += p.burst_time
            completed += 1
        else:
            current_time += 1

    avg_tat, avg_wt = calculate_metrics(processes)
    return gantt, avg_tat, avg_wt

def round_robin(processes, time_quantum):
    ready_queue = deque()
    gantt = []
    current_time = 0
    completed = 0
    n = len(processes)

    while completed < n:
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue and p.remaining_time > 0:
                ready_queue.append(p)

        if ready_queue:
            p = ready_queue.popleft()
            if not gantt or gantt[-1][0] != p.pid:
                gantt.append((p.pid, current_time))
            executed_time = min(time_quantum, p.remaining_time)
            current_time += executed_time
            p.remaining_time -= executed_time

            if p.remaining_time == 0:
                p.completion_time = current_time
                completed += 1
            else:
                ready_queue.append(p)
        else:
            current_time += 1

    avg_tat, avg_wt = calculate_metrics(processes)
    return gantt, avg_tat, avg_wt

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    gantt = []
    current_time = 0

    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        if not gantt or gantt[-1][0] != p.pid:
            gantt.append((p.pid, current_time))
        p.start_time = current_time
        p.completion_time = current_time + p.burst_time
        current_time += p.burst_time

    avg_tat, avg_wt = calculate_metrics(processes)
    return gantt, avg_tat, avg_wt

def execute_all_algorithms(processes):
    original_processes = [Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes]

    algorithms = {
        "FCFS": fcfs,
        "SJF": sjf,
        "Round Robin (Time Quantum = 2)": lambda p: round_robin(p, 2),
        "Priority Scheduling": priority_scheduling,
    }

    for algo_name, algo_func in algorithms.items():
        reset_processes(processes, original_processes)
        gantt, avg_tat, avg_wt = algo_func(processes)
        print_gantt_chart(gantt, algo_name)
        print(f"{algo_name} -> Average Turnaround Time: {avg_tat:.2f}, Average Waiting Time: {avg_wt:.2f}\n")

def main():
    processes_data = [
        [1, 0, 6, 2],  # Process ID, Arrival Time, Burst Time, Priority
        [2, 2, 7, 1],
        [3, 4, 8, 3],
        [4, 6, 3, 4]
    ]

    # Create a list of Process objects
    processes = [Process(pid, arrival_time, burst_time, priority)
                 for pid, arrival_time, burst_time, priority in processes_data]

    print("\nExecuting all algorithms...")
    execute_all_algorithms(processes)

if __name__ == "__main__":
    main()

