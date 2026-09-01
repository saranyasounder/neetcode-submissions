class DynamicArray {
    private:
    int* arr;
    int length;
    int capacity;

public:

    DynamicArray(int capacity) : length(0), capacity(capacity) {
      
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (length == capacity) {
        resize();
    }
        arr[length] = n;
        length ++;
    }

    int popback() {
        length --;
        return arr[length];
    }

    void resize() {
        capacity *= 2;
        int *newArray = new int[capacity];
        for (int i = 0; i < length; i++){
            newArray[i] = arr[i];
        }
        delete[] arr;
        arr = newArray;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
