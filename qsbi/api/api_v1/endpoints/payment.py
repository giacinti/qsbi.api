from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.payment as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.Payment)
async def create_payment(
        *,
        payment_in: schema.PaymentCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Payment:
    """
    create a new payment
    """
    payment: schema.Payment  = await crud.payment.create(payment_in)
    return payment

## READ
@router.get("/list", status_code=200, response_model=List[schema.Payment])
async def list_payments(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Payment]:
    """
    list all payments
    """
    payments: List[schema.Payment] = await crud.payment.list(skip, limit)
    return payments

@router.post("/search", status_code=200, response_model=List[schema.Payment])
async def search_payments(
        *,
        payment_in: schema.Payment,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Payment]:
    """
    search payments
    """
    payments: List[schema.Payment] = await crud.payment.search(payment_in, limit)
    return payments

@router.get("/id/{id}", status_code=200, response_model=schema.Payment)
async def get_payment_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Payment]:
    """
    get payment by id
    """
    result: Optional[schema.Payment] = await crud.payment.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_payments(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all payments
    """
    count: int = await crud.payment.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.Payment)
async def update_payment(
        *,
        payment_in: schema.PaymentUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Payment]:
    """
    update existing payment
    """
    result: Optional[schema.Payment] = await crud.payment.update(payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.Payment)
async def delete_payment(
        *,
        payment_in: schema.PaymentDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.Payment]:
    """
    delete one payment
    """
    result: Optional[schema.Payment] = await crud.payment.delete(payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result