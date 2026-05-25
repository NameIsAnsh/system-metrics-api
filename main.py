from fastapi import FastAPI
import psutil 
app=FastAPI()

@app.get("/health")
def health_check():
    return {"status":"healthy","version":"1.1 - CI/CD Active"}
@app.get("/cpu")
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return {"cpu_percentage": cpu_usage}
@app.get("/ram")
def get_ram_usage():
    ram_usage= psutil.virtual_memory().percent
    return {"ram_percent" : ram_usage}

