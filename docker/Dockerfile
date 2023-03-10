FROM python:3.10
ENV SERVICE_NAME='hello-world'
ARG APP_PATH="/hello-world"
WORKDIR ${APP_PATH}

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y libpq-dev && \
    apt-get clean -y && \
    apt-get autoremove -y


ENV VIRTUAL_ENV="$APP_PATH/venv"
RUN python3.10 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.10 -m pip install --upgrade pip
RUN pip install poetry

COPY . $APP_PATH
RUN cd $APP_PATH \
    make && \
    make install && \
    python -m compileall $APP_PATH/hello_wormald  


# Run server
EXPOSE 8000
# ["make", "run"] makes it not able to recieve Ctrl+C signal from console.
#ENTRYPOINT ["poetry", "show","--why"]
ENTRYPOINT ["poetry", "run", "python3.10", "-m", "hello_world"]