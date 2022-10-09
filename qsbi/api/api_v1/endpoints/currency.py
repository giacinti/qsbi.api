from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.currency as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.Currency)
async def create_currency(
        *,
        currency_in: schema.CurrencyCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Currency:
    """
    create a new currency
    """
    currency: schema.Currency  = await crud.currency.create(currency_in)
    return currency

## READ
@router.get("/list", status_code=200, response_model=List[schema.Currency])
async def list_currencys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Currency]:
    """
    list all currencys
    """
    currencys: List[schema.Currency] = await crud.currency.list(skip, limit)
    return currencys

@router.post("/search", status_code=200, response_model=List[schema.Currency])
async def search_currencys(
        *,
        currency_in: schema.Currency,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Currency]:
    """
    search currencys
    """
    currencys: List[schema.Currency] = await crud.currency.search(currency_in, limit)
    return currencys

@router.get("/id/{id}", status_code=200, response_model=schema.Currency)
async def get_currency_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Currency]:
    """
    get currency by id
    """
    result: Optional[schema.Currency] = await crud.currency.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Currency)
async def get_currency_by_name(
        *,
        name: str,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Currency]:
    """
    get currency by name
    """
    result: Optional[schema.Currency] = await crud.currency.get_by('name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with name {name} not found"
        )
    return result
  
@router.get("/nickname/{nickname}", status_code=200, response_model=schema.Currency)
async def get_currency_by_nickname(
        *,
        nickname: str,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Currency]:
    """
    get currency by nickname
    """
    result: Optional[schema.Currency] = await crud.currency.get_by('nickname', nickname)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with nickname {nickname} not found"
        )
    return result
  
@router.get("/code/{code}", status_code=200, response_model=schema.Currency)
async def get_currency_by_code(
        *,
        code: str,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Currency]:
    """
    get currency by code
    """
    result: Optional[schema.Currency] = await crud.currency.get_by('code', code)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency with code {code} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_currencys(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all currencys
    """
    count: int = await crud.currency.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.Currency)
async def update_currency(
        *,
        currency_in: schema.CurrencyUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Currency]:
    """
    update existing currency
    """
    result: Optional[schema.Currency] = await crud.currency.update(currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.Currency)
async def delete_currency(
        *,
        currency_in: schema.CurrencyDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.Currency]:
    """
    delete one currency
    """
    result: Optional[schema.Currency] = await crud.currency.delete(currency_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Currency {currency_in} not found"
        )
    return result