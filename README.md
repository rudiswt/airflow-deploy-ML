# efsihery-assesment-ML
eFishery recruitment process for the Machine Learning Engineer position. 
Rudi Setiawan - rudiswtn@gmail.com

### Restore Database

### run airflow/scheduler
`
docker-compose up airflow-init <br /> 
docker-compose up
`
#### to trigger DAG
`
Open localhost:8080 on the browser <br /> 
user airflow <br /> 
pass airflow
`

### run rest api
`
pip install -r requirements.txt <br /> 
python main.py
`
#### to test API
`localhost:8080/predict`
