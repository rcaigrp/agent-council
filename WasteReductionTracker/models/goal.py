from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class SustainabilityGoal(Base):
    __tablename__ = 'sustainability_goals'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    target_weight_kg = Column(Float, nullable=False)
    deadline = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    waste_items = relationship("WasteItem", back_populates="goal")

    def __repr__(self):
        return f"<SustainabilityGoal(id={self.id}, title='{self.title}', target_weight_kg={self.target_weight_kg})>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'target_weight_kg': self.target_weight_kg,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }