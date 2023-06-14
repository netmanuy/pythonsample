# Dockers simple Python sample

## Build the docker image image

```
docker build -t pythonsample .
```

## Execute the docker app locally for testing & debug

```
docker run -p 80:80 pythonsample:latest
```

## Execute the docker and keep running as daemon 
```
docker run -d -p 80:80 pythonsample:latest
```
