# Develop a class ‘complex number’ that takes real and imaginary part from user separately and print the
# complex number in proper format i.e. 3+4j
class complex_number:

    RealNo=input('enter real part:')
    imaginaryNo=input("enter imaginary part:")

    def print_complex_no(self):
        return f"{self.RealNo}+{self.imaginaryNo}j"

CompNo=complex_number()
print(CompNo.print_complex_no())
