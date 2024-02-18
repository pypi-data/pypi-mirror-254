import os
import json
import shutil
import traceback
import uuid
from typing import Callable, Any

from petdb import PetDB, PetCollection, NON_EXISTENT, NonExistent, QueryException

TEST_COLLECTION_NAME = "testcol"

RED = "\033[91m"
GREEN = "\033[92m"
COLOREND = "\033[0m"

with open(__file__, "r") as f:
	testfile = f.read().splitlines()

def get_line(func: Callable):
	search = f"def {func.__name__}(col: PetCollection):"
	for i, line in enumerate(testfile, 1):
		if search in line:
			return i + 1
	return 0

class Tests:

	root: str
	db: PetDB
	col: PetCollection
	sets: list[Callable] = []
	tests: list = []

	@classmethod
	def init(cls):
		cls.root = os.path.join(os.getcwd(), "testdb")
		if os.path.exists(cls.root):
			shutil.rmtree(cls.root)
		os.mkdir(cls.root)
		cls.db = PetDB(cls.root)

	@classmethod
	def setup(cls, init: list, ignore_id: bool):
		cls.db.drop_collection(TEST_COLLECTION_NAME)
		if not ignore_id:
			for doc in init:
				if isinstance(doc, dict) and "_id" not in doc:
					doc["_id"] = str(uuid.uuid4())
		with open(os.path.join(cls.root, "petstorage", f"{TEST_COLLECTION_NAME}.json"), "w") as f:
			json.dump(init, f)
		cls.col = cls.db.collection(TEST_COLLECTION_NAME)

	@classmethod
	def run(cls, nums: int | list[int] = None):
		if isinstance(nums, int):
			nums = [nums]
		for testset in cls.sets:
			testset()
		passed = 0
		failed = []
		for i, test in enumerate(cls.tests, 1):
			try:
				if nums is not None and i not in nums:
					continue
				cls.setup(test["init"], test["ignore_id"])
				result = test["func"](cls.col)
				if not test["ignore_id"]:
					cls.remove_ids(result)
					cls.remove_ids(test["expect"])
				if result == test["expect"]:
					passed += 1
				else:
					failed.append(cls.format_failed(i, test, result))
			except Exception as e:
				if isinstance(test["expect"], type) and isinstance(e, test["expect"]):
					passed += 1
				elif isinstance(test["expect"], Exception) and e.args == test["expect"].args:
					passed += 1
				else:
					failed.append(cls.format_exception(i, test))
		shutil.rmtree(cls.root)
		return passed, failed

	@classmethod
	def format_failed(cls, number: int, test: dict, result: Any) -> str:
		return (f"{RED}Test {number} ({test["name"]}){COLOREND}: expected '{test["expect"]}', got '{result}'\n"
			f"File \"{__file__}\", line {get_line(test["func"])}")

	@classmethod
	def format_exception(cls, number: int, test: dict) -> str:
		return (f"{RED}Exception raised during Test {number} ({test["name"]}):{COLOREND}\n"
			+ traceback.format_exc().replace("\n\n", "\n"))

	@classmethod
	def remove_ids(cls, entry):
		if isinstance(entry, dict):
			entry.pop("_id", None)
		elif isinstance(entry, list) and len(entry) > 0 and isinstance(entry[0], dict):
			for doc in entry:
				doc.pop("_id", None)

def test(init=None, expect=None, ignore_id: bool = False, init_expectation: bool = True):
	if init is None and expect and init_expectation:
		if isinstance(expect, dict):
			init = [expect]
		elif isinstance(expect, list) and all(isinstance(doc, dict) for doc in expect):
			init = expect[:]
	def decorator(func):
		Tests.tests.append({
			"func": func,
			"init": init or [],
			"expect": expect,
			"ignore_id": ignore_id,
			"name": func.__name__})
	return decorator

def testset(func):
	Tests.sets.append(func)

def read_collection_file():
	with open(os.path.join(Tests.root, "petstorage", f"{TEST_COLLECTION_NAME}.json")) as f:
		return json.load(f)

# BASE

@testset
def base():

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def collection_to_list(col: PetCollection):
		return list(col)

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def iteration1(col: PetCollection):
		result = []
		for doc in col:
			result.append(doc)
		return result

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[1, 2, 3])
	def iteration2(col: PetCollection):
		result = []
		for doc in col:
			result.append(doc["a"])
		return result

# INSERT

@testset
def insertion():

	@test(expect=[{"a": 5}], init_expectation=False)
	def insert1(col: PetCollection):
		col.insert({"a": 5})
		return list(col)

	@test(expect=[{"a": 1}, {"a": 2}, {"a": 3}], init_expectation=False)
	def insert2(col: PetCollection):
		col.insert({"a": 1})
		col.insert({"a": 2})
		col.insert({"a": 3})
		return list(col)

	@test(expect=True, init_expectation=False)
	def insert3(col: PetCollection):
		doc_org = {"a": 5}
		doc_copy = col.insert(doc_org)
		doc_copy["a"] = 10
		return doc_org["a"] == 5 and col.exists({"a": 10})

	@test(expect=[{"a": 1}, {"a": 2}, {"a": 3}], init_expectation=False)
	def insert_many(col: PetCollection):
		col.insert_many([{"a": 1}, {"a": 2}, {"a": 3}])
		return list(col)

	@test(expect=[{"a": 1}, {"a": 2}, {"a": 3}], init_expectation=False)
	def insert_many(col: PetCollection):
		docs_org = [{"a": 1}, {"a": 2}, {"a": 3}]
		docs_copy = col.insert_many(docs_org)
		return list(col)

	@test(expect=True)
	def id1(col: PetCollection):
		doc1 = col.insert({"a": 1})
		doc2 = col.insert({"a": 2})
		return ("_id" in doc1 and len(doc1["_id"]) > 8
				and "_id" in doc2 and len(doc2["_id"]) > 8
				and doc1["_id"] != doc2["_id"])

	@test(expect=12345)
	def id2(col: PetCollection):
		col.insert({"a": 5, "_id": 12345})
		return col.find({"a": 5})["_id"]

	@test(expect=True)
	def id3(col: PetCollection):
		doc1, doc2 = col.insert_many([{"a": 1}, {"a": 2}])
		return ("_id" in doc1 and len(doc1["_id"]) > 8
				and "_id" in doc2 and len(doc2["_id"]) > 8
				and doc1["_id"] != doc2["_id"])

	@test(expect=12345)
	def id4(col: PetCollection):
		col.insert_many([{"a": 5, "_id": 12345}])
		return col.find({"a": 5})["_id"]

	@test(expect=[{"a": 5}], init_expectation=False)
	def insert_dump1(col: PetCollection):
		col.insert({"a": 5})
		return read_collection_file()

	@test(expect=[{"a": 5}, {"a": 5}, {"a": 5}], init_expectation=False)
	def insert_dump2(col: PetCollection):
		for i in range(3):
			col.insert({"a": 5})
		return read_collection_file()

	@test(expect=[{"a": 1}, {"a": 2}, {"a": 3}], init_expectation=False)
	def insert_many_dump(col: PetCollection):
		col.insert_many([{"a": 1}, {"a": 2}, {"a": 3}])
		return read_collection_file()

	@test(expect=QueryException("Duplicate id"))
	def insert_queryexception1(col: PetCollection):
		_id = col.insert({"a": 5})["_id"]
		return col.insert({"a": 10, "_id": _id, "b": 5})

	@test(expect=QueryException("Duplicate id"))
	def insert_many_queryexception1(col: PetCollection):
		_id = col.insert_many([{"a": 5}])[0]["_id"]
		return col.insert_many([{"a": 10, "_id": _id, "b": 5}])

	@test(expect=TypeError("Document must be of type dict"))
	def insert_typeexception(col: PetCollection):
		return col.insert(123)

	@test(expect=TypeError("Document must be of type dict"))
	def insert_many_typeexception(col: PetCollection):
		return col.insert_many([{}, 123, {}])

# UPDATING

@testset
def updating():

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set1(col: PetCollection):
		for doc in col.filter({"a": {"$lt": 3}}):
			col.update_one({"$set": {"b": 10}}, doc["_id"])
		return col.list()

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set2(col: PetCollection):
		col.update({"$set": {"b": 10}}, col.filter({"a": {"$lt": 3}}).flat("_id").list())
		return col.list()

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set3(col: PetCollection):
		col.update({"$set": {"b": 10}}, {"a": {"$lt": 3}})
		return col.list()

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set4(col: PetCollection):
		col.update({"$set": {"b": 10}}, col.filter({"a": {"$lt": 3}}).list())
		return col.list()

	@test(init=[{"a": {"b": [1, [0, 3, {}]]}}], expect=[{"a": {"b": [1, [0, 3, {"c": 5}]]}}])
	def set5(col: PetCollection):
		col.update({"$set": {"a.b.1.2.c": 5}})
		return col.list()

	@test(init=[{"a": {"b": {}}}], expect=[{"a": {"b": {"c": {"d": 5}}}}])
	def set5(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 5}})
		return col.list()

	@test(init=[{"a": {}}], expect=[{"a": {"b": {"c": {"d": 5}}}}])
	def set6(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 5}})
		return col.list()

	@test(init=[{}], expect=[{"a": {"b": {"c": {"d": 5}}}}])
	def set7(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 5}})
		return col.list()

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set_dump1(col: PetCollection):
		for doc in col.findall({"a": {"$lt": 3}}):
			col.update_one({"$set": {"b": 10}}, doc["_id"])
		return read_collection_file()

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set_dump2(col: PetCollection):
		col.update({"$set": {"b": 10}}, col.filter({"a": {"$lt": 3}}).flat("_id").list())
		return read_collection_file()

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set_dump3(col: PetCollection):
		col.update({"$set": {"b": 10}}, {"a": {"$lt": 3}})
		return read_collection_file()

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def set_dump4(col: PetCollection):
		col.update({"$set": {"b": 10}}, col.filter({"a": {"$lt": 3}}).list())
		return read_collection_file()

	@test(init=[{"a": {"b": []}}], expect=QueryException("Invalid set query: path a.b.c.d doesn't exist"))
	def set_queryexception1(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 5}})
		return col.list()

	@test(init=[{"a": {"b": 0}}], expect=QueryException("Invalid set query: path a.b.c.d doesn't exist"))
	def set_queryexception2(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 5}})
		return col.list()

	@test(init=[{"a": {"b": None}}], expect=QueryException("Invalid set query: path a.b.c.d doesn't exist"))
	def set_queryexception3(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 5}})
		return col.list()

	@test(init=[{"a": {"b": {"c": None}}}], expect=QueryException("Invalid set query: path a.b.c.d doesn't exist"))
	def set_queryexception4(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 5}})
		return col.list()

	@test(init=[{"a": {"b": []}}], expect=QueryException("Invalid set query: list index must contains only digits"))
	def set_queryexception5(col: PetCollection):
		col.update({"$set": {"a.b.c": 5}})

	@test(init=[{"a": {"b": []}}], expect=QueryException("Invalid set query: list index out of range"))
	def set_queryexception6(col: PetCollection):
		col.update({"$set": {"a.b.1": 5}})

	@test(init=[{"a": 0}], expect=QueryException("Invalid query format: query list should contains only ids or only docs"))
	def set_queryexception7(col: PetCollection):
		col.update({"$set": {"a.b.c.d": 0}}, ["12345", "67890", {"a": 0}])

	@test(init=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset1(col: PetCollection):
		col.update({"$unset": {"b": True}})
		return col.list()

	@test(init=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset2(col: PetCollection):
		col.update({"$unset": {"b": True}}, {"b": 10})
		return col.list()

	@test(init=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset3(col: PetCollection):
		col.update({"$unset": {"b": True}}, {"b": {"$exists": True}})
		return col.list()

	@test(expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def unset4(col: PetCollection):
		col.update({"$unset": {"b": True}}, {"b": {"$exists": False}})
		return col.list()

	@test(init=[{"a": 1, "b": 10, "c": 4}, {"a": 2, "b": 10}, {"a": 3, "c": 4}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset5(col: PetCollection):
		col.update({"$unset": {"b": True, "c": True}})
		return col.list()

	@test(init=[{"a": 1, "b": 10, "c": 4}, {"a": 2, "b": 10}, {"a": 3, "c": 4}],
		expect=[{"a": 1, "c": 4}, {"a": 2}, {"a": 3, "c": 4}])
	def unset6(col: PetCollection):
		col.update({"$unset": {"b": True, "c": False}})
		return col.list()

	@test(init=[{"a": 1, "b": 10, "c": 4}, {"a": 2, "b": 10}, {"a": 3, "c": 4}],
		expect=[{"a": 1, "c": 4}, {"a": 2}, {"a": 3, "c": 4}])
	def unset7(col: PetCollection):
		col.update({"$unset": {"b": True}})
		return col.list()

	@test(init=[{"a": {"b": [1, [0, 3, {"c": 5}]]}}], expect=[{"a": {"b": [1, [0, 3, {}]]}}])
	def unset8(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return col.list()

	@test(expect=[{"a": {"b": [1, [0, 3, {}]]}}])
	def unset9(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return col.list()

	@test(expect=[{"a": {"b": [1, [0, 3]]}}])
	def unset10(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return col.list()

	@test(expect=[{"a": {"b": None}}])
	def unset11(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return col.list()

	@test(expect=[{}])
	def unset12(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return col.list()

	@test(init=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset_dump1(col: PetCollection):
		col.update({"$unset": {"b": True}})
		return read_collection_file()

	@test(init=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset_dump2(col: PetCollection):
		col.update({"$unset": {"b": True}}, {"b": 10})
		return read_collection_file()

	@test(init=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset_dump3(col: PetCollection):
		col.update({"$unset": {"b": True}}, {"b": {"$exists": True}})
		return read_collection_file()

	@test(expect=[{"a": 1, "b": 10}, {"a": 2, "b": 10}, {"a": 3}])
	def unset_dump4(col: PetCollection):
		col.update({"$unset": {"b": True}}, {"b": {"$exists": False}})
		return read_collection_file()

	@test(init=[{"a": 1, "b": 10, "c": 4}, {"a": 2, "b": 10}, {"a": 3, "c": 4}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def unset_dump5(col: PetCollection):
		col.update({"$unset": {"b": True, "c": True}})
		return read_collection_file()

	@test(init=[{"a": 1, "b": 10, "c": 4}, {"a": 2, "b": 10}, {"a": 3, "c": 4}],
		expect=[{"a": 1, "c": 4}, {"a": 2}, {"a": 3, "c": 4}])
	def unset_dump6(col: PetCollection):
		col.update({"$unset": {"b": True, "c": False}})
		return read_collection_file()

	@test(init=[{"a": 1, "b": 10, "c": 4}, {"a": 2, "b": 10}, {"a": 3, "c": 4}],
		expect=[{"a": 1, "c": 4}, {"a": 2}, {"a": 3, "c": 4}])
	def unset_dump7(col: PetCollection):
		col.update({"$unset": {"b": True}})
		return read_collection_file()

	@test(init=[{"a": {"b": [1, [0, 3, {"c": 5}]]}}], expect=[{"a": {"b": [1, [0, 3, {}]]}}])
	def unset_dump8(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return read_collection_file()

	@test(expect=[{"a": {"b": [1, [0, 3, {}]]}}])
	def unset_dump9(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return read_collection_file()

	@test(expect=[{"a": {"b": [1, [0, 3]]}}])
	def unset_dump10(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return read_collection_file()

	@test(expect=[{"a": {"b": None}}])
	def unset_dump11(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return read_collection_file()

	@test(expect=[{}])
	def unset_dump12(col: PetCollection):
		col.update({"$unset": {"a.b.1.2.c": True}})
		return read_collection_file()

	@test(init=[{"a": [1, 2]}, {"a": [1, 2, 3, 4]}], expect=[{"a": [1, 2, 123]}, {"a": [1, 2, 3, 4, 123]}])
	def append1(col: PetCollection):
		col.update({"$append": {"a": 123}}, {})
		return col.list()

	@test(init=[[0, [1, 2, 3]], [0, [4, 5, 6]]], expect=[[0, [1, 2, 3, 222]], [0, [4, 5, 6, 222]]])
	def append2(col: PetCollection):
		col.update({"$append": {1: 222}})
		return col.list()

	@test(init=[{"a": [1, {"b": [1, 2]}]}, {"a": [4, {"b": []}]}],
		expect=[{"a": [1, {"b": [1, 2, {"c": 5}]}]}, {"a": [4, {"b": [{"c": 5}]}]}])
	def append3(col: PetCollection):
		col.update({"$append": {"a.1.b": {"c": 5}}})
		return col.list()

	@test(init=[{"a": [1, 2]}, {"a": [1, 2, 3, 4]}], expect=[{"a": [1, 2, 123]}, {"a": [1, 2, 3, 4, 123]}])
	def append_dump1(col: PetCollection):
		col.update({"$append": {"a": 123}}, {})
		return read_collection_file()

	@test(init=[[0, [1, 2, 3]], [0, [4, 5, 6]]], expect=[[0, [1, 2, 3, 222]], [0, [4, 5, 6, 222]]])
	def append_dump2(col: PetCollection):
		col.update({"$append": {1: 222}})
		return read_collection_file()

	@test(init=[{"a": [1, {"b": [1, 2]}]}, {"a": [4, {"b": []}]}],
		expect=[{"a": [1, {"b": [1, 2, {"c": 5}]}]}, {"a": [4, {"b": [{"c": 5}]}]}])
	def append_dump3(col: PetCollection):
		col.update({"$append": {"a.1.b": {"c": 5}}})
		return read_collection_file()

	@test(init=[{"a": 5}], expect=QueryException("Invalid append query: only lists supports integer keys"))
	def append_queryexception1(col: PetCollection):
		col.update({"$append": {1: "item"}})

	@test(init=[[0, [1, 2, 3]], [0, [4, 5, 6]]], expect=QueryException("Invalid append query: index out of range"))
	def append_queryexception2(col: PetCollection):
		col.update({"$append": {2: 222}})

	@test(init=[[0, {}], [0, {}]], expect=QueryException("Invalid append query: it's impossible to append not to a list"))
	def append_queryexception3(col: PetCollection):
		col.update({"$append": {1: 222}})

	@test(init=[[0, "123"], [0, "123"]],
		expect=QueryException("Invalid append query: it's impossible to append not to a list"))
	def append_queryexception4(col: PetCollection):
		col.update({"$append": {1: 222}})

	@test(init=[{"a": {}}], expect=QueryException("Invalid append query: path a.b doesn't exist"))
	def append_queryexception5(col: PetCollection):
		col.update({"$append": {"a.b": 5}})

	@test(init=[{}], expect=QueryException("Invalid append query: path a.b doesn't exist"))
	def append_queryexception6(col: PetCollection):
		col.update({"$append": {"a.b": 5}})

	@test(init=[{"a": {"b": {}}}],
		expect=QueryException(f"Invalid append query: it's impossible to append not to a list"))
	def append_queryexception7(col: PetCollection):
		col.update({"$append": {"a.b": 5}})

	@test(init=[{"a": {"b": 5}}],
		expect=QueryException(f"Invalid append query: it's impossible to append not to a list"))
	def append_queryexception8(col: PetCollection):
		col.update({"$append": {"a.b": 5}})

	@test(init=[{"a": {"b": None}}],
		expect=QueryException(f"Invalid append query: it's impossible to append not to a list"))
	def append_queryexception9(col: PetCollection):
		col.update({"$append": {"a.b": 5}})

# SELECTION

@testset
def selection():

	@test(expect={"a": 1}, init_expectation=False)
	def get_by_id1(col: PetCollection):
		doc_id = col.insert({"a": 1})["_id"]
		return col.get(doc_id)

	@test(expect=None)
	def get_by_id2(col: PetCollection):
		return col.get("12345")

	@test(expect={"a": 5, "b": 10})
	def find1(col: PetCollection):
		return col.find({"a": 5})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def find2(col: PetCollection):
		return col.find({"a": 10})

	@test(expect={"a": 5, "b": 10, "c": 20})
	def find3(col: PetCollection):
		return col.find({"a": 5, "c": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def find4(col: PetCollection):
		return col.find({"a": 5, "c.d": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def find5(col: PetCollection):
		return col.find({"a": 5, "c": {"d": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def find6(col: PetCollection):
		return col.find({"a": 5, "c": {"d.e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def find6(col: PetCollection):
		return col.find({"a": 5, "c.d": {"e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def find6(col: PetCollection):
		return col.find({"a": 5, "c": {"d": {"e": 20}}})

	@test(expect=[{"a": 5, "b": 1, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall1(col: PetCollection):
		return col.findall({})

	@test(expect=[{"a": 5, "b": 1, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall2(col: PetCollection):
		return list(col.findall({}))

	@test(init=[{"a": 5, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}], expect=[{"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall3(col: PetCollection):
		return col.findall({"b": 1})

	@test(init=[{"a": 5, "b": 2, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}], expect=[{"a": 6, "b": 1}, {"a": 7, "b": 1}])
	def findall4(col: PetCollection):
		return col.findall({"b": 1})

	@test(init=[{"a": 5, "b": 2, "c": 3}, {"a": 6, "b": 1}, {"a": 7, "b": 1}], expect=[])
	def findall5(col: PetCollection):
		return col.findall({"b": 3})

	@test(init=[{"a": [{}, {"b": 1}]}, {"a": [{}, {"b": 2}]}, {"a": [{}, {"b": 3}]}, {"a": []}],
		expect=[{"a": [{}, {"b": 1}]}, {"a": [{}, {"b": 2}]}])
	def findall6(col: PetCollection):
		return col.filter({"a.1.b": {"$exists": True}}).findall({"a.1.b": {"$lt": 3}})

# OPERATORS

@testset
def operators():

	@test(init=[{"a": {"b": 5}}, {"a": 10}],
		expect=QueryException("Invalid query: all keys into operators query must start with $"))
	def operators_queryexception1(col: PetCollection):
		return col.findall({"a": {"b": 5, "$lt": 4}})

	@test(expect={"a": 5, "b": 10})
	def eq1(col: PetCollection):
		return col.find({"a": {"$eq": 5}})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def eq2(col: PetCollection):
		return col.find({"a": {"$eq": 50}})

	@test(expect={"a": 5, "b": 10})
	def not1(col: PetCollection):
		return col.find({"a": {"$not": 1}})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def not2(col: PetCollection):
		return col.find({"a": {"$not": 5}})

	@test(expect={"a": 5, "b": 10})
	def ne1(col: PetCollection):
		return col.find({"a": {"$ne": 1}})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def ne2(col: PetCollection):
		return col.find({"a": {"$ne": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 1, "b": 0}])
	def lt(col: PetCollection):
		return col.findall({"a": {"$lt": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}, {"a": 1, "b": 0}])
	def lte(col: PetCollection):
		return col.findall({"a": {"$lte": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}])
	def gt(col: PetCollection):
		return col.findall({"a": {"$gt": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}, {"a": 10, "b": 5}])
	def gte(col: PetCollection):
		return col.findall({"a": {"$gte": 5}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}])
	def gt_an_lt(col: PetCollection):
		return col.findall({"a": {"$gt": 3, "$lt": 7}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 5, "b": 10}])
	def in1(col: PetCollection):
		return col.findall({"a": {"$in": [4, 5, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[])
	def in2(col: PetCollection):
		return col.findall({"a": {"$in": [4, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}])
	def nin1(col: PetCollection):
		return col.findall({"a": {"$nin": [1, 4, 5, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[])
	def nin2(col: PetCollection):
		return col.findall({"a": {"$nin": [1, 4, 5, 6, 10]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[{"a": 10, "b": 5}])
	def notin1(col: PetCollection):
		return col.findall({"a": {"$notin": [1, 4, 5, 6]}})

	@test(init=[{"a": 5, "b": 10}, {"a": 10, "b": 5}, {"a": 1, "b": 0}], expect=[])
	def notin2(col: PetCollection):
		return col.findall({"a": {"$notin": [1, 4, 5, 6, 10]}})

	@test(expect=[{"a": 5}])
	def exists1(col: PetCollection):
		return col.findall({"a": {"$exists": True}})

	@test(init=[{"a": 5}], expect=[])
	def exists2(col: PetCollection):
		return col.findall({"b": {"$exists": True}})

	@test(init=[{"a": 5}, {"a": 6}, {"b": 10}], expect=[{"a": 5}, {"a": 6}])
	def exists3(col: PetCollection):
		return col.findall({"a": {"$exists": True}})

	@test(init=[{"a": 5}, {"a": 6}, {"b": 10}], expect=[{"b": 10}])
	def exists4(col: PetCollection):
		return col.findall({"a": {"$exists": False}})

	@test(expect=[{"a": 5}, {"a": 6}, {"b": 10}])
	def exists5(col: PetCollection):
		return col.findall({"a.b": {"$exists": False}})

	@test(init=[{"a": 5}, {"a": 6}, {"b": 10}], expect=[])
	def exists6(col: PetCollection):
		return col.findall({"a.b": {"$exists": True}})

	@test(expect=[{"a": "12345"}, {"a": "67890"}])
	def regex1(col: PetCollection):
		return col.findall({"a": {"$regex": "\\d{5}"}})

	@test(init=[{"a": "12345"}, {"a": "67890"}], expect=[])
	def regex2(col: PetCollection):
		return col.findall({"a": {"$regex": "\\D{5}"}})

	@test(init=[{"a": "12345"}, {"a": "678901"}], expect=[{"a": "12345"}])
	def regex3(col: PetCollection):
		return col.findall({"a": {"$regex": "^1"}})

	@test(init=[{"a": "12345"}, {"a": "678901"}], expect=[{"a": "12345"}])
	def regex4(col: PetCollection):
		return col.findall({"a": {"$regex": "5$"}})

	@test(init=[{"a": "12345"}, {"a": "abcde"}], expect=[{"a": "12345"}])
	def func1(col: PetCollection):
		return col.findall({"a": {"$func": str.isdigit}})

	@test(init=[{"a": "12345"}, {"a": "abcde"}, {"a": 12345}], expect=TypeError)
	def func2(col: PetCollection):
		return col.findall({"a": {"$func": str.isdigit}})

	@test(init=[{"a": "12345"}, {"a": "abcde"}], expect=[{"a": "12345"}])
	def func3(col: PetCollection):
		return col.findall({"a": {"$func": str.isdigit}})

	@test(init=[{"a": "12345"}, {"a": "abcde"}, {"a": 12345}], expect=[{"a": "12345"}, {"a": "abcde"}])
	def type1(col: PetCollection):
		return col.findall({"a": {"$type": str}})

	@test(expect=[{"a": "12345"}, {"a": "abcde"}, {"a": 12345}])
	def type2(col: PetCollection):
		return col.findall({"b": {"$type": NonExistent}})

# LOGICAL OPERATORS

@testset
def logical_operators():

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}], expect=[{"a": 1}, {"a": 3}])
	def or1(col: PetCollection):
		return col.findall({"$or": [{"a": 1}, {"a": 3}]})

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}], expect=[{"a": 1}, {"a": 3}])
	def or2(col: PetCollection):
		return col.findall({"a": {"$or": [1, 3]}})

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}], expect=[{"a": 1}, {"a": 3}])
	def or3(col: PetCollection):
		return col.findall({"a": {"$or": [{"$lt": 2}, {"$eq": 3}]}})

	@test(init=[{"a": {"b": 1}}, {"a": {"b": 7}}, {"a": {"b": 10}}], expect=[{"a": {"b": 1}}, {"a": {"b": 10}}])
	def or4(col: PetCollection):
		return col.findall({"$or": [{"a.b": 1}, {"a.b": 10}]})

	@test(init=[{"a": {"b": 1}}, {"a": {"b": 7}}, {"a": {"b": 10}}], expect=[{"a": {"b": 1}}, {"a": {"b": 10}}])
	def or5(col: PetCollection):
		return col.findall({"$or": [{"a.b": {"$lt": 5}}, {"a.b": {"$gte": 10}}]})

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}], expect=[{"a": 2}])
	def and1(col: PetCollection):
		return col.findall({"$and": [{"a": {"$gt": 1}}, {"a": {"$lt": 3}}]})

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}, {"b": 2}], expect=[{"a": 2}])
	def and2(col: PetCollection):
		return col.findall({"a": {"$and": [{"$exists": True}, {"$gt": 1}, {"$lt": 3}]}})

# DELETION

@testset
def deletion():

	@test(init=[{"a": 5}, {"b": 2}, {"b": 3}], expect=[])
	def remove_clear_dump1(col: PetCollection):
		col.remove({})
		return read_collection_file()

	@test(expect=[], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_clear_dump2(col: PetCollection):
		col.remove({})
		return read_collection_file()

	@test(init=[{"a": 5}, {"b": 2}, {"b": 3}], expect=[])
	def remove_clear1(col: PetCollection):
		col.remove({})
		return col.list()

	@test(expect=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_clear2(col: PetCollection):
		return col.remove({})

	@test(expect=[], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_clear3(col: PetCollection):
		col.remove({})
		return col.list()

	@test(expect=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_clear4(col: PetCollection):
		return col.remove({})

	@test(expect=[{"a": 5}, {"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove1(col: PetCollection):
		col.remove({"b": 3})
		return col.list()

	@test(expect=[{"a": 5}, {"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_dump1(col: PetCollection):
		col.remove({"b": 3})
		return read_collection_file()

	@test(expect=[{"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove2(col: PetCollection):
		return col.remove({"b": 2})

	@test(expect=[{"a": 5}, {"b": 3}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove3(col: PetCollection):
		col.remove(col.flat("_id")[1])
		return col.list()

	@test(expect=[{"a": 5}, {"b": 3}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_dump2(col: PetCollection):
		col.remove(col.flat("_id")[1])
		return read_collection_file()

	@test(expect=[{"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove4(col: PetCollection):
		return col.remove(col.flat("_id")[1])

	@test(expect=[{"a": 5}, {"b": 3}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove5(col: PetCollection):
		col.remove([col.flat("_id")[1]])
		return col.list()

	@test(expect=[{"a": 5}, {"b": 3}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_dump3(col: PetCollection):
		col.remove([col.flat("_id")[1]])
		return read_collection_file()

	@test(expect=[{"b": 2}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove6(col: PetCollection):
		return col.remove([col.flat("_id")[1]])

	@test(expect=[{"a": 5}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove7(col: PetCollection):
		col.remove(col[1:])
		return col.list()

	@test(expect=[{"a": 5}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove_dump4(col: PetCollection):
		col.remove(col[1:])
		return read_collection_file()

	@test(expect=[{"b": 2}, {"b": 3}], init=[{"a": 5}, {"b": 2}, {"b": 3}])
	def remove8(col: PetCollection):
		return col.remove(col[1:])

	@test(init=[{"a": 5}], expect=QueryException("Invalid delete query"))
	def remove_queryexception1(col: PetCollection):
		return col.remove(1)

	@test(init=[{"a": 5}], expect=QueryException("Invalid delete query: it can only be a list of IDs or a list of docs"))
	def remove_queryexception1(col: PetCollection):
		return col.remove(["abcd", "abcde", {"a": 5}])

# SORTING

@testset
def sorting():

	@test(init=[{"a": 5}, {"a": 4}, {"a": 8}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[{"a": 1}, {"a": 2}, {"a": 4}, {"a": 5}, {"a": 8}, {"a": 10}])
	def sort1(col: PetCollection):
		return col.sort("a").list()

	@test(init=[{"a": 5}, {"a": 4}, {"a": 8}, {"b": 0}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[{"a": 1}, {"a": 2}, {"a": 4}, {"a": 5}, {"a": 8}, {"a": 10}, {"b": 0}])
	def sort2(col: PetCollection):
		return col.sort("a").list()

	@test(init=[{"a": "5"}, {"a": 4}, {"a": "8"}, {"b": 0}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[{'a': 1}, {'a': 2}, {'a': 4}, {'a': 10}])
	def sort3(col: PetCollection):
		return col.filter({"a": {"$type": int}}).sort("a").list()

	@test(init=[{"a": "5"}, {"a": 4}, {"a": "8"}, {"b": 0}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[{'a': 10}, {'a': 4}, {'a': 2}, {'a': 1}])
	def sort4(col: PetCollection):
		return col.filter({"a": {"$type": int}}).sort("a", reverse=True).list()

	@test(init=[{"a": 5}, {"a": 4}, {"a": 8}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[[1], [2], [4], [5], [8], [10]])
	def sort5(col: PetCollection):
		return col.map(lambda doc: [doc["a"]]).sort(0).list()

	@test(init=[{"a": 5}, {"a": 4}, {"a": 8}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[[1], [2], [4], [5], [8], [10]])
	def sort6(col: PetCollection):
		return col.map(lambda doc: [doc["a"]]).sort("0").list()

	@test(init=[{"a": 5}, {"a": 4}, {"a": 8}, {"b": 0}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[[1], [2], [4], [5], [8], [10], [None]])
	def sort7(col: PetCollection):
		return col.map(lambda doc: [doc.get("a", None)]).sort(lambda i: (i[0] is None, i[0])).list()

	@test(init=[{"a": 5}, {"a": 4}, {"a": 8}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[[[0, 1]], [[0, 2]], [[0, 4]], [[0, 5]], [[0, 8]], [[0, 10]]])
	def sort8(col: PetCollection):
		return col.map(lambda doc: [[0, doc.get("a", None)]]).sort("0.1").list()

	@test(init=[{"a": 5}, {"a": 4}, {"a": 8}, {"b": 0}, {"a": 10}, {"a": 2}, {"a": 1}],
		expect=[1, 2, 4, 5, 8, 10, NON_EXISTENT])
	def sort9(col: PetCollection):
		return col.map(lambda doc: doc.get("a", NON_EXISTENT)).sort().list()

	@test(init=[{"a": 5, "b": 5}, {"a": 5, "b": 3}, {"a": 4, "b": 4}],
		expect=[{"a": 4, "b": 4}, {"a": 5, "b": 3}, {"a": 5, "b": 5}])
	def sort10(col: PetCollection):
		return col.sort(("a", "b")).list()

# MAPPING AND MUTABLE MAPPING

@testset
def mapping():

	@test(init=[{"a": 5}, {"a": 10}], expect=[5, 10])
	def map1(col: PetCollection):
		return col.map(lambda doc: doc["a"]).list()

	@test(init=[{"a": 5}, {"b": 1}, {"a": 10}], expect=[25, 0, 100])
	def map2(col: PetCollection):
		return col.map(lambda doc: doc.get("a", 0) ** 2).list()

	@test(init=[{"a": 5}, {"b": 1}, {"a": 10}], expect=[100, 25, 0])
	def map3(col: PetCollection):
		return col.map(lambda doc: doc.get("a", 0) ** 2).sort(reverse=True).list()

	@test(expect=[5, 6, 7, 8, 9])
	def map4(col: PetCollection):
		for i in range(10):
			col.insert({"a": i})
		return col.filter({"a": {"$gte": 5}}).map(lambda doc: doc["a"]).list()

# SIZE AND MUTABLE SIZE

@testset
def size():

	@test(expect=100)
	def size1(col: PetCollection):
		for i in range(100):
			col.insert({"a": i})
		return col.size()

	@test(expect=50)
	def size2(col: PetCollection):
		for i in range(100):
			col.insert({"a": i})
		return col.filter({"a": {"$lt": 50}}).size()

	@test(expect=0)
	def size3(col: PetCollection):
		return col.size()

	@test(expect=0)
	def size4(col: PetCollection):
		return col.filter({"a": {"$lt": 50}}).size()

# FLATTING

@testset
def flatting():

	@test(init=[{"a": 5}, {"a": 6}, {"b": 1}, {"a": 2}], expect=[5, 6, 2])
	def flat1(col: PetCollection):
		return col.flat("a").list()

	@test(init=[{"a": {"b": 5}}, {"a": {"b": 6}}, {"a": {"b": 2}}], expect=[5, 6, 2])
	def flat2(col: PetCollection):
		return col.flat("a.b").list()

	@test(init=[{"a": {"b": 5}}, {"a": {"b": 6}}, {"a": {"b": 2}}], expect=[5, 6, 2])
	def flat3(col: PetCollection):
		return col.flat("a").flat("b").list()

	@test(init=[{"a": [0, {"b": 5}]}, {"a": [0, {"b": 6}]}, {"a": [0, {"b": 2}]}], expect=[5, 6, 2])
	def flat4(col: PetCollection):
		return col.flat("a.1.b").list()

	@test(init=[{"a": [0, {"b": 5}]}, {"a": [0, {"b": 6}]}, {"a": [0, {"b": 2}]}], expect=[5, 6, 2])
	def flat5(col: PetCollection):
		return col.flat("a").flat("1.b").list()

	@test(init=[{"a": [0, {"b": 5}]}, {"a": [0, {"b": 6}]}, {"a": [0, {"b": 2}]}], expect=[5, 6, 2])
	def flat6(col: PetCollection):
		return col.flat("a.1").flat("b").list()

	@test(init=[{"a": [0, {"b": 5}]}, {"a": [0, {"b": 6}]}, {"a": [0, {"b": 2}]}], expect=[5, 6, 2])
	def flat7(col: PetCollection):
		return col.flat("a").flat(1).flat("b").list()

	@test(init=[{"a": [0, {"b": 5}]}, {"a": [0, {"b": 6}]}, {"a": [0, {"b": 2}]}], expect=[5, 6, 2])
	def flat8(col: PetCollection):
		return col.flat("a").flat("1").flat("b").list()

# MUTABLE BASE

@testset
def mutable_base():

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def collection_to_list(col: PetCollection):
		return list(col.filter({}))

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[{"a": 1}, {"a": 2}, {"a": 3}])
	def iteration1(col: PetCollection):
		result = []
		for doc in col.filter({}):
			result.append(doc)
		return result

	@test(init=[{"a": 1}, {"a": 2}, {"a": 3}], expect=[1, 2, 3])
	def iteration2(col: PetCollection):
		result = []
		for doc in col.filter({}):
			result.append(doc["a"])
		return result

# MUTABLE DELETION

@testset
def mutable_deletion():

	@test(init=[{"a": 5, "c": 10}, {"a": 5, "c": 1}, {"a": 1, "c": 10}, {"a": 55, "c": 1}],
		expect=[{"a": 5, "c": 10}, {"a": 5, "c": 1}])
	def mutable_remove1(col: PetCollection):
		return col.filter({"a": 5}).remove({})

	@test(init=[{"a": 5, "c": 10}, {"a": 5, "c": 1}, {"a": 1, "c": 10}, {"a": 55, "c": 1}],
		expect=[{"a": 1, "c": 10}, {"a": 55, "c": 1}])
	def mutable_remove2(col: PetCollection):
		col.filter({"a": 5}).remove({})
		return col.list()

# MUTABLE SELECTION

@testset
def mutable_selection():

	@test(init=[{"a": 2}, {"a": 3}], expect={"a": 1})
	def mutable_get_by_id1(col: PetCollection):
		doc_id = col.insert({"a": 1})["_id"]
		return col.filter({}).get(doc_id)

	@test(expect=None)
	def mutable_get_by_id2(col: PetCollection):
		return col.filter({}).get("12345")

	@test(expect={"a": 5, "b": 10})
	def mutable_find1(col: PetCollection):
		return col.filter({}).find({"a": 5})

	@test(init=[{"a": 5, "b": 10}], expect=None)
	def mutable_find2(col: PetCollection):
		return col.filter({}).find({"a": 10})

	@test(expect={"a": 5, "b": 10, "c": 20})
	def mutable_find3(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def mutable_find4(col: PetCollection):
		return col.filter({}).find({"a": 5, "c.d": 20})

	@test(expect={"a": 5, "b": 10, "c": {"d": 20}})
	def mutable_find5(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": {"d": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def mutable_find6(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": {"d.e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def mutable_find6(col: PetCollection):
		return col.filter({}).find({"a": 5, "c.d": {"e": 20}})

	@test(expect={"a": 5, "b": 10, "c": {"d": {"e": 20}}})
	def mutable_find6(col: PetCollection):
		return col.filter({}).find({"a": 5, "c": {"d": {"e": 20}}})

if __name__ == '__main__':
	print("Running tests...\n")
	Tests.init()
	passed, failed = Tests.run()
	if len(failed) == 0:
		print(f"{GREEN}All tests passed ({passed}){COLOREND}")
	else:
		print("\n".join(failed) + "\n")
		print(f"{RED}Tests failed ({len(failed)}/{len(failed) + passed}){COLOREND}")
