# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstNum  = []
        secondNum = []
        
        firstNum.append(l1.val)
        while l1.next:
            l1 = l1.next
            firstNum.append(l1.val)
            
        secondNum.append(l2.val)
        while l2.next:
            l2 = l2.next
            secondNum.append(l2.val)
            
            
        outputNum = int(''.join([ str(i) for i in firstNum ])[::-1]) + int(''.join([ str(i) for i in secondNum ])[::-1])
        outputNum = str(outputNum)[::-1]
        
        result = ListNode(outputNum[0])
        resultTemp = result
        
        for number in outputNum[1::]:
            temp = ListNode(int(number))
            resultTemp.next = temp
            resultTemp = resultTemp.next
            
        return result
        
