from typing import List, Optional
from fastapi.encoders import jsonable_encoder

from app.models.db.rule import Rule as DBRule
from app.models.rule import Rule, RuleIn
import datetime
# from app.db.session import database
# import sqlalchemy


def get(db_session, *, rule_id: int) -> Optional[Rule]:
    return db_session.query(DBRule).filter(DBRule.id == rule_id).first()


def get_by_model(db_session, *, rule: RuleIn) -> Optional[Rule]:
    return db_session.query(DBRule).filter_by(**rule.dict()).first()


def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Rule]]:
    # query = DBRule.select()
    # results = await database.fetch_all(query)
    # return results
    return db_session.query(DBRule).offset(skip).limit(limit).all()


def create(db_session, *, rule_in: RuleIn) -> Rule:
    rule = DBRule(**rule_in.dict())
    db_session.add(rule)
    db_session.commit()
    db_session.refresh(rule)
    return rule


def update(db_session, *, rule: DBRule, rule_in: RuleIn) -> Rule:
    rule_data = jsonable_encoder(rule)
    for field in rule_data:
        if field in rule_in.fields:
            value_in = getattr(rule_in, field)
            if value_in is not None:
                setattr(rule, field, value_in)
    rule.updated_at = str(datetime.datetime.now())
    db_session.add(rule)
    db_session.commit()
    db_session.refresh(rule)
    return rule


def delete(db_session, *, rule_id: int) -> bool:
    rule = get(db_session, rule_id=rule_id)
    if rule:
        db_session.delete(rule)
        db_session.commit()
        return True
    return False
