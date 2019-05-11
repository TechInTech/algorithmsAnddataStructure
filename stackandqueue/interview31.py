"""栈的压入、弹出序列
"""

class Solution_31(object):
    def ispoporder(self, push_stack, pop_stack):
        if len(push_stack) = 0 or len(pop_stack) = 0:
            return False

        stack = []

        while len(pop_stack) > 0:
            if push_stack and push_stack[0] = pop_stack[0]:
                push_stack.pop(0)
                pop_stack.pop(0)
            elif stack and stack[-1] == pop_stack[0]:
                stack.pop()
                pop_stack.pop(0)
            elif push_stack:
                stack.append(push_stack.pop(0))
            else:
                return False
        return True
