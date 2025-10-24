# Build an Employee CRUD with validations

from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, EmailStr, Field, validator
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional


app = FastAPI()

DATABASE_URL = "sqlite:///./employee.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)


class EmployeeBase(BaseModel):
    name: str = Field(..., example="Sushant Sutar")
    email: EmailStr
    age: int = Field(..., ge=21, le=60, example=30)  
    department: str
    salary: float = Field(..., gt=10000, example=20000) 

class EmpCreate(EmployeeBase):
    pass

class EmpUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=21, le=60)
    department: Optional[str] = None
    salary: Optional[float] = Field(None, gt=10000)

class EmpResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employees", response_model=List[EmpResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@app.get("/employees/{id}", response_model=EmpResponse)
def get_employee(id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@app.post("/employees", response_model=EmpResponse, status_code=201)
def create_employee(emp: EmpCreate, db: Session = Depends(get_db)):
    existing_email = db.query(Employee).filter(Employee.email == emp.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_emp = Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

@app.put("/employees", response_model=EmpResponse)
def update_employee(id: int, emp_update: EmpUpdate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in emp_update.dict(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp

@app.delete("/employees/{id}", status_code=204)
def delete_employee(id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
    return {"detail": "Employee deleted successfully"}

@app.get("/employees", response_model=List[EmpResponse])
def get_all_employees(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Number of records per page"),
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    employees = db.query(Employee).offset(skip).limit(limit).all()
    return employees




