from fastapi import FastAPI, BackgroundTasks, HTTPException
from app.tasks import Tasks, tasks_data
from logger import logger

app = FastAPI()


@app.post("/calculate/{x}/{y}/{operator}")
async def calculate(x: int, y: int, operator: str, background_tasks: BackgroundTasks):
    if operator not in ["+", "-", "*", "\\"]:  # use \, because / parse as URL part
        logger.log(f"calculate - invalid operator: {operator}")
        raise HTTPException(
            status_code=400,
            detail="Invalid operator. Supported operators are +, -, *, \\",
        )
    if type(x) != int or type(y) != int:
        logger.log(f"calculate - invalid type {x if type(x) != int else y}")
        raise HTTPException(
            status_code=422,
            detail=f"Invalid type of {'x' if type(x) != int else 'y'}, supported only int",
        )

    task_id = len(tasks_data) + 1
    tasks_data[task_id] = {"status": "in_progress"}

    logger.log(f"calculate - calc {x}, {y}, with {operator}")
    logger.log(f"calculate - task now: {len(tasks_data)}")

    background_tasks.add_task(Tasks.perform_calculation, task_id, x, y, operator)

    return {"task_id": task_id}


@app.get("/result/{task_id}")
async def get_result(task_id: int):
    logger.log(f"get_result - getting task with id: {task_id}")
    task = tasks_data.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if task["status"] == "in_progress":
        return {"status": "in_progress"}

    result = task.get("result")
    if result is None:
        raise HTTPException(status_code=404, detail="Result not available yet")

    return {"status": "completed", "result": result}


@app.get("/tasks")
async def get_tasks():
    logger.log("get_tasks - get all tasks")
    return tasks_data
