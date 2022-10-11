from fastapi import APIRouter, HTTPException, Security
from typing import Optional, List

import qsbi.api.schemas.party as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()


@router.post("", status_code=201, response_model=schema.Party)
async def create_party(
        *,
        party_in: schema.PartyCreate,
        curr_user=Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Party:
    """
    create a new party
    """
    party: schema.Party = await crud.party.create(party_in)
    return party


@router.get("/list", status_code=200, response_model=List[schema.Party])
async def list_partys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Party]:
    """
    list all partys
    """
    partys: List[schema.Party] = await crud.party.list(skip, limit)
    return partys


@router.post("/search", status_code=200, response_model=List[schema.Party])
async def search_partys(
        *,
        party_in: schema.Party,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Party]:
    """
    search partys
    """
    partys: List[schema.Party] = await crud.party.search(party_in, limit)
    return partys


@router.get("/id/{id}", status_code=200, response_model=schema.Party)
async def get_party_by_id(
        *,
        id: int,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Party]:
    """
    get party by id
    """
    result: Optional[schema.Party] = await crud.party.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party with id {id} not found"
        )
    return result


@router.get("/name/{name}", status_code=200, response_model=schema.Party)
async def get_party_by_name(
        *,
        name: str,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Party]:
    """
    get party by name
    """
    result: Optional[schema.Party] = await crud.party.get_by('name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party with name {name} not found"
        )
    return result


@router.get("/count", status_code=200, response_model=int)
async def count_partys(
        *,
        curr_user=Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all partys
    """
    count: int = await crud.party.count()
    return count


@router.put("", status_code=201, response_model=schema.Party)
async def update_party(
        *,
        party_in: schema.PartyUpdate,
        curr_user=Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Party]:
    """
    update existing party
    """
    result: Optional[schema.Party] = await crud.party.update(party_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party {party_in} not found"
        )
    return result


@router.delete("", status_code=200, response_model=schema.Party)
async def delete_party(
        *,
        party_in: schema.PartyDelete,
        curr_user=Security(auth.get_current_active_user, scopes=["delete"]),
        ) -> Optional[schema.Party]:
    """
    delete one party
    """
    result: Optional[schema.Party] = await crud.party.delete(party_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Party {party_in} not found"
        )
    return result
