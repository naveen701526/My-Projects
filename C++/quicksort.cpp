#include <iostream>

using namespace std;

void Swap(int* arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void quickSort(int* arr, int left, int right) {
    if(left>=right) return;
    int pos = left;
    int i = left+1;
    while(i<=right) {
        if(arr[i]<arr[left]) {
            pos++;
            Swap(arr, pos, i);
        }
        i++;
    }
    Swap(arr, pos, left);
    quickSort(arr, left, pos-1);
    quickSort(arr, pos+1, right);
}
int main() {
    int n;
    cout << "----Quick sort algorithm----" << endl;
    cout << "Enter number of elements: ";
    cin >> n;
    int* arr = new int[n];
    cout << "Enter elements:" << endl;
    for(int i = 0; i<n; i++) {
      cin >> arr[i];
    }
    quickSort(arr, 0, n-1);
    cout << "Sorted array: ";
    for(int i = 0; i<n; i++)
      cout << arr[i] << " ";
    delete[] arr;
}
