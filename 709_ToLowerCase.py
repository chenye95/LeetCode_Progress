def toLowerCase(str: str) -> str:
    steps = ord('a') - ord('A')
    return ''.join([c if c >= 'a' and c <='z' else chr(ord(c) + steps) if c >= 'A' and c <= 'Z' else c for c in str])

assert toLowerCase("here") == "here"
assert toLowerCase("Hello") == "hello"
assert toLowerCase("LOVELY") == "lovely"
