from fastapi import FastAPI,HTTPException
from database import Base,engine,SessionLocal
from services.ingestion import ingest
from models.customer import Customer

app=FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/api/ingest")
def run_ingestion():
    count=ingest()
    return {
        "status":"success",
        "records_processed":count
    }

@app.get("/api/customers")
def get_customers(page:int=1,limit:int=10):
    db=SessionLocal()
    start=(page-1)*limit
    data=db.query(Customer).offset(start).limit(limit).all()
    return data

@app.get("/api/customers/{customer_id}")
def get_customer(customer_id:str):
    db=SessionLocal()
    customer=db.query(Customer).filter(
        Customer.customer_id==customer_id
    ).first()
    if not customer:
        raise HTTPException(404)

    return customer