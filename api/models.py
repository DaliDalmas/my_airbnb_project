from email.policy import default
from sqlalchemy import Column, Boolean, String, Float, Integer, Date

from .database import Base

class Airbnb(Base):
    __tablename__ = "airbnb"
    
    id = Column(String, primary_key=True, index=True)
    host_identity_verified = Column(Boolean, default=False)
    neighbourhood_group = Column(String)
    lat = Column(Float)
    long  = Column(Float)
    instant_bookable  = Column(Boolean, default=False)
    cancellation_policy = Column(String)
    room_type =  Column(String)
    construction_year =  Column(Integer)
    price  = Column(Float)
    service_fee  = Column(Float)
    minimum_nights  = Column(Float)
    number_of_reviews  = Column(Float)
    reviews_per_month  = Column(Float)
    review_rate_number  = Column(Float)
    calculated_host_listings_count  = Column(Float)
    availability_365  = Column(Float)
    missing_house_rules  = Column(Boolean, default=False)
    clean_last_review  = Column(Date)
    clean_accomodation_bio =  Column(String)