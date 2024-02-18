from .model import DbModel, DbTable, DbCol, DbIndex, DbIndexField, DbType
from typing import NamedTuple

AUTO_INCREMENT = {"autoinc", True}
NOT_NULL = {"notnull", True}
UNIQUE = {"unique", True}


class TEXT(NamedTuple):
    size: int = 0
    name = DbType.TEXT


class INTEGER(NamedTuple):
    size: int = 8
    name = DbType.INTEGER


class BLOB:
    size: int = 0
    name = DbType.BLOB


class FLOAT:
    size = 0
    name = DbType.FLOAT


class DOUBLE:
    size = 0
    name = DbType.DOUBLE


class ANY:
    size = 0
    name = DbType.ANY


class BOOLEAN:
    size = 0
    name = DbType.BOOLEAN


class PRIMARY_KEY:
    pass


def COLUMN(name, typ, *attrs):
    kws = {}
    is_prim = False
    for attr in attrs:
        if type(attr) is dict:
            kws.update(attr)
        is_prim = type(attr) is PRIMARY_KEY

    return is_prim, DbCol(name, typ=typ.name, size=typ.size, **kws)


def FIELD(name, prefix=None):
    return DbIndexField(name, prefix_len=prefix)


def INDEX(*ents):
    kws = {}
    for attr in ents:
        if type(attr) is dict:
            kws.update(attr)
    fields = [ent for ent in ents if type(ent) is DbIndexField]
    return None, DbIndex(tuple(fields), **kws)


def TABLE(name, *ents):
    columns = [ent for _, ent in ents if type(ent) is DbCol]
    indexes = [ent for _, ent in ents if type(ent) is DbIndex]
    prim = [ent for is_prim, ent in ents if is_prim]
    if prim:
        indexes.append(DBIndex((prim[0].name,), primary=True))
    return name, DbTable(tuple(columns), tuple(indexes))


def MODEL(*tables):
    return DbModel({name: ent for name, ent in tables})


def test_model():
    model = MODEL(
        TABLE(
            "tab",
            COLUMN("foo", INTEGER, PRIMARY_KEY, AUTO_INCREMENT),
            COLUMN("bar", TEXT(20), NOT_NULL),
            INDEX(UNIQUE, FIELD("foo"), FIELD("bar")),
        ),
        TABLE(
            "othertab",
            COLUMN("bar", TEXT(20)),
            COLUMN("baz", TEXT),
            INDEX(PRIMARY_KEY, FIELD("foo"), FIELD("bar")),
        ),
    )
