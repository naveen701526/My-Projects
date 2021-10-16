#include <iostream>
#include <queue>
  
using namespace std;
  
void display(queue<int> x)
{
    queue<int> que = x;
    while (!que.empty()) {
        cout << '\t' << que.front();
        que.pop();
    }
    cout << '\n';
}

int main()
{
    queue<int> test;
    test.push(10);
    test.push(20);
    test.push(30);
  
    cout << "The queue test is : ";
    display(test);
  
    cout << "\ntest.size() : " << test.size();
    cout << "\ngtest.front() : " << test.front();
    cout << "\ntest.back() : " << test.back();
  
    cout << "\ntest.pop() : ";
    test.pop();
    display(test);
  
    return 0;
}
