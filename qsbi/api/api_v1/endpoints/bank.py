from fastapi import APIRouter, HTTPException, Security
from typing import Optional, List

import qsbi.api.schemas.bank as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()


@router.post("", status_code=201, response_model=schema.Bank)
async def create_bank(
        *,
        bank_in: schema.BankCreate,
        curr_user=Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Bank:
    """
    create a new bank
    """
    bank: schema.Bank = await crud.bank.create(bank_in)
    return bank


@router.get("/list", status_code=200, response_model=List[schema.Bank])
async def list_banks(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Bank]:
    """
    list all banks
    """
    banks: List[schema.Bank] = await crud.bank.list(skip, limit)
    return banks


@router.post("/search", status_code=200, response_model=List[schema.Bank])
async def search_banks(
        *,
        bank_in: schema.Bank,
        limit: Optional[int] = 100,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Bank]:
    """
    search banks
    """
    banks: List[schema.Bank] = await crud.bank.search(bank_in, limit)
    return banks


@router.get("/id/{id}", status_code=200, response_model=schema.Bank)
async def get_bank_by_id(
        *,
        id: int,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Bank]:
    """
    get bank by id
    """
    result: Optional[schema.Bank] = await crud.bank.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank with id {id} not found"
        )
    return result


@router.get("/name/{name}", status_code=200, response_model=schema.Bank)
async def get_bank_by_name(
        *,
        name: str,
        curr_user=Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Bank]:
    """
    get bank by name
    """
    result: Optional[schema.Bank] = await crud.bank.get_by('name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank with name {name} not found"
        )
    return result


@router.get("/count", status_code=200, response_model=int)
async def count_banks(
        *,
        curr_user=Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all banks
    """
    count: int = await crud.bank.count()
    return count


@router.put("", status_code=201, response_model=schema.Bank)
async def update_bank(
        *,
        bank_in: schema.BankUpdate,
        curr_user=Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Bank]:
    """
    update existing bank
    """
    result: Optional[schema.Bank] = await crud.bank.update(bank_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank {bank_in} not found"
        )
    return result


@router.delete("", status_code=200, response_model=schema.Bank)
async def delete_bank(
        *,
        bank_in: schema.BankDelete,
        curr_user=Security(auth.get_current_active_user, scopes=["delete"]),
        ) -> Optional[schema.Bank]:
    """
    delete one bank
    """
    result: Optional[schema.Bank] = await crud.bank.delete(bank_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank {bank_in} not found"
        )
    return result
