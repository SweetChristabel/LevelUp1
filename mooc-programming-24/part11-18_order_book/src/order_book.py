# Write your solution here:
class Task:
    id = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._status = False #Could have just beena  boolean and the finished/not finished defined in the __str__ instead.
        self.id = Task.id
        Task.id +=1
    
    def __str__(self):
        status = "NOT FINISHED" if not self._status else "FINISHED"
        return(f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}")
    
    def is_finished(self):
        return self._status
        
    def mark_finished(self):
        self._status = True

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self.orders
    
    def programmers(self):
        programmers = [order.programmer for order in self.orders]
        return list(set(programmers))

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError
    
    def finished_orders(self):
        return [order for order in self.orders if order._status is True]
    
    def unfinished_orders(self):
        return [order for order in self.orders if order._status is False]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError
        else:
            finished_tasks = [t for t in self.orders if t.programmer == programmer and t.is_finished()]
            unfinished_tasks = [t for t in self.orders if t.programmer == programmer and not t.is_finished()]
            return len(finished_tasks), len(unfinished_tasks), sum(t.workload for t in finished_tasks), sum(t.workload for t in unfinished_tasks)



if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)


   

