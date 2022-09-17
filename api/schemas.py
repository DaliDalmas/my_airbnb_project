from datetime import date
from pydantic import BaseModel

class AirbnbBase(BaseModel):
    host_identity_verified: bool
    neighbourhood_group: str
    lat: float
    long: float
    instant_bookable: bool
    cancellation_policy: str
    room_type: str
    construction_year: int
    price: float
    service_fee: float
    minimum_nights: float
    number_of_reviews: float
    reviews_per_month: float
    review_rate_number: float
    calculated_host_listings_count: float
    availability_365: float
    missing_house_rules: bool
    clean_last_review: date
    clean_accomodation_bio: str

class AirbnbCreate(AirbnbBase):
    id: str

class Airbnb(AirbnbBase):
    id: str

    class Config:
        # Pydantic's orm_mode will tell the Pydantic model to read the 
        # data even if it is not a dict
        orm_mode = True