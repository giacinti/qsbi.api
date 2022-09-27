from fastapi import APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Dict

import qsbi.api.schemas.sub_category
import qsbi.crud

router = APIRouter()

## CREATE
@router.post("/", status_code=201, response_model=qsbi.api.schemas.sub_category.SubCategory)
def create_sub_category(
        *,
        sub_category_in: qsbi.api.schemas.sub_category.SubCategoryCreate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.sub_category.SubCategory:
    """
    create a new sub_category
    """
    sub_category = qsbi.crud.sub_category.create(sess, sub_category_in)
    return sub_category

## READ
@router.get("/list", status_code=200, response_model=qsbi.api.schemas.sub_category.SubCategorySeq)
def list_sub_categorys(
        *,
        skip: Optional[int] = 0,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.sub_category.SubCategorySeq:
    """
    list all sub_categorys
    """
    sub_categorys = qsbi.crud.sub_category.list(sess, skip, limit)
    return {"results": sub_categorys}

@router.post("/search", status_code=200, response_model=qsbi.api.schemas.sub_category.SubCategorySeq)
def search_sub_categorys(
        *,
        sub_category_in: qsbi.api.schemas.sub_category.SubCategoryRead,
        limit: Optional[int] = 100,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> qsbi.api.schemas.sub_category.SubCategorySeq:
    """
    search sub_categorys
    """
    sub_categorys = qsbi.crud.sub_category.search(sess, sub_category_in, limit)
    return {"results": sub_categorys}

@router.get("/id/{id}", status_code=200, response_model=qsbi.api.schemas.sub_category.SubCategory)
def get_sub_category_by_id(
        *,
        id: int,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.sub_category.SubCategory]:
    """
    get sub_category by id
    """
    result = qsbi.crud.sub_category.get_by(sess, 'id', id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory with id {id} not found"
        )
    return result
  


## UPDATE
@router.put("/", status_code=201, response_model=qsbi.api.schemas.sub_category.SubCategory)
def update_sub_category(
        *,
        sub_category_in: qsbi.api.schemas.sub_category.SubCategoryUpdate,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
        ) -> Optional[qsbi.api.schemas.sub_category.SubCategory]:
    """
    update existing sub_category
    """
    result = qsbi.crud.sub_category.update(sess, sub_category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory {sub_category_in} not found"
        )
    return result

## DELETE
@router.delete("/", status_code=200, response_model=qsbi.api.schemas.sub_category.SubCategoryDict)
def delete_sub_category(
        *,
        sub_category_in: qsbi.api.schemas.sub_category.SubCategoryDelete,
        sess: qsbi.crud.CRUDSession = Depends(qsbi.crud.get_session),
	) -> Optional[Dict]:
    """
    delete one sub_category
    """
    result = qsbi.crud.sub_category.delete(sess, sub_category_in)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"SubCategory {sub_category_in} not found"
        )
    return result
