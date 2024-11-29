//A dynamic array is a data structure that automatically resizes itself when the allocated space is insufficient to hold new elements.


class MyDynamicArray{
    private:
       int* arr;
       int capacity;
       int size;

    void resize(){
        capacity *= 2; // Double the capacity
        int* newArr = new int[capacity]; // Create a new array with the new capacity

        // Copy existing elements to the new array
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        delete[] arr; // Free the old array
        arr = newArr; // Update the pointer to the new array
    }
       
    public:
    
        MyDynamicArray(int cap){
            capacity=cap;
            arr=new int[capacity];
            size=0;
        }
        
        void add(int elm){
            if (size==capacity){
                resize();
            }
            arr[size++]=elm;
            
        }
        
        int get(int index){
            return arr[index];
        }
        
        int getSize(){
            return size;
        }
        int getCapacity(){
            return capacity;
        }
        
};

int main() {
    // Write C++ code here
    MyDynamicArray obj(4);
    
    for(int i=0;i<=20;i++){
    obj.add(i);
    cout<<"current size"<<obj.getSize()<<"  total capacity: "<<obj.getCapacity()<<endl;
    }
    
     for(int i=0;i<=20;i++){
    cout<<obj.get(i)<<endl;
    }
        

    return 0;
}
