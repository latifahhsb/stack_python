class Stack:
    def __init__(self):
        self._data = []

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._data)
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data top.')
        return self._data[-1]

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data yang dapat di-pop.')  
        return self._data.pop()  

    def push(self, data):
        self._data.append(data)

    def printData(self): 
        for item in self._data:
            print(item)

    def deleteAll(self):
        self._data.clear()


myStack = Stack()
myStack.push(10) 
myStack.push(21) 
myStack.push(23)  

print(f'Total Data = {len(myStack)}')
print(f'Elemen TOP = {myStack.peek()}')

print()
print('Data dalam Stack:')
myStack.printData()

print()
print('Hapus Data')
myStack.pop()
print('Data dalam Stack:')
myStack.printData()

print()
print('Hapus Seluruh Data')
myStack.deleteAll()
if myStack.isEmpty():
    print('Stack kosong')
else:
    print('Data dalam Stack:')
    myStack.printData()
