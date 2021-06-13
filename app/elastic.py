from elasticsearch import Elasticsearch

url = "127.0.0.1"
port = "9200"
index = "finance"
doc_type = "fluct"
es = Elasticsearch(f'{url}:{port}')

def create_index():
	if not es.indices.exists(index=index):
		return es.indices.create(index=index)

def delete_index():
	if es.indices.exists(index=index):
		return es.indices.delete(index=index)

def insert(body):
	return es.index(index=index, doc_type=doc_type, body=body)

def delete(data):
	if data is None:
		data = {"match_all": {}}
	else:
		data = {"match": data}
	body = {"query": data }
	return es.delete_by_query(index, body=body)

def delete_by_id(id):
	return es.delete(index, id=id)

def search(data=None):
	if data is None:
		data = {"match_all": {}}
	else:
		data = {"match": data}
	body = {"query": data}
	res = es.search(index=index, body=body)
	return res

def updata(id, doc):
	body = {
		'doc': doc
	}
	res = es.update(index=index, id=id, body=body, doc_type=doc_type)
	return res
