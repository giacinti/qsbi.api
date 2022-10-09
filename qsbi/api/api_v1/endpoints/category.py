from fastapi import APIRouter, Query, HTTPException, Request, Depends, Security
from typing import Optional, List

import qsbi.api.schemas.base
import qsbi.api.schemas.category as schema
import qsbi.api.crud as crud
import qsbi.api.security.deps as auth

router = APIRouter()

## CREATE
@router.post("", status_code=201, response_model=schema.Category)
async def create_category(
        *,
        category_in: schema.CategoryCreate,
        curr_user = Security(auth.get_current_active_user, scopes=["create"]),
        ) -> schema.Category:
    """
    create a new category
    """
    category: schema.Category  = await crud.category.create(category_in)
    return category

## READ
@router.get("/list", status_code=200, response_model=List[schema.Category])
async def list_categorys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Category]:
    """
    list all categorys
    """
    categorys: List[schema.Category] = await crud.category.list(skip, limit)
    return categorys

@router.post("/search", status_code=200, response_model=List[schema.Category])
async def search_categorys(
        *,
        category_in: schema.Category,
        limit: Optional[int] = 100,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> List[schema.Category]:
    """
    search categorys
    """
    categorys: List[schema.Category] = await crud.category.search(category_in, limit)
    return categorys

@router.get("/id/{id}", status_code=200, response_model=schema.Category)
async def get_category_by_id(
        *,
        id: int,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Category]:
    """
    get category by id
    """
    result: Optional[schema.Category] = await crud.category.get_by('id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with id {id} not found"
        )
    return result
  
@router.get("/name/{name}", status_code=200, response_model=schema.Category)
async def get_category_by_name(
        *,
        name: str,
        curr_user = Security(auth.get_current_active_user, scopes=["read"]),
        ) -> Optional[schema.Category]:
    """
    get category by name
    """
    result: Optional[schema.Category] = await crud.category.get_by('name', name)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category with name {name} not found"
        )
    return result
  
@router.get("/count", status_code=200, response_model=int)
async def count_categorys(
        *,
        curr_user = Security(auth.get_current_active_user, scopes=["login"]),
        ) -> int:
    """
    count all categorys
    """
    count: int = await crud.category.count()
    return count

## UPDATE
@router.put("", status_code=201, response_model=schema.Category)
async def update_category(
        *,
        category_in: schema.CategoryUpdate,
        curr_user = Security(auth.get_current_active_user, scopes=["update"]),
        ) -> Optional[schema.Category]:
    """
    update existing category
    """
    result: Optional[schema.Category] = await crud.category.update(category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result

## DELETE
@router.delete("", status_code=200, response_model=schema.Category)
async def delete_category(
        *,
        category_in: schema.CategoryDelete,
        curr_user = Security(auth.get_current_active_user, scopes=["delete"]),
	) -> Optional[schema.Category]:
    """
    delete one category
    """
    result: Optional[schema.Category] = await crud.category.delete(category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Category {category_in} not found"
        )
    return result