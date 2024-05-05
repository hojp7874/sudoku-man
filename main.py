from typing import List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from services.sudoku_service import generate_sudoku_problem, solve_sudoku

app = FastAPI()
app.mount("/static", StaticFiles(directory="templates"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/index.html") as file:
        return HTMLResponse(content=file.read(), status_code=200)


@app.get("/api/problem")
async def generate_problem():
    return generate_sudoku_problem()


@app.post("/api/solve")
async def solve_problem(board: List[List[int]]):
    return solve_sudoku(board)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)