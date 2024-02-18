from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI() #creating our 'app' here. this is what we call in our command to run

#TO RUN: uvicorn main:app --reload
#This must be from inside the SRC folder
#Alternatively, uvicorn cyb600_lab1_perreaua10.egg-info.main:app --reload can be used from root folder.


@app.get("/time", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <h1> """ + "Current Time is: " + str(datetime.now().strftime("%H:%M:%S")) + """
        </h1>
    </html>
    """

    


