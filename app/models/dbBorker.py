from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Criptomoneda(Base):
    __tablename__ = 'criptomonedas'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    symbol = Column(String(10), nullable=False, unique=True)
    msupply = Column(DECIMAL(20, 2))

    # Relación con registros
    registros = relationship("Registro", back_populates="criptomoneda")


class Registro(Base):
    __tablename__ = 'registros'
    
    id = Column(Integer, primary_key=True)
    criptomoneda_id = Column(Integer, ForeignKey('criptomonedas.id'))
    price_usd = Column(DECIMAL(20, 2))
    percent_change_24h = Column(DECIMAL(10, 2))
    percent_change_1h = Column(DECIMAL(10, 2))
    percent_change_7d = Column(DECIMAL(10, 2))
    price_btc = Column(DECIMAL(20, 2))
    market_cap_usd = Column(DECIMAL(20, 2))
    volume24 = Column(DECIMAL(20, 2))
    volume24a = Column(DECIMAL(20, 2))
    csupply = Column(DECIMAL(20, 2))
    tsupply = Column(DECIMAL(20, 2))
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')
    rank = Column(Integer)

    # Relación con criptomonedas
    criptomoneda = relationship("Criptomoneda", back_populates="registros")

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(150), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)