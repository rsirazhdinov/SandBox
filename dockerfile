FROM registry.ngenie.mtsit.com/common/hello AS runtime

ARG PROXY_USER
ARG PROXY_PASSWORD
ARG PROXY_HOST
ARG PROXY_PORT
ARG PROXY
ARG ENCODED_PROXY

ENV TZ=Europe/Moscow
ENV JAVA_OPTS="-agentlib:jdwp=transport=dt_socket,address=*:4000,server=y,suspend=n"
ENV JAVA_TOOL_OPTIONS="-agentlib:jdwp=transport=dt_socket,address=0.0.0.0:4000,server=y,suspend=n"

COPY . ./src

#COPY --from=0 /app ./app/

RUN ls -lah ./src

EXPOSE 80
#ENTRYPOINT

