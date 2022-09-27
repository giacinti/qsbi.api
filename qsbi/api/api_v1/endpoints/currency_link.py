from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.currency_link
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.currency_link.CurrencyLink)
def create_currency_link(
        *,
        currency_link_in: qsbi.api.schemas.currency_link.CurrencyLinkCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.currency_link.CurrencyLink:
    """
    create a new currency_link
    """
    currency_link = qsbi.crud.currency_link.create(sess, currency_link_in)
    return currency_link

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.currency_link.CurrencyLinkSeq)
def list_currency_links(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.currency_link.CurrencyLinkSeq:
    """
    list all currency_links
    """
    currency_links = qsbi.crud.currency_link.list(sess, skip, limit)
    return {"results": currency_links}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.currency_link.CurrencyLinkSeq)
def search_currency_links(
        *,
        currency_link_in: qsbi.api.schemas.currency_link.CurrencyLinkRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.currency_link.CurrencyLinkSeq:
    """
    search currency_links
    """
    currency_links = qsbi.crud.currency_link.search(sess, currency_link_in, limit)
    return {"results": currency_links}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.currency_link.CurrencyLink)
def get_currency_link_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.currency_link.CurrencyLink]:
    """
    get currency_link by id
    """
    result = qsbi.crud.currency_link.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.currency_link.CurrencyLink)
def update_currency_link(
        *,
        currency_link_in: qsbi.api.schemas.currency_link.CurrencyLinkUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.currency_link.CurrencyLink]:
    """
    update existing currency_link
    """
    result = qsbi.crud.currency_link.update(sess, currency_link_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink {currency_link_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.currency_link.CurrencyLinkDict)
def delete_currency_link(
        *,
        currency_link_in: qsbi.api.schemas.currency_link.CurrencyLinkDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one currency_link
    """
    result = qsbi.crud.currency_link.delete(sess, currency_link_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"CurrencyLink {currency_link_in} not found"
        )
    return result
