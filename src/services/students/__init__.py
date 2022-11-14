from src.brokers.storages import StorageBroker
from src.models.students import Student


class StudentService:

    def __init__(self, storage_broker: StorageBroker) -> None:
        self.storage_broker = storage_broker

    def add_student(self, student: Student) -> Student:
        return self.storage_broker.insert_student(student)
