import unittest
from unittest.mock import MagicMock
from src.brokers.storages import StorageBroker
from src.models.students import Student
from src.services.students import StudentService


class MyTestCase(unittest.TestCase):

    def test_something(self):
        # given
        inputStudent = Student()
        inserted_student = inputStudent
        expected_student = inserted_student
        storageBrokerMock = StorageBroker()

        studentService = \
            StudentService(storageBrokerMock)

        storageBrokerMock.insert_student = \
            MagicMock(return_value=inserted_student)

        # when
        actualStudent = studentService \
            .add_student(inputStudent)

        # then
        self.assertEqual(actualStudent, expected_student)

        storageBrokerMock.insert_student \
            .assert_called_once_with(inputStudent)


if __name__ == '__main__':
    unittest.main()
