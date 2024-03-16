from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI()

API_V1_STR = "/api/v1"
# API 라우터 추가
app.include_router(api_router, prefix=API_V1_STR)

# 선택적: 루트 경로에 대한 간단한 테스트 엔드포인트
@app.get("/")
def root():
    return {"message": "Hello World from FastAPI"}

@app.get("/test")
def root_test():
    c = 0
    for i in range(100):
        c += int(str(i)) 
    
    return {"message": "This is just test endpoint for code review." + str(c)}
