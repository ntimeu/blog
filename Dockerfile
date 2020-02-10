FROM alpine:latest as builder
WORKDIR /tmp
RUN apk --no-cache add git hugo
RUN git clone --recursive --depth=1 https://github.com/ntimeu/blog.git
WORKDIR /tmp/blog
RUN hugo -D

FROM nginx:alpine
COPY --from=builder /tmp/blog/public /usr/share/nginx/html
