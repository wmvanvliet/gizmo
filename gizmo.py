class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print (self.name)

    def hello(self, name, country = "finland"):
        print("Hello ", name, " How's life in ", country, "?")

    def spell(self, woord):
        teller = 1
        for i in woord:
            print(i, end='')
            if teller < len(woord):
                print(".", end='')
            teller += 1
        print()

    def relative_path(self, identifiers):
        i = 0
        for identifier in identifiers:
            identifiers[i] = "./subjects/mock_recording_" + identifier + ".rec"
            i += 1
        return identifiers

    def generate_fibonacci_sequence(self, nums):
        """ Short summary:

            This function generates a fibonacci sequence until the given maximum (nums)
        """

        """ Extended summary:

            This function generates a fibonacci sequence. It will take one parameter to define
            the number of iterations to peform.

            Parameters
            ----------
            nums : type int
                   Defines the number of ietration to perform

            Yields
            ------
            x    : type int
                   The value is the next number in the fibonacci sequence.

        """

        x, y = 0, 1
        for _ in range(nums):
            yield x
            x, y = y, x+y
