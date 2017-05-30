import unittest

from invoice_calculator import divide_pay

class InvoiceCalculatorTests(unittest.TestCase):
	
	def test_fair_pay(self):
		staff_hours = {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0}
		staff_pay = divide_pay(360.0, staff_hours)
		expected_pay = {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0}
		for person in staff_pay.keys():
			self.assertEqual(staff_pay[person], expected_pay[person])
	
	def test_zero_hours_person(self):
		staff_hours = {"Alice": 3.0, "Bob": 6.0, "Carol": 0.0}
		staff_pay = divide_pay(360.0, staff_hours)
		expected_pay = {"Alice": 120.0, "Bob": 240.0, "Carol": 0.0}
		for person in staff_pay.keys():
			self.assertEqual(staff_pay[person], expected_pay[person])
	
	def test_zero_hours_total(self):
		staff_hours = {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0}
		with self.assertRaises(ValueError):
			staff_pay = divide_pay(360.0, staff_hours)
	
	def test_no_people(self):
		with self.assertRaises(ValueError):
			pay = divide_pay(360.0, {})
	
	def test_high_hours(self):
		staff_hours = {"Alice": 600.0, "Bob": 300.0, "Carol": 300.0}
		staff_pay = divide_pay(360.0, staff_hours)
		expected_pay = {"Alice": 180.0, "Bob": 90.0, "Carol": 90.0}
		for person in staff_pay.keys():
			self.assertEqual(staff_pay[person], expected_pay[person])
	
if __name__ == "__main__":
	unittest.main()
