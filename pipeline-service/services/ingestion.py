import requests

from database import SessionLocal
from models.customer import Customer

FLASK_URL="http://mock-server:5000/api/customers"

def ingest():
    db = SessionLocal()
    page=1
    limit=10
    total_records=0
    while True:
        response = requests.get(
            FLASK_URL,
            params={"page":page,"limit":limit}
        )
        data=response.json()
        customers=data["data"]
        if not customers:
            break
        for c in customers:
            existing=db.query(Customer).filter(
                Customer.customer_id==c["customer_id"]
            ).first()
            if existing:
                existing.first_name=c["first_name"]
                existing.last_name=c["last_name"]
                existing.email=c["email"]
            else:
                new_customer=Customer(**c)
                db.add(new_customer)
            total_records+=1
        db.commit()
        page+=1

    return total_records