from deli_counter import (
    line, take_a_number, now_serving
)

import io
import sys

class TestDeliCounter:
    '''Module deli_counter.py'''

    KATZ_DELI = []
    OTHER_DELI = ["Logan", "Avi", "Spencer"]
    ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

    def test_line_when_empty(self):
        '''says the line is empty'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        line(TestDeliCounter.KATZ_DELI)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The line is currently empty.\n")

    def test_line_with_people(self):
        '''displays the current line'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        line(TestDeliCounter.OTHER_DELI)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The line is currently: 1. Logan 2. Avi 3. Spencer\n")

        captured_out = io.StringIO()
        sys.stdout = captured_out
        line(TestDeliCounter.ANOTHER_DELI)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The line is currently: 1. Amanda 2. Annette 3. Ruchi 4. Jason 5. Logan 6. Spencer 7. Avi 8. Joe 9. Rachel 10. Lindsey\n")

    def test_take_a_number_when_empty(self):
        '''adds a person to an empty line'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        take_a_number(TestDeliCounter.KATZ_DELI, "Ada")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Welcome, Ada. You are number 1 in line.\n")
        assert(TestDeliCounter.KATZ_DELI == ["Ada"])
        TestDeliCounter.KATZ_DELI.clear()

    def test_take_a_number_with_people_in_line(self):
        '''adds a person to the end of the line'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        take_a_number(TestDeliCounter.OTHER_DELI, "Gracie")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Welcome, Gracie. You are number 4 in line.\n")
        assert(TestDeliCounter.OTHER_DELI == ["Logan", "Avi", "Spencer", "Gracie"])
        TestDeliCounter.OTHER_DELI.pop()

    def test_take_a_number_multiple_times(self):
        '''correctly builds the line'''
        take_a_number(TestDeliCounter.KATZ_DELI, "Ada")
        take_a_number(TestDeliCounter.KATZ_DELI, "Gracie")
        take_a_number(TestDeliCounter.KATZ_DELI, "Kent")
        assert(TestDeliCounter.KATZ_DELI == ["Ada", "Gracie", "Kent"])
        TestDeliCounter.KATZ_DELI.clear()

    def test_now_serving_with_empty_line(self):
        '''says that the line is empty'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        now_serving(TestDeliCounter.KATZ_DELI)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "There is nobody waiting to be served!\n")

    def test_now_serving_with_people_in_line(self):
        '''serves the first person in line and removes them from the queue'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        now_serving(TestDeliCounter.OTHER_DELI)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Currently serving Logan.\n")
        assert(TestDeliCounter.OTHER_DELI == ["Avi", "Spencer"])
        TestDeliCounter.OTHER_DELI.insert(0, "Logan")
        