FROM python:3
RUN mkdir /apiautomation
RUN pip install pytest
RUN pip install requests
RUN pip install jsonpath
RUN pip install wsproto
WORKDIR /apiautomation
COPY ./apiautomation .
CMD ["pytest", "-v", "-s"]
