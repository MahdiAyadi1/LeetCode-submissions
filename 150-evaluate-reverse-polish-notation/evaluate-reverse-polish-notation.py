class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens :
            if i =='+': 
                one = stack.pop()
                two = stack.pop()
                stack.append(one +two )
            elif i =='*': 
                one = stack.pop()
                two = stack.pop()
                stack.append(one * two )
            elif i =='-': 
                one = stack.pop()
                two = stack.pop()
                stack.append(two - one )
            elif i =='/': 
                one = stack.pop()
                two = stack.pop()
                stack.append(int(two / float(one)))
            else :
                stack.append(int(i))
        return stack.pop()

        