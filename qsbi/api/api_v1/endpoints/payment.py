from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.payment as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Payment)
def create_payment(
        *,
        payment_in: schema.PaymentCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Payment:
    """
    create a new payment
    """
    payment = crud.payment.create(sess, payment_in)
    return payment

## READ
@router.get("/list", status_code=200, response_model=schema.PaymentSeq)
def list_payments(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.PaymentSeq:
    """
    list all payments
    """
    payments = crud.payment.list(sess, skip, limit)
    return {"results": payments}

@router.post("/search", status_code=200, response_model=schema.PaymentSeq)
def search_payments(
        *,
        payment_in: schema.PaymentRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.PaymentSeq:
    """
    search payments
    """
    payments = crud.payment.search(sess, payment_in, limit)
    return {"results": payments}

@router.get("/id/{id}", status_code=200, response_model=schema.Payment)
def get_payment_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Payment]:
    """
    get payment by id
    """
    result = crud.payment.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Payment)
def update_payment(
        *,
        payment_in: schema.PaymentUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Payment]:
    """
    update existing payment
    """
    result = crud.payment.update(sess, payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.PaymentDict)
def delete_payment(
        *,
        payment_in: schema.PaymentDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one payment
    """
    result = crud.payment.delete(sess, payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result
