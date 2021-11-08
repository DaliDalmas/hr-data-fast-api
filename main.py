from typing import Optional
from fastapi import FastAPI

description = """I have learnt some bit of fastAPI and I wpuld like to see whether I can create
a secure api using csv files"""

tags_metadata = [
    {
        "name": "employees",
        "description": "Employee data, with information like, name, Date of Birth, Date of hire, Department",
        "externalDocs": {
            "description": "Read more about this data from Kaggle",
            "url": "https://www.kaggle.com/davidepolizzi/hr-data-set-based-on-human-resources-data-set?select=tbl_Perf.csv",
        },
    },
    {
        "name": "actions",
        "description": "Action data, indicating actions like, hiring, promotions, demotions, attrition.",
        "externalDocs": {
            "description": "Read more about this data from Kaggle",
            "url": "https://www.kaggle.com/davidepolizzi/hr-data-set-based-on-human-resources-data-set?select=tbl_Perf.csv",
        },
    },
    {
        "name": "performances",
        "description": "Performance data. For each employee for each period.",
        "externalDocs": {
            "description": "Read more about this data from Kaggle",
            "url": "https://www.kaggle.com/davidepolizzi/hr-data-set-based-on-human-resources-data-set?select=tbl_Perf.csv",
        },
    },
]


app = FastAPI(title="DaliCodes HR API",description = description,version="0.0.1", openapi_tags=tags_metadata)


@app.get("/employees", tags=["employees"])
def read_employees():
    return {"EmpID","EmpName","EngDt","TermDt","DepID","GenderID","RaceID","MgrID","DOB","PayRate","Level"}

@app.get("/employee/{employee_id}", tags=["employees"])
def read_employees(employee_id:int):
    return {"EmpID","EmpName","EngDt","TermDt","DepID","GenderID","RaceID","MgrID","DOB","PayRate","Level"}

@app.post("/employees", tags=["employees"])
def write_employees():
    return {"EmpID","EmpName","EngDt","TermDt","DepID","GenderID","RaceID","MgrID","DOB","PayRate","Level"}

@app.put("/employees", tags=["employees"])
def update_employees():
    return {"EmpID","EmpName","EngDt","TermDt","DepID","GenderID","RaceID","MgrID","DOB","PayRate","Level"}

@app.delete("/employees", tags=["employees"])
def delete_employees():
    return {"EmpID","EmpName","EngDt","TermDt","DepID","GenderID","RaceID","MgrID","DOB","PayRate","Level"}



@app.get("/actions", tags=["actions"])
def read_actions():
    return {"ActID","ActionID","EmpID","EffectiveDt"}

@app.get("/action/{employee_id}", tags=["actions"])
def read_actions(employee_id:int):
    return {"ActID","ActionID","EmpID","EffectiveDt"}

@app.post("/actions", tags=["actions"])
def write_actions():
    return {"ActID","ActionID","EmpID","EffectiveDt"}

@app.put("/actions", tags=["actions"])
def update_actions():
    return {"ActID","ActionID","EmpID","EffectiveDt"}

@app.delete("/actions", tags=["actions"])
def delete_actions():
    return {"ActID","ActionID","EmpID","EffectiveDt"}




@app.get("/performances", tags=["performances"])
def read_performances():
    return {"PerfID","EmpID","Rating","PerfDate"}

@app.get("/performance/{employee_id}", tags=["performances"])
def read_performances(employee_id:int):
    return {"PerfID","EmpID","Rating","PerfDate"}

@app.post("/performances", tags=["performances"])
def write_performances():
    return {"PerfID","EmpID","Rating","PerfDate"}

@app.put("/performances", tags=["performances"])
def update_performances():
    return {"PerfID","EmpID","Rating","PerfDate"}

@app.delete("/performances", tags=["performances"])
def delete_performances():
    return {"PerfID","EmpID","Rating","PerfDate"}