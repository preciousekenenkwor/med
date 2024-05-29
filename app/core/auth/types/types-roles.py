from dataclasses import dataclass


@dataclass
class Role:
    id: int
    name: str
    guard_name: str
    business_id: int
    is_default: bool
    created_at: str  # Consider using a proper datetime type if available in your Python environment
    updated_at: str  # Consider using a proper datetime type if available in your Python environment

@dataclass
class ModelHasPermission:
    permission_id: int
    model_id: int
    model_type: str

@dataclass
class ModelHasRole:
    role_id: int
    model_id: int
    model_type: str

@dataclass
class RoleHasPermission:
    permission_id: int
    role_id: int
