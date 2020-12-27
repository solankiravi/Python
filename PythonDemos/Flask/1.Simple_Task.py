from flask import Flask, request
import redis, time
from rq import Queue
from rq.connections import Connection

app = Flask(__name__)

r= redis.Redis()

q= Queue(Connection=r)

def background_task(n):
    delay = 2
    print("Task running =====")
    print(f"Simulating {delay} second delay")
    time.sleep(delay)
    print(len(n))
    print("Task complete")
    return len(n)

@app.route("/task")
def add_task():
    if request.args.get("n"):
        job = q.enqueue(background_task,request.args.get("n"))
        q_len= len(q)
        return f"Task {job.id} added to queue at {job.ended_at}. {q_len} task in the queue"
    return "No value for n"

if __name__=="__main__":
    app.run()
