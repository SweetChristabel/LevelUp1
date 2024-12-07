# Write your solution here
class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def instructions(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        desc = input("description: ")
        progrload = input("programmer and workload estimate: ").split()
        self.__orderbook.add_order(desc, progrload[0], int(progrload[1]))
        print("added!")

    def fetch_orders(self, command: int):
        if command == 2:
            hit = self.__orderbook.finished_orders()
            if hit == []:
                print("no finished tasks")
            else:
                for t in hit:
                    print(t)
        
        if command == 3:
            hit = self.__orderbook.unfinished_orders()
            if hit == []:
                print("no unfinished tasks")
            else:
                for t in hit:
                    print(t)

        
    def finish_order(self):
        order = int(input("id: "))
        self.__orderbook.mark_finished(order)
        print("marked as finished")

    def fetch_programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)
    
    def fetch_programmerstatus(self):
        programmer = input("programmer: ")
        fin, notfin, finhrs, notfinhrs = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {fin} not finished {notfin}, hours: done {finhrs} scheduled {notfinhrs}")
 
    def execute(self):
        self.instructions()
        while True:
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                try:
                    self.add_order()
                except:
                    print("erroneous input")
                    continue
            elif command == 2 or command == 3:
                try:
                    self.fetch_orders(command)
                except:
                    print("erroneous input")
                    continue
            elif command == 4:
                try:
                    self.finish_order()
                except:
                    print("erroneous input")
                    continue
            elif command == 5:
                try:
                    self.fetch_programmers()
                except:
                    print("erroneous input")
                    continue
            elif command == 6:
                try:
                    self.fetch_programmerstatus()
                except:
                    print("erroneous input")
                    continue



    
    
        


# If you use the classes made in the previous exercise, copy them here
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


OB = OrderBookApplication()
OB.execute()