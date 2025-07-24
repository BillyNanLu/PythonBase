__all__ = ['test_a']

def test_a(a, b):
    return a + b

def test_b(a, b):
    return a - b

if __name__ == '__main__':
    print(test_a(1, 2))
    print(test_b(1, 2))