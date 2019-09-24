from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.rule import Rule, RuleIn
from app.api.utils.security import check_token
from app.crud.rule import get, get_multi, create, delete, update, get_by_model
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
)

Tags = ["rule"]

router = APIRouter()


@router.get("/{rule_id}", tags=Tags, response_model=Rule)
def read_rule(
    rule_id: int, db: Session = Depends(get_db), authorized: bool = Depends(check_token)
):
    if authorized:
        rule = get(db, rule_id=rule_id)
        if not rule:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="The rule does not exist."
            )
        return rule


@router.get("/", tags=Tags, response_model=List[Rule])
def read_rules(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve rules
    """
    if authorized:
        rules = get_multi(db, skip=skip, limit=limit)
        return rules


@router.post("/", tags=Tags, response_model=List[Rule])
def create_rule(
    *,
    db: Session = Depends(get_db),
    rules_in: List[RuleIn],
    authorized: bool = Depends(check_token)
):
    """
    Create new rule
    """
    if authorized:
        rules_out = []
        for rule_in in rules_in:
            rule = get_by_model(db, rule=rule_in)
            if rule:
                raise HTTPException(
                    status_code=HTTP_409_CONFLICT, detail="The rule already exists."
                )
            rule = create(db, rule_in=rule_in)
            rules_out.append(rule)
        return rules_out


@router.put("/{rule_id}", tags=Tags, response_model=Rule)
def update_rule(
    *,
    db: Session = Depends(get_db),
    rule_id: int,
    rule_in: RuleIn,
    authorized: bool = Depends(check_token)
):
    """
    Update a rule
    """
    if authorized:
        rule = get(db, rule_id=rule_id)

        if not rule:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Rule does not exist")
        rule = update(db, rule=rule, rule_in=rule_in)
        return rule


@router.delete("/{rule_id}", tags=Tags, response_model=bool)
def delete_rule(
    rule_id: int, db: Session = Depends(get_db), authorized: bool = Depends(check_token)
):
    """
    delete rule
    """
    if authorized:
        rule = get(db, rule_id=rule_id)
        if not rule:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="The rule does not exist.")
        if delete(db, rule_id=rule_id):
            return True
        return False
