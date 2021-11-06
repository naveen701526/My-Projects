#include <iostream>

using namespace std;

void Swap(int* arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void bubbleSort(int *arr, int n) {
    bool changed = false;
    do {
        changed=false;
        for(int i=0;i<n-1;i++) {
            if(arr[i]>arr[i+1]) {
                changed=true;
                Swap(arr, i, i+1);
            }
        }
    } while(changed==true);&8

}
int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    int* arr = new int[n];
    cout << "Enter elements:" << endl;
    for(int i = 0; i<n; i++) {
      cin >> arr[i];
    }
    bubbleSort(arr, n);
    cout << "Sorted array: ";
    for(int i = 0; i<n; i++)
      cout << arr[i] << " ";
    delete[] arr;
}
