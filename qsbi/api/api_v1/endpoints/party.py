from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.party as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Party)
def create_party(
        *,
        party_in: schema.PartyCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Party:
    """
    create a new party
    """
    party = crud.party.create(sess, party_in)
    return party

## READ
@router.get("/list", status_code=200, response_model=schema.PartySeq)
def list_partys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.PartySeq:
    """
    list all partys
    """
    partys = crud.party.list(sess, skip, limit)
    return {"results": partys}

@router.post("/search", status_code=200, response_model=schema.PartySeq)
def search_partys(
        *,
        party_in: schema.PartyRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.PartySeq:
    """
    search partys
    """
    partys = crud.party.search(sess, party_in, limit)
    return {"results": partys}

@router.get("/id/{id}", status_code=200, response_model=schema.Party)
def get_party_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Party]:
    """
    get party by id
    """
    result = crud.party.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Party)
def get_party_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Party]:
    """
    get party by name
    """
    result = crud.party.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Party)
def update_party(
        *,
        party_in: schema.PartyUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Party]:
    """
    update existing party
    """
    result = crud.party.update(sess, party_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party {party_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.PartyDict)
def delete_party(
        *,
        party_in: schema.PartyDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one party
    """
    result = crud.party.delete(sess, party_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party {party_in} not found"
        )
    return result
