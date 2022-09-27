from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.payment
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.payment.Payment)
def create_payment(
        *,
        payment_in: qsbi.api.schemas.payment.PaymentCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.payment.Payment:
    """
    create a new payment
    """
    payment = qsbi.crud.payment.create(sess, payment_in)
    return payment

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.payment.PaymentSeq)
def list_payments(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.payment.PaymentSeq:
    """
    list all payments
    """
    payments = qsbi.crud.payment.list(sess, skip, limit)
    return {"results": payments}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.payment.PaymentSeq)
def search_payments(
        *,
        payment_in: qsbi.api.schemas.payment.PaymentRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.payment.PaymentSeq:
    """
    search payments
    """
    payments = qsbi.crud.payment.search(sess, payment_in, limit)
    return {"results": payments}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.payment.Payment)
def get_payment_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.payment.Payment]:
    """
    get payment by id
    """
    result = qsbi.crud.payment.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.payment.Payment)
def update_payment(
        *,
        payment_in: qsbi.api.schemas.payment.PaymentUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.payment.Payment]:
    """
    update existing payment
    """
    result = qsbi.crud.payment.update(sess, payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.payment.PaymentDict)
def delete_payment(
        *,
        payment_in: qsbi.api.schemas.payment.PaymentDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one payment
    """
    result = qsbi.crud.payment.delete(sess, payment_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Payment {payment_in} not found"
        )
    return result
