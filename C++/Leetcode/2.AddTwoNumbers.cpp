
//   Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *sum, *sumcur; /*sum is used to store the head of our answer list containing the sum. sumcur is used to traverse our answer list*/
        ListNode *cur1 = l1, *cur2 = l2;
        int carry = 0;
        bool b = false; //carry to store the carry from previous sum. The boolean 'b' is used for setting the head of our answer list during the first iteration
        while (cur1 != nullptr && cur2 != nullptr)
        {
            if (b)
            {
                int tmpSum = (cur1->val + cur2->val + carry) % 10; //finding the sum along with the carry and only the unit's digit being taken
                carry = (cur1->val + cur2->val + carry) / 10;      //finding the carry
                ListNode *newNode = new ListNode(tmpSum);          //creation of a new node
                newNode->next = nullptr;
                sumcur->next = newNode; //Sumcur was set in the first iteration as head so its next will point to the next node being created
                sumcur = sumcur->next;  //move the pointer to the next node of our answer list so the next number can be added
            }
            else
            {
                int tmpSum = (cur1->val + cur2->val) % 10;
                carry = (cur1->val + cur2->val) / 10;
                ListNode *newNode = new ListNode(tmpSum); //creation of a new node
                newNode->next = nullptr;                  //new node always points to null
                sum = newNode;
                sumcur = sum;
                b = true; //changing the calue of 'b' since we have set the head node of our answer list
            }
            cur1 = cur1->next;
            cur2 = cur2->next;
        }
        /*It might so happen that both the list are of different size and one of them ended. We check for pointer being 'null'. The one whose pointer is not null, we traverse it until the end is reached and  keep finding the sum. The sum is found in the exact same way except that only the current value of the list being traversed and carry is addded */
        if (cur1 != nullptr)
        {
            while (cur1 != nullptr)
            {
                int tmpSum = (cur1->val + carry) % 10;
                carry = (cur1->val + carry) / 10;
                ListNode *newNode = new ListNode(tmpSum);
                newNode->next = nullptr;
                sumcur->next = newNode;
                sumcur = sumcur->next;
                cur1 = cur1->next;
            }
        }
        else if (cur2 != nullptr)
        {
            while (cur2 != nullptr)
            {
                int tmpSum = (cur2->val + carry) % 10;
                carry = (cur2->val + carry) / 10;
                ListNode *newNode = new ListNode(tmpSum);
                newNode->next = nullptr;
                sumcur->next = newNode;
                sumcur = sumcur->next;
                cur2 = cur2->next;
            }
        }
        if (carry != 0) //If any remaining carry is left its added in the end
        {
            ListNode *newNode = new ListNode(carry);
            newNode->next = nullptr;
            sumcur->next = newNode;
            sumcur = sumcur->next;
        }
        return sum; //The head node of our answe list which we saved during the first iteration is returned
    }
};
