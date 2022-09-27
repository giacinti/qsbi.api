from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.currency
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.currency.Currency)
def create_currency(
        *,
        currency_in: qsbi.api.schemas.currency.CurrencyCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.currency.Currency:
    """
    create a new currency
    """
    currency = qsbi.crud.currency.create(sess, currency_in)
    return currency

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.currency.CurrencySeq)
def list_currencys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.currency.CurrencySeq:
    """
    list all currencys
    """
    currencys = qsbi.crud.currency.list(sess, skip, limit)
    return {"results": currencys}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.currency.CurrencySeq)
def search_currencys(
        *,
        currency_in: qsbi.api.schemas.currency.CurrencyRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.currency.CurrencySeq:
    """
    search currencys
    """
    currencys = qsbi.crud.currency.search(sess, currency_in, limit)
    return {"results": currencys}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.currency.Currency)
def get_currency_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.currency.Currency]:
    """
    get currency by id
    """
    result = qsbi.crud.currency.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=qsbi.api.schemas.currency.Currency)
def get_currency_by_name(
        *,
        name: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.currency.Currency]:
    """
    get currency by name
    """
    result = qsbi.crud.currency.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with name {name} not found"
        )
    return result
  
@router.get("/nickname/{nickname}", status_code=200, response_model=qsbi.api.schemas.currency.Currency)
def get_currency_by_nickname(
        *,
        nickname: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.currency.Currency]:
    """
    get currency by nickname
    """
    result = qsbi.crud.currency.get_by(sess, 'nickname', nickname)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with nickname {nickname} not found"
        )
    return result
  
@router.get("/code/{code}", status_code=200, response_model=qsbi.api.schemas.currency.Currency)
def get_currency_by_code(
        *,
        code: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.currency.Currency]:
    """
    get currency by code
    """
    result = qsbi.crud.currency.get_by(sess, 'code', code)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with code {code} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.currency.Currency)
def update_currency(
        *,
        currency_in: qsbi.api.schemas.currency.CurrencyUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.currency.Currency]:
    """
    update existing currency
    """
    result = qsbi.crud.currency.update(sess, currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.currency.CurrencyDict)
def delete_currency(
        *,
        currency_in: qsbi.api.schemas.currency.CurrencyDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one currency
    """
    result = qsbi.crud.currency.delete(sess, currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result
