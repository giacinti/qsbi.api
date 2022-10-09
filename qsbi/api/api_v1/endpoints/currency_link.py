from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.currency_link as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.CurrencyLink)
async def create_currency_link(
        *,
        currency_link_in: schema.CurrencyLinkCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.CurrencyLink:
    """
    create a new currency_link
    """
    currency_link: schema.CurrencyLink  = await crud.currency_link.create(currency_link_in)
    return currency_link

## READ
@router.get("/list", status_code=200, response_model=List[schema.CurrencyLink])
async def list_currency_links(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.CurrencyLink]:
    """
    list all currency_links
    """
    currency_links: List[schema.CurrencyLink] = await crud.currency_link.list(skip, limit)
    return currency_links

@router.post("/search", status_code=200, response_model=List[schema.CurrencyLink])
async def search_currency_links(
        *,
        currency_link_in: schema.CurrencyLink,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.CurrencyLink]:
    """
    search currency_links
    """
    currency_links: List[schema.CurrencyLink] = await crud.currency_link.search(currency_link_in, limit)
    return currency_links

@router.get("/id/{id}", status_code=200, response_model=schema.CurrencyLink)
async def get_currency_link_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.CurrencyLink]:
    """
    get currency_link by id
    """
    result: Optional[schema.CurrencyLink] = await crud.currency_link.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_currency_links(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all currency_links
    """
    count: int = await crud.currency_link.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.CurrencyLink)
async def update_currency_link(
        *,
        currency_link_in: schema.CurrencyLinkUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.CurrencyLink]:
    """
    update existing currency_link
    """
    result: Optional[schema.CurrencyLink] = await crud.currency_link.update(currency_link_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink {currency_link_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.CurrencyLink)
async def delete_currency_link(
        *,
        currency_link_in: schema.CurrencyLinkDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.CurrencyLink]:
    """
    delete one currency_link
    """
    result: Optional[schema.CurrencyLink] = await crud.currency_link.delete(currency_link_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink {currency_link_in} not found"
        )
    return result