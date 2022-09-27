from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.currency_link as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.CurrencyLink)
async def create_currency_link(
        *,
        currency_link_in: schema.CurrencyLinkCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CurrencyLink:
    """
    create a new currency_link
    """
    currency_link = await crud.currency_link.create(sess, currency_link_in)
    return currency_link

## READ
@router.get("/list", status_code=200, response_model=schema.CurrencyLinkSeq)
async def list_currency_links(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CurrencyLinkSeq:
    """
    list all currency_links
    """
    currency_links = await crud.currency_link.list(sess, skip, limit)
    return {"results": currency_links}

@router.post("/search", status_code=200, response_model=schema.CurrencyLinkSeq)
async def search_currency_links(
        *,
        currency_link_in: schema.CurrencyLinkRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CurrencyLinkSeq:
    """
    search currency_links
    """
    currency_links = await crud.currency_link.search(sess, currency_link_in, limit)
    return {"results": currency_links}

@router.get("/id/{id}", status_code=200, response_model=schema.CurrencyLink)
async def get_currency_link_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.CurrencyLink]:
    """
    get currency_link by id
    """
    result = await crud.currency_link.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_currency_links(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all currency_links
    """
    count = await crud.currency_link.count(sess)
    return {"count": count}

## UPDATE
@router.put("/", status_code=201, response_model=schema.CurrencyLink)
async def update_currency_link(
        *,
        currency_link_in: schema.CurrencyLinkUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.CurrencyLink]:
    """
    update existing currency_link
    """
    result = await crud.currency_link.update(sess, currency_link_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink {currency_link_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.CurrencyLinkDict)
async def delete_currency_link(
        *,
        currency_link_in: schema.CurrencyLinkDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one currency_link
    """
    result = await crud.currency_link.delete(sess, currency_link_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink {currency_link_in} not found"
        )
    return result