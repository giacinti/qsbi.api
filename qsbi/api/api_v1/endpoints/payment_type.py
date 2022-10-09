from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.payment_type as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.PaymentType)
async def create_payment_type(
        *,
        payment_type_in: schema.PaymentTypeCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.PaymentType:
    """
    create a new payment_type
    """
    payment_type: schema.PaymentType  = await crud.payment_type.create(payment_type_in)
    return payment_type

## READ
@router.get("/list", status_code=200, response_model=List[schema.PaymentType])
async def list_payment_types(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.PaymentType]:
    """
    list all payment_types
    """
    payment_types: List[schema.PaymentType] = await crud.payment_type.list(skip, limit)
    return payment_types

@router.post("/search", status_code=200, response_model=List[schema.PaymentType])
async def search_payment_types(
        *,
        payment_type_in: schema.PaymentType,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.PaymentType]:
    """
    search payment_types
    """
    payment_types: List[schema.PaymentType] = await crud.payment_type.search(payment_type_in, limit)
    return payment_types

@router.get("/id/{id}", status_code=200, response_model=schema.PaymentType)
async def get_payment_type_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.PaymentType]:
    """
    get payment_type by id
    """
    result: Optional[schema.PaymentType] = await crud.payment_type.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.PaymentType)
async def get_payment_type_by_name(
        *,
        name: str,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.PaymentType]:
    """
    get payment_type by name
    """
    result: Optional[schema.PaymentType] = await crud.payment_type.get_by('name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType with name {name} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_payment_types(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all payment_types
    """
    count: int = await crud.payment_type.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.PaymentType)
async def update_payment_type(
        *,
        payment_type_in: schema.PaymentTypeUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.PaymentType]:
    """
    update existing payment_type
    """
    result: Optional[schema.PaymentType] = await crud.payment_type.update(payment_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType {payment_type_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.PaymentType)
async def delete_payment_type(
        *,
        payment_type_in: schema.PaymentTypeDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.PaymentType]:
    """
    delete one payment_type
    """
    result: Optional[schema.PaymentType] = await crud.payment_type.delete(payment_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType {payment_type_in} not found"
        )
    return result