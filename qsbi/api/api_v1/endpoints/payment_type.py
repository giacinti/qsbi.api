from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.payment_type as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.PaymentType)
async def create_payment_type(
        *,
        payment_type_in: schema.PaymentTypeCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.PaymentType:
    """
    create a new payment_type
    """
    payment_type = await crud.payment_type.create(sess, payment_type_in)
    return payment_type

## READ
@router.get("/list", status_code=200, response_model=schema.PaymentTypeSeq)
async def list_payment_types(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.PaymentTypeSeq:
    """
    list all payment_types
    """
    payment_types = await crud.payment_type.list(sess, skip, limit)
    return {"results": payment_types}

@router.post("/search", status_code=200, response_model=schema.PaymentTypeSeq)
async def search_payment_types(
        *,
        payment_type_in: schema.PaymentTypeRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.PaymentTypeSeq:
    """
    search payment_types
    """
    payment_types = await crud.payment_type.search(sess, payment_type_in, limit)
    return {"results": payment_types}

@router.get("/id/{id}", status_code=200, response_model=schema.PaymentType)
async def get_payment_type_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.PaymentType]:
    """
    get payment_type by id
    """
    result = await crud.payment_type.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.PaymentType)
async def get_payment_type_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.PaymentType]:
    """
    get payment_type by name
    """
    result = await crud.payment_type.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType with name {name} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_payment_types(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all payment_types
    """
    count = await crud.payment_type.count(sess)
    return {"count": count}

## UPDATE
@router.put("/", status_code=201, response_model=schema.PaymentType)
async def update_payment_type(
        *,
        payment_type_in: schema.PaymentTypeUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.PaymentType]:
    """
    update existing payment_type
    """
    result = await crud.payment_type.update(sess, payment_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType {payment_type_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.PaymentTypeDict)
async def delete_payment_type(
        *,
        payment_type_in: schema.PaymentTypeDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one payment_type
    """
    result = await crud.payment_type.delete(sess, payment_type_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"PaymentType {payment_type_in} not found"
        )
    return result