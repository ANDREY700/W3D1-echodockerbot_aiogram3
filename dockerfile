FROM python:3.10-slim
ENV TOKEN=' - token code here - '
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "Echo_700_bot.py" ]





