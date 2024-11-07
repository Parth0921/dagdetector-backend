from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from dag_helper import dag_dfs, dag_bfs 
from models import PipelineData

app = FastAPI()

# This is to allow CORS
origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://http://ec2-13-235-167-7.ap-south-1.compute.amazonaws.com/"
]

# Apply CORS configuration to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}


# Pipeline Parse endpoint which finds if the nodes and edges make a DAG or not
# dag_bfs and dag_dfs returns empty string if it is a DAG else it returns the node where cycle is detected
@app.post('/pipelines/parse', tags=['pipelines'])
def parse_pipeline(pipeline: PipelineData):
    nodes, edges = pipeline.nodes, pipeline.edges
    # is_dag= dag_bfs(nodes, edges)
    is_dag_str= dag_dfs(nodes, edges)

    is_dag = True if is_dag_str == "" else False
    
    return {
        'num_nodes': len(nodes),
        'num_edges': len(edges),
        'is_dag' : is_dag,
    }
