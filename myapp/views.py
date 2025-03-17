from django.shortcuts import render
from django.http import HttpResponse
import os
import datetime
import subprocess

def htop_view(request):
    name = "Shravani"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    # Get top output (first 10 lines for brevity)
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    response_html = f"""
    <h1>HTOP Endpoint</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {formatted_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response_html)
