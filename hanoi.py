# Simple illustration of tower of hanoi problem using recursive functions in python - min steps 2**n - 1

def hanoi(height, left="left", right="right", middle="middle"):
    if height>=1:
        hanoi(height-1, left, middle, right)
        print(left + "->" + right)
        hanoi(height-1, middle, right, left)

hanoi(5)
