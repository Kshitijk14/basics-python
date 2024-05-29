import math

class calc:
    def takeInputs(self, x, y):
        self.x = x
        self.y = y
    
class opes(calc):
    def add(self):
        print(f"Sum {self.x + self.y}")

    def subtract(self):
        print(f"Difference: {self.x - self.y}")

    def multiply(self):
        print(f"Product: {self.x * self.y}")

    def divide(self):
        if self.y == 0:
            raise ValueError("Cannot divide by zero.")
        print(f"Division: {self.x / self.y}")
    
    def remainder(self):
        print(f"Remainder: {self.x % self.y}")

    def square_root(self):
        return math.sqrt(self.x)
    
    def power(self):
        return math.pow(self.x, self.y)

    def sin(self):
        return math.sin(self.x)

    def cos(self):
        return math.cos(self.x)

    def tan(self):
        return math.tan(self.x)

def main():
    print("Welcome to the Scientific Calculator!")
    while True:
        try:
            expression = input("Enter an expression (or 'q' to quit): ")
            if expression.lower() == 'q':
                break

            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()