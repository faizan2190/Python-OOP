# Develop a ‘bank’ class and implement a method ‘application_for_loan’ such that it gives two possible
# outputs based on the value of variable ‘loan_take_previously’ within the class. The two possible
# outputs are

# a. Loan granted (if loan_taken_previously=false)
# b. Loan is not granted(if loan_taken_previously=false)

# Also makes two objects of afore mentioned class and modify the value of ‘loan_taken_previously’
# with the help of object.
class bank:
    loan_taken_previously=False
    def application_for_loan(self):
        if self.loan_taken_previously:
            return "loan is granted"
        else:
            return "loan is not granted"

obj1=bank()
obj2=bank()

obj1.loan_taken_previously=True
obj2.loan_taken_previously=False

ans_1=obj1.application_for_loan()
ans_2=obj2.application_for_loan()

print(ans_1)
print(ans_2)




