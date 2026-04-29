class MinStack:

    def __init__(self):
        self._stack = []
        self._minstack = []
    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._minstack:
            self._minstack.append(min(val,self._minstack[-1]))
        else:
            self._minstack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._minstack.pop()

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]

    def getMin(self) -> int:
        return self._minstack[-1]
