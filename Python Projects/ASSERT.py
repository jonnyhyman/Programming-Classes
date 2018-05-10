class Hendrick:
    def __init__(self):
        self.value = None

h0 = Hendrick()
h1 = Hendrick()

h0.value = int(1)
h1.value = float(1.0)
print(h0.value == h1.value)
print(h0.value is h1.value)
