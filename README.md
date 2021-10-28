
#uruchomienie serwera:

    python manage.py runserver

#budowanie projektu

    django-admin startproject Django_sklep

#budowanie kategorii

    python manage.py startapp Produkty

#zaakceptowanie/przebudowanie modelu w pliku models.py

    python manage.py makemigrations
    python manage.py migrate

#listuje wszystkie pakiety potrzebne do uruchomienia projektu

    pip freeze 
################################################################################
#1) Listing available containers 
    docker ps
#2) to enter container
    
    docker exec -it {id} bash

#3) to rebuild container  
    
    docker-compose build {nazwa}

#4)  start project containers
    
    docker-compose up

       
#tworzenie superusera
    
    python manage.py createsuperuser
#DEV

    To enter container docker exec -it {id} bash
    To rebuild container docker-compose build {nazwa}
    Start project's containers docker-compose up

    Usage:  docker [OPTIONS] COMMAND

    A self-sufficient runtime for containers
    
    Options:
          --config string      Location of client config files (default
                               "C:\\Users\\ggrek\\.docker")
      -c, --context string     Name of the context to use to connect to the
                               daemon (overrides DOCKER_HOST env var and
                               default context set with "docker context use")
      -D, --debug              Enable debug mode
      -H, --host list          Daemon socket(s) to connect to
      -l, --log-level string   Set the logging level
                               ("debug"|"info"|"warn"|"error"|"fatal")
                               (default "info")
          --tls                Use TLS; implied by --tlsverify
          --tlscacert string   Trust certs signed only by this CA (default
                               "C:\\Users\\ggrek\\.docker\\ca.pem")
          --tlscert string     Path to TLS certificate file (default
                               "C:\\Users\\ggrek\\.docker\\cert.pem")
          --tlskey string      Path to TLS key file (default
                               "C:\\Users\\ggrek\\.docker\\key.pem")
          --tlsverify          Use TLS and verify the remote
      -v, --version            Print version information and quit
    
    Management Commands:
      builder     Manage builds
      buildx*     Build with BuildKit (Docker Inc., v0.6.3)
      compose*    Docker Compose (Docker Inc., v2.0.0)
      config      Manage Docker configs
      container   Manage containers
      context     Manage contexts
      image       Manage images
      manifest    Manage Docker image manifests and manifest lists
      network     Manage networks
      node        Manage Swarm nodes
      plugin      Manage plugins
      scan*       Docker Scan (Docker Inc., v0.8.0)
      secret      Manage Docker secrets
      service     Manage services
      stack       Manage Docker stacks
      swarm       Manage Swarm
      system      Manage Docker
      trust       Manage trust on Docker images
      volume      Manage volumes
    
    Commands:
      attach      Attach local standard input, output, and error streams to a running container
      build       Build an image from a Dockerfile
      commit      Create a new image from a container's changes
      cp          Copy files/folders between a container and the local filesystem
      create      Create a new container
      diff        Inspect changes to files or directories on a container's filesystem
      events      Get real time events from the server
      exec        Run a command in a running container
      export      Export a container's filesystem as a tar archive
      history     Show the history of an image
      images      List images
      import      Import the contents from a tarball to create a filesystem image
      info        Display system-wide information
      inspect     Return low-level information on Docker objects
      kill        Kill one or more running containers
      load        Load an image from a tar archive or STDIN
      login       Log in to a Docker registry
      logout      Log out from a Docker registry
      logs        Fetch the logs of a container
      pause       Pause all processes within one or more containers
      port        List port mappings or a specific mapping for the container
      ps          List containers
      pull        Pull an image or a repository from a registry
      push        Push an image or a repository to a registry
      rename      Rename a container
      restart     Restart one or more containers
      rm          Remove one or more containers
      rmi         Remove one or more images
      run         Run a command in a new container
      save        Save one or more images to a tar archive (streamed to STDOUT by default)
      search      Search the Docker Hub for images
      start       Start one or more stopped containers
      stats       Display a live stream of container(s) resource usage statistics
      stop        Stop one or more running containers
      tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
      top         Display the running processes of a container
      unpause     Unpause all processes within one or more containers
      update      Update configuration of one or more containers
      version     Show the Docker version information
      wait        Block until one or more containers stop, then print their exit codes
#######################################################################################