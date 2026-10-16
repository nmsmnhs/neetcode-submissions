public class MinStack
{
    private List<int> _stack;
    private List<int> _minStack;

    public MinStack()
    {
        _stack = new List<int>();
        _minStack = new List<int>();
    }

    public void Push(int val)
    {
        if (_stack.Count == 0|| val < _minStack[_minStack.Count - 1])
        {
            _minStack.Add(val);
        }
        else
        {
            _minStack.Add(_minStack[_minStack.Count - 1]);
        }
        _stack.Add(val);
    }

    public void Pop()
    {
        if (_stack.Count == 0) return;
        _stack.RemoveAt(_stack.Count - 1);
        _minStack.RemoveAt(_minStack.Count - 1);
    }

    public int Top()
    {
        if (_stack.Count == 0)
        {
            return -1;
        }
        return _stack[_stack.Count - 1];
    }

    public int GetMin()
    {
        if (_stack.Count == 0)
        {
            return -1;
        }
        return (_minStack[_minStack.Count - 1]);
    }
}