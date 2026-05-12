from vector_db.VectorDB import db

db.setup_test()


def retrieve_baseline(query, top_k, decs="baseline"):
    return db.queryDB_test(query, top_k, "baseline")


def retrieve_e1(query, top_k, decs="e1"):
    return db.queryDB_test(query, top_k, "e1")


def retrieve_e2(query, top_k, decs="e2"):
    return db.queryDB_test(query, top_k, "e2")


def retrieve_e3(query, top_k, decs="e3"):
    return db.queryDB_test(query, top_k, "e3")


def retrieve_e4(query, top_k, decs="e4"):
    return db.queryDB_test(query, top_k, "e4")


def retrieve_full(query, top_k, decs="full"):
    return db.queryDB_test(query, top_k, "full")
