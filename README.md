
# How to use?



## Usage/Examples

```python
from expansion import Expansion

t1 = time.monotonic()

eq = Expansion(" ( 2t + ( ( (2x-4)^2 - ( -3x + z )^2 )^2 - 3b )^4 + 6y )^2 ")

t2 = time.monotonic()

result : list = eq.result


print("\n*************Result**************")
print(result)

print("*********************************")
print(f"Sentences Number: {len(result)}")

print("*********************************")
print("Execution Time:")
print("        Minutes: "+str(((t2-t1)/60)))
print("        Seconds: "+str((t2-t1)))

```
