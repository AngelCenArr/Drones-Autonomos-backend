from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict

class RolBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class RolResponse(RolBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Esquema para login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Esquema para registro
class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    rol_id: int  # 1 para ADMIN, 2 para GUARDIA

# Esquema de respuesta pública (sin password_hash)
class UserResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    activo: bool
    rol: RolResponse
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)