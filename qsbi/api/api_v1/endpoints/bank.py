from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.bank
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.bank.Bank)
def create_bank(
        *,
        bank_in: qsbi.api.schemas.bank.BankCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.bank.Bank:
    """
    create a new bank
    """
    bank = qsbi.crud.bank.create(sess, bank_in)
    return bank

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.bank.BankSeq)
def list_banks(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.bank.BankSeq:
    """
    list all banks
    """
    banks = qsbi.crud.bank.list(sess, skip, limit)
    return {"results": banks}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.bank.BankSeq)
def search_banks(
        *,
        bank_in: qsbi.api.schemas.bank.BankRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.bank.BankSeq:
    """
    search banks
    """
    banks = qsbi.crud.bank.search(sess, bank_in, limit)
    return {"results": banks}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.bank.Bank)
def get_bank_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.bank.Bank]:
    """
    get bank by id
    """
    result = qsbi.crud.bank.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=qsbi.api.schemas.bank.Bank)
def get_bank_by_name(
        *,
        name: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.bank.Bank]:
    """
    get bank by name
    """
    result = qsbi.crud.bank.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.bank.Bank)
def update_bank(
        *,
        bank_in: qsbi.api.schemas.bank.BankUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.bank.Bank]:
    """
    update existing bank
    """
    result = qsbi.crud.bank.update(sess, bank_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank {bank_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.bank.BankDict)
def delete_bank(
        *,
        bank_in: qsbi.api.schemas.bank.BankDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one bank
    """
    result = qsbi.crud.bank.delete(sess, bank_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank {bank_in} not found"
        )
    return result
