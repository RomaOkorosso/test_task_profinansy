import time

from logger import logger

tasks_data = {}


class Tasks:
    @staticmethod
    def perform_calculation(task_id: int, x: int, y: int, operator: str):
        time.sleep(5)  # Simulate a delay for the calculation
        logger.log(f"perform_calculation - calc task_id: {task_id}, {x} {operator} {y}")

        if operator == "+":
            result = x + y
        elif operator == "-":
            result = x - y
        elif operator == "*":
            result = x * y
        elif operator == "\\":
            result = x / y
        else:
            result = None

        tasks_data[task_id] = {"status": "completed", "result": result}
