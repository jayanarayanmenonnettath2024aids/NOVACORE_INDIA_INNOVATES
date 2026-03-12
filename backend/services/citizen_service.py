from sqlalchemy.orm import Session
from backend.models.all_models import Citizen
from backend.schemas.all_schemas import CitizenCreate, CitizenUpdate
import uuid

class CitizenService:
    @staticmethod
    def get_citizen_by_phone(db: Session, phone_number: str):
        return db.query(Citizen).filter(Citizen.phone_number == phone_number).first()

    @staticmethod
    def get_citizen_by_uuid(db: Session, citizen_uuid: str):
        return db.query(Citizen).filter(Citizen.citizen_uuid == citizen_uuid).first()

    @staticmethod
    def create_citizen(db: Session, citizen_in: CitizenCreate):
        db_citizen = Citizen(
            citizen_uuid=str(uuid.uuid4()),
            **citizen_in.dict()
        )
        db.add(db_citizen)
        db.commit()
        db.refresh(db_citizen)
        return db_citizen

    @staticmethod
    def update_citizen(db: Session, citizen_id: int, citizen_in: CitizenUpdate):
        db_citizen = db.query(Citizen).filter(Citizen.id == citizen_id).first()
        if not db_citizen:
            return None
            
        update_data = citizen_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_citizen, field, value)
            
        db.add(db_citizen)
        db.commit()
        db.refresh(db_citizen)
        return db_citizen

citizen_service = CitizenService()
