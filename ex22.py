class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

		Employee.num_of_emps += 1  

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)


	def __add__(self, other):
		return self.pay + other.pay


	def __len__(self):
		return len(self.fullname())

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
	    first, last, pay = emp_str.split('-')
	    return cls(first, last, pay)


	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True    




	
emp_1 = Employee('Esther', 'Awuku', 50000)
emp_2 = Employee('juliet', 'Awuku', 70000)

print(len(emp_1))

print('juliet'.__len__())



print(emp_1 + emp_2)

print(emp_1)

print(repr(emp_1))
print(str(emp_1))


print(emp_1.__repr__())
print(emp_1.__str__())




class Developer(Employee):
	raise_amt =1.10

	def __init__(self, first, last, pay, prog_lang):
		Employee.__init__(self,first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employee=None):
		Employee.__init__(self,first, last, pay)
		if employee is None:
			self.employees =[]
		else:
			self.employees = employee

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())



	


dev_1 = Developer('Daniel', 'Anim', 1800, 'python')
dev_2 = Developer('kingsley', 'Bremen', 2000, 'java')






mgr_1 =Manager('sue','smith', 98000, [dev_1])




print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

