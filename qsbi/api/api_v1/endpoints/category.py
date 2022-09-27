from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.category as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.Category)
async def create_category(
        *,
        category_in: schema.CategoryCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.Category:
    """
    create a new category
    """
    category = await crud.category.create(sess, category_in)
    return category

## READ
@router.get("/list", status_code=200, response_model=schema.CategorySeq)
async def list_categorys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CategorySeq:
    """
    list all categorys
    """
    categorys = await crud.category.list(sess, skip, limit)
    return {"results": categorys}

@router.post("/search", status_code=200, response_model=schema.CategorySeq)
async def search_categorys(
        *,
        category_in: schema.CategoryRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.CategorySeq:
    """
    search categorys
    """
    categorys = await crud.category.search(sess, category_in, limit)
    return {"results": categorys}

@router.get("/id/{id}", status_code=200, response_model=schema.Category)
async def get_category_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Category]:
    """
    get category by id
    """
    result = await crud.category.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Category)
async def get_category_by_name(
        *,
        name: str,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Category]:
    """
    get category by name
    """
    result = await crud.category.get_by(sess, 'name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with name {name} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_categorys(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all categorys
    """
    count = await crud.category.count(sess)
    return {"count": count}

## UPDATE
@router.put("/", status_code=201, response_model=schema.Category)
async def update_category(
        *,
        category_in: schema.CategoryUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.Category]:
    """
    update existing category
    """
    result = await crud.category.update(sess, category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.CategoryDict)
async def delete_category(
        *,
        category_in: schema.CategoryDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one category
    """
    result = await crud.category.delete(sess, category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result