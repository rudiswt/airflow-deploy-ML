# efsihery-assesment-ML
eFishery recruitment process for the Machine Learning Engineer position. 
Rudi Setiawan - rudiswtn@gmail.com

### Restore Database

### run airflow/scheduler
`
docker-compose up airflow-init
docker-compose up
`
#### to trigger DAG
`
Open localhost:8080 on the browser
user airflow
pass airflow
`

### run rest api
`
pip install -r requirements.txt
python main.py
`
#### to test API
`localhost:8080/predict`
