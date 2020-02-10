# NTimeu's blog

This is the source code of my blog, located at [ntimeu.fr](http://ntimeu.fr/).
Actually, the code for the blog is under a GPLv3 license (see the file LICENSE
for more informations), and the content is released under a
[Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

## Installing

1. install [Hugo](https://gohugo.io/)
2. hugo server -D

Enjoy !


## Docker deployment

For those of you who like dockerizing everything, I provide a Dockerfile that
you can use to deploy the web site as a docker image. It is a multistage build
Dockerfile :

1. compiles all static files using alpine:latest
2. copy all those files on the nginx:alpine image

After building the image, you might need to run a prune on all docker images,
as the multistage build does not automatically erase intermediate images used
only for build.
