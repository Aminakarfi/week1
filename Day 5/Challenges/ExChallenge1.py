import math

class Circle:
    def __init__(self, *, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle: radius = {self.radius:.2f}, diameter = {self.diameter:.2f}, area = {self.area():.2f}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other


# Let's create some circles and test them

c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=3)

print(c1)
print(c2)

# Add two circles
new_circle = c1 + c3
print(new_circle)

# Compare circles
print("Is c1 bigger than c3?", c1 > c3)
print("Is c1 equal to c2?", c1 == c2)

# Sort and print
circles = [c1, c2, c3]
sorted_circles = sorted(circles)

print("\nSorted circles by radius:")
for c in sorted_circles:
    print(c)
