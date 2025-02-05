import heapq

class TaskScheduler:
    def __init__(self):
        # Priority queue (min-heap)
        self.task_queue = []

    def add_task(self, priority, task_name):
        """
        Add a task to the priority queue.
        Priority: Lower values indicate higher priority.
        """
        heapq.heappush(self.task_queue, (priority, task_name))
        print(f"Task '{task_name}' added with priority {priority}")

    def execute_task(self):
        """
        Execute the highest-priority task.
        """
        if self.task_queue:
            priority, task_name = heapq.heappop(self.task_queue)
            print(f"Executing task '{task_name}' with priority {priority}")
        else:
            print("No tasks to execute.")

    def peek_next_task(self):
        """
        Peek at the highest-priority task without removing it.
        """
        if self.task_queue:
            priority, task_name = self.task_queue[0]
            print(f"Next task to execute: '{task_name}' with priority {priority}")
        else:
            print("No tasks in the queue.")

# Example Usage
if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Add tasks
    scheduler.add_task(3, "Write report")
    scheduler.add_task(1, "Fix critical bug")
    scheduler.add_task(2, "Attend team meeting")

    # Peek at the next task
    scheduler.peek_next_task()

    # Execute tasks in order of priority
    scheduler.execute_task()
    scheduler.execute_task()
    scheduler.execute_task()

    # Try to execute with no tasks
    scheduler.execute_task()
