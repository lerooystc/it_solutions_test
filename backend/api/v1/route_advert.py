from db.repository.advert import retrieve_advert, create_new_advert
from db import User
from api.v1.route_login import get_current_user
from schemas.advert import ShowAdvert, CreateAdvert
from db.session import get_db
from fastapi import APIRouter, Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session


router = APIRouter()

@router.get(
    "/adverts/{id}", response_model=ShowAdvert, status_code=status.HTTP_200_OK
)
async def get_advert(id: int, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    advert = retrieve_advert(id=id, db=db, user=current_user.id)
    if isinstance(advert,dict):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=advert.get("error")
        )
    return advert


@router.post("/adverts", response_model=ShowAdvert, status_code=status.HTTP_201_CREATED)
async def create_advert(
    advert: CreateAdvert,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    advert = create_new_advert(advert=advert, db=db, user=current_user.id)
    return advert