class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def Length(self,node):
        if node is None:
            return 0
        return 1+self.Length(node.next)

    def printL(self):
            temp=self.head
            print("\nThe elements present in the list are")
            while temp:
                print(temp.data,end=" ")
                temp=temp.next

        

    def insertAtBeginning(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            print("\nList is empty and new node becomes the first node")
            return

        else:
            newNode.next=self.head
            self.head=newNode
            print("\nNew node is inserted at the beginning")
            return

    def insertAtEnd(self,data):
        newNode=Node(data)
        
        if self.head == None:
            self.head=newNode
            self.tail=newNode
            print("\nNo list is present and new node becomes the first node")
            return

        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next

            temp.next=newNode
            self.tail=newNode

    def insertAtMiddle(self,pos,data):
        newNode=Node(data)

        if self.head==None:
            print("\nList is currently empty and thus node will be inserted at the beginning")
            self.insertAtBeginning(data)
        elif pos==1:
            print("\nSince the position of the element is one,the element needs to be inserted at the beginning")
            self.insertAtBeginning(data)
        else:
            le=self.Length(self.head)
            if pos==le:
                self.insertAtEnd(data)
            elif pos>le:
                print("\nThe value of the position exceeds the length of the linked list")
            else:
                coun=1
                temp=self.head
                while temp:
                    if coun==pos-1:
                        newNode.next=temp.next
                        temp.next=newNode
                        print("\n New Node is inserted at the position",pos)
                        return
                    else:
                        coun+=1
                        temp=temp.next


    def deleteAtBeginning(self):
         if self.head==None:
             print("\nList is empty")
         elif self.head.next==None:
             self.head=None
             self.tail=None
             print("\nNode is deleted and the list is empty")
         else:
             self.head=self.head.next
             print("\nElement is deleted at the beginning")
             return

    def deleteAtEnd(self):
        if self.head==None:
            print("\nList is empty")
        elif self.head.next==None:
            self.head=None
            self.tail=None
            print("\nNode is deleted and the list is empty")

        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            print("\nElement is deleted at the end")


    def deleteAtMiddle(self,pos):
        if self.head==None:
            print("\nList is empty")

        elif pos==1:
            self.deleteAtBeginning()

        else:
            l=self.Length(self.head)

            if pos==l:
                self.deleteAtEnd()
            elif pos>l:
                print("Position is greater than the length of the list")
                return
            else:
                temp=self.head
                coun=1
                while temp:
                    if coun==pos-1:
                        temp.next=temp.next.next
                        print("\nNode is deleted at the position",pos)
                        return
                    else:
                        coun+=1
                        temp=temp.next
                    
                    
        
              

        
                        
      






L=SLL()

L.insertAtEnd(5)
L.insertAtEnd(6)
L.insertAtEnd(4)
L.insertAtEnd(80)
L.insertAtBeginning(66)
L.insertAtBeginning(11)
L.insertAtBeginning(32)
L.printL()
L.insertAtMiddle(3,1111)
L.printL()
L.insertAtMiddle(4,2222)
L.printL()
L.insertAtMiddle(1,55555)
L.printL()
L.insertAtMiddle(15,99999)
L.printL()
L.Length(L.head)
L.deleteAtBeginning()
L.printL()
L.deleteAtEnd()
L.printL()
L.deleteAtMiddle(3)
L.printL()
L.deleteAtMiddle(2)
L.printL()
L.deleteAtMiddle(6)
L.printL()
                
                
                        



                
                
            
            
