class task:
       def __init__(self):
              self.list_of_task=[]

       def add_task(self):
              self.list_of_task.append(input("enter task: "))

       def delete_task(self):
              n=int(input("enter task number which you want to deleted: "))
              if 0<n-1<len(self.list_of_task):
                     self.list_of_task.remove(self.list_of_task[n-1])
                     print("task deleted")
              else:
                     print("no task available ")

       def mark_task(self):
              n=int(input("enter task number: "))
              if 0<n-1<len(self.list_of_task):
                     self.list_of_task[n-1]="Completed"
              else:
                     print("no task available")

class main:
       obj = task()
       while(True):
           print("optionns")
           print("1. add task: ")
           print("2. delete task: ")
           print("3. mark task as completed: ")
           print("4. exit: ")
           num=int(input("enter number"))
           if num==1:
              obj.add_task()
           elif num==2:
                  obj.delete_task()
           elif num==3:
                  obj.mark_task()
           elif num==4:
                  break
           else:
                  print("invalid input please try again: ")

if __name__=="__main__":
       main()