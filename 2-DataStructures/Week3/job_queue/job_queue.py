# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def SiftDown(self, i):
        size = self.num_workers
        minIndex = i
        l = 2*i + 1
        if l < size and (self.next_free_time[l] < self.next_free_time[minIndex] or (self.next_free_time[l] == self.next_free_time[minIndex] and self.order[l] < self.order[minIndex])):
            minIndex = l
        r = 2*i + 2
        if r < size and (self.next_free_time[r] < self.next_free_time[minIndex] or (self.next_free_time[r] == self.next_free_time[minIndex] and self.order[r] < self.order[minIndex])):
            minIndex = r
        if i != minIndex:
            self.order[i], self.order[minIndex] = self.order[minIndex], self.order[i]
            self.next_free_time[i], self.next_free_time[minIndex] = self.next_free_time[minIndex], self.next_free_time[i]
            self.SiftDown(minIndex)

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = []
        self.start_times = []
        self.next_free_time = [0] * self.num_workers
        self.order = [int(i) for i in range(self.num_workers)]
        for j in self.jobs:
            self.assigned_workers.append(self.order[0])
            self.start_times.append( self.next_free_time[0])
            self.next_free_time[0] += j
            self.SiftDown(0)

        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

