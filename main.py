from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from dag_helper import dag_dfs, dag_bfs 
from models import PipelineData

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
]

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


# is dag would be empty string then it is dag otherwise it is the node which is causing the cycle
@app.post('/pipelines/parse', tags=['pipelines'])
def parse_pipeline(pipeline: PipelineData):
    nodes, edges = pipeline.nodes, pipeline.edges
    is_dag_bfs = dag_bfs(nodes, edges)
    is_dag_dfs = dag_dfs(nodes, edges)
    
    return {
        'num_nodes': len(nodes),
        'num_edges': len(edges),
        'is_dag_bfs' : is_dag_bfs,
        'is_dag_dfs' : is_dag_dfs
    }
