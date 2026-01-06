import numpy as np

class Trapazoid:
    def __init__(self, b0, b1, t0, t1, height):
        # This function defines a trapazoid by four points and a height
        #   t0 /-------\ t1     .
        #     /        \       .
        # b0 /         \ b1   . height

        # TODO: This is not a PDF

        self.b0 = b0
        self.b1 = b1
        self.t0 = t0
        self.t1 = t1
        self.height = height

    def fuzzify(self, value):
        result = 0
        if value not in range(self.b0, self.b1):
            return result
        
        elif (self.t0 <= value <= self.t1):
            return self.height
        
        elif (value < self.t0):
            return self.height/(self.t0 - self.b0) * value
        
        elif (value > self.t1):
            return self.height - self.height/(self.b1-self.t1) * (value-self.t1)
        return

def main():
    fuzzifier = Trapazoid(0, 10, 4, 8, 7)
    print(fuzzifier.fuzzify(0))
    print(fuzzifier.fuzzify(1))
    print(fuzzifier.fuzzify(3))
    print(fuzzifier.fuzzify(5))
    print(fuzzifier.fuzzify(9))
    print(fuzzifier.fuzzify(10))


if __name__ == "__main__":
    main()
