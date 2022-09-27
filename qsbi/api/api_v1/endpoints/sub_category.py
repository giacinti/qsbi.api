from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.base
import qsbi.api.schemas.sub_category as schema
import qsbi.api.crud as crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=schema.SubCategory)
async def create_sub_category(
        *,
        sub_category_in: schema.SubCategoryCreate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.SubCategory:
    """
    create a new sub_category
    """
    sub_category = await crud.sub_category.create(sess, sub_category_in)
    return sub_category

## READ
@router.get("/list", status_code=200, response_model=schema.SubCategorySeq)
async def list_sub_categorys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.SubCategorySeq:
    """
    list all sub_categorys
    """
    sub_categorys = await crud.sub_category.list(sess, skip, limit)
    return {"results": sub_categorys}

@router.post("/search", status_code=200, response_model=schema.SubCategorySeq)
async def search_sub_categorys(
        *,
        sub_category_in: schema.SubCategoryRead,
        limit: Optional[int] = 100,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> schema.SubCategorySeq:
    """
    search sub_categorys
    """
    sub_categorys = await crud.sub_category.search(sess, sub_category_in, limit)
    return {"results": sub_categorys}

@router.get("/id/{id}", status_code=200, response_model=schema.SubCategory)
async def get_sub_category_by_id(
        *,
        id: int,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.SubCategory]:
    """
    get sub_category by id
    """
    result = await crud.sub_category.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=qsbi.api.schemas.base.CountResult)
async def count_sub_categorys(
        *,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> qsbi.api.schemas.base.CountResult:
    """
    count all sub_categorys
    """
    count = await crud.sub_category.count(sess)
    return {"count": count}

## UPDATE
@router.put("/", status_code=201, response_model=schema.SubCategory)
async def update_sub_category(
        *,
        sub_category_in: schema.SubCategoryUpdate,
        sess: crud.CRUDSession = Depends(crud.get_session),
        ) -> Optional[schema.SubCategory]:
    """
    update existing sub_category
    """
    result = await crud.sub_category.update(sess, sub_category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory {sub_category_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=schema.SubCategoryDict)
async def delete_sub_category(
        *,
        sub_category_in: schema.SubCategoryDelete,
        sess: crud.CRUDSession = Depends(crud.get_session),
	) -> Optional[Dict]:
    """
    delete one sub_category
    """
    result = await crud.sub_category.delete(sess, sub_category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory {sub_category_in} not found"
        )
    return result