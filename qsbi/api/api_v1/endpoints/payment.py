from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, Dict

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
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Payment:
    """
    create a new payment
    """
    payment = await crud.payment.create(sess, payment_in)
    return payment

## READ
@router.get("/list", status_code=200, response_model=schema.PaymentSeq)
async def list_payments(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.PaymentSeq:
    """
    list all payments
    """
    payments = await crud.payment.list(sess, skip, limit)
    return {"results": payments}

@router.post("/search", status_code=200, response_model=schema.PaymentSeq)
async def search_payments(
        *,
        payment_in: schema.PaymentRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> schema.PaymentSeq:
    """
    search payments
    """
    payments = await crud.payment.search(sess, payment_in, limit)
    return {"results": payments}

@router.get("/id/{id}", status_code=200, response_model=schema.Payment)
async def get_payment_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Payment]:
    """
    get payment by id
    """
    result = await crud.payment.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_payments(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all payments
    """
    count = await crud.payment.count(sess)
    return {"count": count}

## UPDATE
@router.put("", status_code=201, response_model=schema.Payment)
async def update_payment(
        *,
        payment_in: schema.PaymentUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Payment]:
    """
    update existing payment
    """
    result = await crud.payment.update(sess, payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.PaymentDict)
async def delete_payment(
        *,
        payment_in: schema.PaymentDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[Dict]:
    """
    delete one payment
    """
    result = await crud.payment.delete(sess, payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result