from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.category as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Category)
def create_category(
        *,
        category_in: schema.CategoryCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Category:
    """
    create a new category
    """
    category = crud.category.create(sess, category_in)
    return category

## READ
@router.get("/list", status_code=200, response_model=schema.CategorySeq)
def list_categorys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CategorySeq:
    """
    list all categorys
    """
    categorys = crud.category.list(sess, skip, limit)
    return {"results": categorys}

@router.post("/search", status_code=200, response_model=schema.CategorySeq)
def search_categorys(
        *,
        category_in: schema.CategoryRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CategorySeq:
    """
    search categorys
    """
    categorys = crud.category.search(sess, category_in, limit)
    return {"results": categorys}

@router.get("/id/{id}", status_code=200, response_model=schema.Category)
def get_category_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Category]:
    """
    get category by id
    """
    result = crud.category.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Category)
def get_category_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Category]:
    """
    get category by name
    """
    result = crud.category.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with name {name} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=schema.Category)
def update_category(
        *,
        category_in: schema.CategoryUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Category]:
    """
    update existing category
    """
    result = crud.category.update(sess, category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.CategoryDict)
def delete_category(
        *,
        category_in: schema.CategoryDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one category
    """
    result = crud.category.delete(sess, category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result
