from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.party
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.party.Party)
def create_party(
        *,
        party_in: qsbi.api.schemas.party.PartyCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.party.Party:
    """
    create a new party
    """
    party = qsbi.crud.party.create(sess, party_in)
    return party

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.party.PartySeq)
def list_partys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.party.PartySeq:
    """
    list all partys
    """
    partys = qsbi.crud.party.list(sess, skip, limit)
    return {"results": partys}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.party.PartySeq)
def search_partys(
        *,
        party_in: qsbi.api.schemas.party.PartyRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.party.PartySeq:
    """
    search partys
    """
    partys = qsbi.crud.party.search(sess, party_in, limit)
    return {"results": partys}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.party.Party)
def get_party_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.party.Party]:
    """
    get party by id
    """
    result = qsbi.crud.party.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=qsbi.api.schemas.party.Party)
def get_party_by_name(
        *,
        name: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.party.Party]:
    """
    get party by name
    """
    result = qsbi.crud.party.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.party.Party)
def update_party(
        *,
        party_in: qsbi.api.schemas.party.PartyUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.party.Party]:
    """
    update existing party
    """
    result = qsbi.crud.party.update(sess, party_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party {party_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.party.PartyDict)
def delete_party(
        *,
        party_in: qsbi.api.schemas.party.PartyDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one party
    """
    result = qsbi.crud.party.delete(sess, party_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party {party_in} not found"
        )
    return result
