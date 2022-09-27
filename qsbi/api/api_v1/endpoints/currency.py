from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.currency as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Currency)
async def create_currency(
        *,
        currency_in: schema.CurrencyCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Currency:
    """
    create a new currency
    """
    currency = await crud.currency.create(sess, currency_in)
    return currency

## READ
@router.get("/list", status_code=200, response_model=schema.CurrencySeq)
async def list_currencys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CurrencySeq:
    """
    list all currencys
    """
    currencys = await crud.currency.list(sess, skip, limit)
    return {"results": currencys}

@router.post("/search", status_code=200, response_model=schema.CurrencySeq)
async def search_currencys(
        *,
        currency_in: schema.CurrencyRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CurrencySeq:
    """
    search currencys
    """
    currencys = await crud.currency.search(sess, currency_in, limit)
    return {"results": currencys}

@router.get("/id/{id}", status_code=200, response_model=schema.Currency)
async def get_currency_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by id
    """
    result = await crud.currency.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Currency)
async def get_currency_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by name
    """
    result = await crud.currency.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with name {name} not found"
        )
    return result
  
@router.get("/nickname/{nickname}", status_code=200, response_model=schema.Currency)
async def get_currency_by_nickname(
        *,
        nickname: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by nickname
    """
    result = await crud.currency.get_by(sess, 'nickname', nickname)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with nickname {nickname} not found"
        )
    return result
  
@router.get("/code/{code}", status_code=200, response_model=schema.Currency)
async def get_currency_by_code(
        *,
        code: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by code
    """
    result = await crud.currency.get_by(sess, 'code', code)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with code {code} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_currencys(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all currencys
    """
    count = await crud.currency.count(sess)
    return {"count": count}

## UPDATE
@router.put("/", status_code=201, response_model=schema.Currency)
async def update_currency(
        *,
        currency_in: schema.CurrencyUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    update existing currency
    """
    result = await crud.currency.update(sess, currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.CurrencyDict)
async def delete_currency(
        *,
        currency_in: schema.CurrencyDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one currency
    """
    result = await crud.currency.delete(sess, currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result