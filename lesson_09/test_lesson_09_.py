import pytest
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import text
from datetime import datetime

DATABASE_URL = "postgresql://postgres@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, default=0)

@pytest.fixture
def db():
    session = SessionLocal()
    yield session
    session.close()

# 1. Добавление
def test_add_student(db):

    student = Student(name="Тест студент", age=1)
    db.add(student)
    db.commit()
    db.refresh(student)

    assert student.id is not None

    db.delete(student)
    db.commit()

#  2. Изменение
def test_update_student(db):
    student = Student(name="Тест студент", age=1)
    db.add(student)
    db.commit()
    db.refresh(student)

    student.name = "Тест студент2"
    db.commit()
    db.refresh(student)

    assert student.name == "Тест студент2"

    db.delete(student)
    db.commit()

# 3. Удаление
def test_delete_student(db):
    student = Student(name="Тест студент2", age=1)
    db.add(student)
    db.commit()
    db.refresh(student)

    student_id = student.id

    db.delete(student)
    db.commit()

    deleted = db.query(Student).filter_by(id=student_id).first()
    assert deleted is None