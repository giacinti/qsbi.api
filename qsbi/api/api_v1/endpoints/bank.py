from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.bank as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Bank)
def create_bank(
        *,
        bank_in: schema.BankCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Bank:
    """
    create a new bank
    """
    bank = crud.bank.create(sess, bank_in)
    return bank

## READ
@router.get("/list", status_code=200, response_model=schema.BankSeq)
def list_banks(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.BankSeq:
    """
    list all banks
    """
    banks = crud.bank.list(sess, skip, limit)
    return {"results": banks}

@router.post("/search", status_code=200, response_model=schema.BankSeq)
def search_banks(
        *,
        bank_in: schema.BankRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.BankSeq:
    """
    search banks
    """
    banks = crud.bank.search(sess, bank_in, limit)
    return {"results": banks}

@router.get("/id/{id}", status_code=200, response_model=schema.Bank)
def get_bank_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Bank]:
    """
    get bank by id
    """
    result = crud.bank.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Bank)
def get_bank_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Bank]:
    """
    get bank by name
    """
    result = crud.bank.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Bank)
def update_bank(
        *,
        bank_in: schema.BankUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Bank]:
    """
    update existing bank
    """
    result = crud.bank.update(sess, bank_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank {bank_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.BankDict)
def delete_bank(
        *,
        bank_in: schema.BankDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one bank
    """
    result = crud.bank.delete(sess, bank_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Bank {bank_in} not found"
        )
    return result
