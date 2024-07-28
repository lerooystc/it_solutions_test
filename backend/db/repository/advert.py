from db.models.advert import Advert
from schemas.advert import CreateAdvert
from sqlalchemy.orm import Session


def retrieve_advert(id: int, db: Session, user: int):
    if not user:
        return {"error": "Not authorized."}
    advert = db.query(Advert).filter(Advert.id == id).first()
    return advert


def create_new_advert(advert: CreateAdvert, db: Session, user: int):
    if not user:
        return {"error": "Not authorized."}
    advert = Advert(
        **advert.model_dump(),
    )
    db.add(advert)
    db.commit()
    db.refresh(advert)
    return advert
