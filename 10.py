import heapq

class MaxHeapScheduler:
    def __init__(self):
        self.heap = []

    def insert_job(self, priority, job_name):
        heapq.heappush(self.heap, (-priority, job_name))
        print(f"Job '{job_name}' with priority {priority} inserted.")

    def extract_max(self):
        if not self.heap:
            print("No jobs to process.")
            return None
        priority, job_name = heapq.heappop(self.heap)
        print(f"Processing job '{job_name}' with priority {-priority}.")
        return (-priority, job_name)

    def peek_max(self):
        if not self.heap:
            print("No jobs in the queue.")
            return None
        priority, job_name = self.heap[0]
        print(f"Next job to process: '{job_name}' with priority {-priority}.")
        return (-priority, job_name)

    def display_jobs(self):
        if not self.heap:
            print("No jobs in the queue.")
            return
        print("Jobs in heap order (not sorted):")
        for priority, job_name in self.heap:
            print(f"Job: '{job_name}', Priority: {-priority}")

def main():
    scheduler = MaxHeapScheduler()
    while True:
        print("\nJob Scheduler Menu:")
        print("1. Insert Job")
        print("2. Process (Extract) Highest Priority Job")
        print("3. Peek at Highest Priority Job")
        print("4. Display All Jobs")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            job_name = input("Enter job name: ")
            try:
                priority = int(input("Enter job priority (higher number = higher priority): "))
                scheduler.insert_job(priority, job_name)
            except ValueError:
                print("Invalid priority. Must be an integer.")
        elif choice == '2':
            scheduler.extract_max()
        elif choice == '3':
            scheduler.peek_max()
        elif choice == '4':
            scheduler.display_jobs()
        elif choice == '5':
            print("Exiting scheduler.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
