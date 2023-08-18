

### Restore Database

### run airflow/scheduler
`docker-compose up airflow-init` \
`docker-compose up`

#### to trigger DAG
`Open localhost:8080 on the browser` \
`user airflow` `pass airflow`

### run rest api
`pip install -r requirements.txt` \
`python main.py`

#### to test API
`localhost:8080/predict` \
Contoh request body
`
{
	"items": [{
		"sepal_length": 5.1,
		"sepal_width": 3.5,
		"petal_length": 1.4,
		"petal_width": 0.2
	},{
		"sepal_length": 5.1,
		"sepal_width": 3.5,
		"petal_length": 1.4,
		"petal_width": 0.2
	}]
}
`
atau
`
{
	"items": [[4.2,2.3,4,2.1], [5.6, 3, 3.5,1.5]]
}
`
