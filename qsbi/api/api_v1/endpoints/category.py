from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.category
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.category.Category)
def create_category(
        *,
        category_in: qsbi.api.schemas.category.CategoryCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.category.Category:
    """
    create a new category
    """
    category = qsbi.crud.category.create(sess, category_in)
    return category

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.category.CategorySeq)
def list_categorys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.category.CategorySeq:
    """
    list all categorys
    """
    categorys = qsbi.crud.category.list(sess, skip, limit)
    return {"results": categorys}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.category.CategorySeq)
def search_categorys(
        *,
        category_in: qsbi.api.schemas.category.CategoryRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.category.CategorySeq:
    """
    search categorys
    """
    categorys = qsbi.crud.category.search(sess, category_in, limit)
    return {"results": categorys}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.category.Category)
def get_category_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.category.Category]:
    """
    get category by id
    """
    result = qsbi.crud.category.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=qsbi.api.schemas.category.Category)
def get_category_by_name(
        *,
        name: str,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.category.Category]:
    """
    get category by name
    """
    result = qsbi.crud.category.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.category.Category)
def update_category(
        *,
        category_in: qsbi.api.schemas.category.CategoryUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.category.Category]:
    """
    update existing category
    """
    result = qsbi.crud.category.update(sess, category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.category.CategoryDict)
def delete_category(
        *,
        category_in: qsbi.api.schemas.category.CategoryDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one category
    """
    result = qsbi.crud.category.delete(sess, category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result
