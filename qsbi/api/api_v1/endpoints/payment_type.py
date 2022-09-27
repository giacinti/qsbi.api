from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.payment_type
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.payment_type.PaymentType)
def create_payment_type(
        *,
        payment_type_in: qsbi.api.schemas.payment_type.PaymentTypeCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.payment_type.PaymentType:
    """
    create a new payment_type
    """
    payment_type = qsbi.crud.payment_type.create(sess, payment_type_in)
    return payment_type

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.payment_type.PaymentTypeSeq)
def list_payment_types(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.payment_type.PaymentTypeSeq:
    """
    list all payment_types
    """
    payment_types = qsbi.crud.payment_type.list(sess, skip, limit)
    return {"results": payment_types}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.payment_type.PaymentTypeSeq)
def search_payment_types(
        *,
        payment_type_in: qsbi.api.schemas.payment_type.PaymentTypeRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.payment_type.PaymentTypeSeq:
    """
    search payment_types
    """
    payment_types = qsbi.crud.payment_type.search(sess, payment_type_in, limit)
    return {"results": payment_types}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.payment_type.PaymentType)
def get_payment_type_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.payment_type.PaymentType]:
    """
    get payment_type by id
    """
    result = qsbi.crud.payment_type.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=qsbi.api.schemas.payment_type.PaymentType)
def get_payment_type_by_name(
        *,
        name: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.payment_type.PaymentType]:
    """
    get payment_type by name
    """
    result = qsbi.crud.payment_type.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.payment_type.PaymentType)
def update_payment_type(
        *,
        payment_type_in: qsbi.api.schemas.payment_type.PaymentTypeUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.payment_type.PaymentType]:
    """
    update existing payment_type
    """
    result = qsbi.crud.payment_type.update(sess, payment_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType {payment_type_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.payment_type.PaymentTypeDict)
def delete_payment_type(
        *,
        payment_type_in: qsbi.api.schemas.payment_type.PaymentTypeDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one payment_type
    """
    result = qsbi.crud.payment_type.delete(sess, payment_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType {payment_type_in} not found"
        )
    return result
