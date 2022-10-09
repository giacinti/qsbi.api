from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.sub_category as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.SubCategory)
async def create_sub_category(
        *,
        sub_category_in: schema.SubCategoryCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.SubCategory:
    """
    create a new sub_category
    """
    sub_category: schema.SubCategory  = await crud.sub_category.create(sub_category_in)
    return sub_category

## READ
@router.get("/list", status_code=200, response_model=List[schema.SubCategory])
async def list_sub_categorys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.SubCategory]:
    """
    list all sub_categorys
    """
    sub_categorys: List[schema.SubCategory] = await crud.sub_category.list(skip, limit)
    return sub_categorys

@router.post("/search", status_code=200, response_model=List[schema.SubCategory])
async def search_sub_categorys(
        *,
        sub_category_in: schema.SubCategory,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.SubCategory]:
    """
    search sub_categorys
    """
    sub_categorys: List[schema.SubCategory] = await crud.sub_category.search(sub_category_in, limit)
    return sub_categorys

@router.get("/id/{id}", status_code=200, response_model=schema.SubCategory)
async def get_sub_category_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.SubCategory]:
    """
    get sub_category by id
    """
    result: Optional[schema.SubCategory] = await crud.sub_category.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory with id {id} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_sub_categorys(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all sub_categorys
    """
    count: int = await crud.sub_category.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.SubCategory)
async def update_sub_category(
        *,
        sub_category_in: schema.SubCategoryUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.SubCategory]:
    """
    update existing sub_category
    """
    result: Optional[schema.SubCategory] = await crud.sub_category.update(sub_category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory {sub_category_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.SubCategory)
async def delete_sub_category(
        *,
        sub_category_in: schema.SubCategoryDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.SubCategory]:
    """
    delete one sub_category
    """
    result: Optional[schema.SubCategory] = await crud.sub_category.delete(sub_category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory {sub_category_in} not found"
        )
    return result