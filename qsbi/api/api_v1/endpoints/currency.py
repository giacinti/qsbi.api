from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.currency as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Currency)
def create_currency(
        *,
        currency_in: schema.CurrencyCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Currency:
    """
    create a new currency
    """
    currency = crud.currency.create(sess, currency_in)
    return currency

## READ
@router.get("/list", status_code=200, response_model=schema.CurrencySeq)
def list_currencys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CurrencySeq:
    """
    list all currencys
    """
    currencys = crud.currency.list(sess, skip, limit)
    return {"results": currencys}

@router.post("/search", status_code=200, response_model=schema.CurrencySeq)
def search_currencys(
        *,
        currency_in: schema.CurrencyRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CurrencySeq:
    """
    search currencys
    """
    currencys = crud.currency.search(sess, currency_in, limit)
    return {"results": currencys}

@router.get("/id/{id}", status_code=200, response_model=schema.Currency)
def get_currency_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by id
    """
    result = crud.currency.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Currency)
def get_currency_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by name
    """
    result = crud.currency.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with name {name} not found"
        )
    return result
  
@router.get("/nickname/{nickname}", status_code=200, response_model=schema.Currency)
def get_currency_by_nickname(
        *,
        nickname: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by nickname
    """
    result = crud.currency.get_by(sess, 'nickname', nickname)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with nickname {nickname} not found"
        )
    return result
  
@router.get("/code/{code}", status_code=200, response_model=schema.Currency)
def get_currency_by_code(
        *,
        code: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    get currency by code
    """
    result = crud.currency.get_by(sess, 'code', code)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with code {code} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Currency)
def update_currency(
        *,
        currency_in: schema.CurrencyUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Currency]:
    """
    update existing currency
    """
    result = crud.currency.update(sess, currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.CurrencyDict)
def delete_currency(
        *,
        currency_in: schema.CurrencyDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one currency
    """
    result = crud.currency.delete(sess, currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result
