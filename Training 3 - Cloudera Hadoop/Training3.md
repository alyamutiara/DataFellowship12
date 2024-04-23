# Cloudera Hadoop

## How to install Cloudera using Docker
After downloading Docker and ensure that it is working in local computer, run this command in terminal to pull the image from docker hub.

```docker run cloudera/quickstart:latest```

It takes some time as the size is pretty big (around 4-6GB). After make sure that the image was pulled using `docker images`, run this command to run the image.

```docker run --hostname=quickstart.cloudera --privileged=true -t -i -v /path/to/volume:/src --publish-all=true -p 8888 cloudera/quickstart /usr/bin/docker-quickstart```

Details regarding the command:
- `quickstart.cloudera` is the hostname in privileged mode, which is required for HBase.
- `-t` flag means to specify the tag or name of the image.
- `-i` or `-ii` flag means to open it in the terminal.
- `-v` or `--volume` flag means to mount a host (or local computer) directory (or volume) to a container followed by the volume path. So anything put inside `/path/to/volume` will be accessible from `/src` path inside the container.
- `--publish-all=true` will opens up all the host ports to the docker ports.

Or can run this:
```docker run --hostname=quickstart.cloudera --privileged=true -t -i -p 8888:8888 -p 7180:7180 -p 80:80 <imageID> /usr/bin/docker-quickstart```


[^docker-cheatsheet]: Docker cheatsheet refer to https://collabnix.com/docker-cheatsheet/