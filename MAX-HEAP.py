class MaxHeap:
    def __init__(self,capacity):
        self.storage=[]
        self.size=0
        self.capacity=capacity

    def hasParent(self,index):
        return (index-1)//2>=0

    def getParentIndex(self,index):
        return (index-1)//2

    def getParent(self,index):
        if self.hasParent(index):
            i=self.getParentIndex(index)
            return self.storage[i]

    def hasLeftChild(self,index):
        return 2*index+1<self.size

    def getLeftChildIndex(self,index):
        return 2*index+1

    def getLeftChild(self,index):
        if self.hasLeftChild(index):
            i=self.getLeftChildIndex(index)
            return self.storage[i]

    def hasRightChild(self,index):
        return 2*index+2<self.size

    def getRightChildIndex(self,index):
        return 2*index+2

    def getRightChild(self,index):
        if self.hasRightChild(index):
            i=self.getRightChildIndex(index)
            return self.storage[i]
        
    def swap(self,l,r):
        self.storage[l],self.storage[r]=self.storage[r],self.storage[l]

    def insert(self,value):
        if self.size==self.capacity:
            print("HEAP IS FULL")
            return
        else:
            self.storage.append(value)
            self.size+=1
            self.heapifyUp()

    def heapifyUp(self):
        ind=self.size-1
        while(self.hasParent(ind) and self.getParent(ind)<self.storage[ind]):
            t=self.getParentIndex(ind)
            self.swap(ind,t)
            ind=t

    def remove(self):
        if self.size==0:
            print("HEAP IS EMPTY")
            return
        else:
            self.swap(0,self.size-1)
            self.size-=1
            self.storage.pop()
            self.heapifyDown()

    def heapifyDown(self):
        i=0
        while self.hasLeftChild(i):
            t=self.getLeftChildIndex(i)
            if self.hasRightChild(i) and self.storage[t]<self.getRightChild(i):
                t=self.getRightChildIndex(i)
            if self.storage[i]>self.storage[t]:
                break
            else:
                self.swap(i,t)
            i=t
    def display(self):
         for i in self.storage:
             print(i)

a=MaxHeap(10)
a.insert(3)
a.insert(4)
a.insert(9)
a.insert(5)
a.insert(2)
a.insert(1)
a.display()
print("******************")
a.remove()
a.display()
            
            
    
        
