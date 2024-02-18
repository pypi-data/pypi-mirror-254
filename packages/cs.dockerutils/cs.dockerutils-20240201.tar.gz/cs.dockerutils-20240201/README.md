Docker related utilities.

*Latest release 20240201*:
* mount_escape: strip trailing carriage return also.
* DockerRun: new output_map attribute much like input_map; also mount existing outputs within the container.

## Function `default_docker_command()`

pylint: disable=unnecessary-lambda-assignment

## Function `default_docker_compose_command()`

pylint: disable=unnecessary-lambda-assignment

## Function `default_docker_compose_config()`

pylint: disable=unnecessary-lambda-assignment

## Function `docker(*dk_argv, exe=None, doit=True, quiet=True) -> subprocess.CompletedProcess`

Invoke `docker` with `dk_argv`.

## Function `docker_compose(*dc_argv, exe=None, config=None, doit=True, quiet=True) -> subprocess.CompletedProcess`

Invoke `docker-compose` with `dc_argv`.

## Class `DockerRun`

A `DockerRun` specifies how to prepare docker to execute a command.

This is a generic wrapper for invoking a docker image and
internal executable to process data from the host system,
essentially a flexible and cleaned up version of the wrappers
used to invoke things like the `linuxserver:*` utility docker
images.

Input paths for the executable will be presented in a read
only directory, by default `/input' inside the container.

An output directory (default '.', the current durectory) will
be mounted read/write inside the container, by default `/output`
inside the container.

_Unlike_ a lot of docker setups, the default mode runs as the
invoking user's UID/GID inside the container and expects the
`s6-setuidgid` utility to be present in the image.

See the `ffmpeg_docker` function from `cs.ffmpegutils` for
an example invocation of this class.

*Method `DockerRun.add_input(self, infspath: str) -> str`*:
Add a host filesystem path to the `input_map`
and return the corresponding container filesystem path.

*Method `DockerRun.add_output(self, outfspath: str) -> str`*:
Add a host filesystem path to the `output_map`
and return the corresponding container filesystem path.

*Method `DockerRun.popopts(self, argv: List[str]) -> None`*:
Pop options from the list `argv`.

The command's working directory will be /output.
-i inputpath
    Mount inputpath as /input/basename(inputpath)
--root
    Do not switch to the current effective uid:gid inside
    the container.
-U  Update the local copy of image before running.
Other options are passed to "docker run".

*Method `DockerRun.run(self, *argv, doit=None, quiet=None, docker_exe=None)`*:
Run a command via `docker run`.
Return the `CompletedProcess` result or `None` if `doit` is false.

## Class `DockerUtilCommand(cs.cmdutils.BaseCommand)`

A command line mode for working with Docker et al.

Command line usage:

    Usage: dockerutil [options...] [@container] subcommand...
        -f docker-compose.yml
          Specify ['docker', 'compose'] YAML file.
          Default: 'docker-compose.yml', overridden by $DK_COMPOSE_YML
        @container  Specify a target container.

      Subcommands:
        help [-l] [subcommand-names...]
          Print the full help for the named subcommands,
          or for all subcommands if no names are specified.
          -l  Long help even if no subcommand-names provided.
        ps
          Show the running docker containers.
        run [options] image [command] [arg...]
          Invoke command in an instance of image.
          A read only directory for input data will be present as /input.
          A read/write directory for output data will be present at /output.
          The command's working directory will be /output.
          -i inputpath
              Mount inputpath as /input/basename(inputpath)
          --root
              Do not switch to the current effective uid:gid inside
              the container.
          -U  Update the local copy of image before running.
          Other options are passed to "docker run".
        shell
          Run a command prompt via cmd.Cmd using this command's subcommands.

*`DockerUtilCommand.Options`*

*Method `DockerUtilCommand.apply_preargv(self, argv)`*:
Consume a leading @container_name if present.

*Method `DockerUtilCommand.cmd_ps(self, argv)`*:
Usage: {cmd}
Show the running docker containers.

*Method `DockerUtilCommand.cmd_run(self, argv)`*:
Usage: {cmd} [options] image [command] [arg...]
Invoke command in an instance of image.
A read only directory for input data will be present as /input.
A read/write directory for output data will be present at /output.
The command's working directory will be /output.
-i inputpath
    Mount inputpath as /input/basename(inputpath)
--root
    Do not switch to the current effective uid:gid inside
    the container.
-U  Update the local copy of image before running.
Other options are passed to "docker run".

*Method `DockerUtilCommand.docker(self, *dk_argv) -> subprocess.CompletedProcess`*:
Invoke `docker`.

*Method `DockerUtilCommand.docker_compose(self, *dc_argv) -> subprocess.CompletedProcess`*:
Invoke `docker-compose`.

## Class `DockerUtilCommandOptions(cs.cmdutils.BaseCommandOptions)`

Command line options for `DockerUtilCommand`.

## Function `main(argv=None, **run_kw)`

Invoke the `DockerUtilCommand` with `argv`.

## Function `mount_escape(*args) -> str`

Escape the strings in `args` for us in the `docker run --mount` option.

Apparently the arguments to `docker run --mount` are in fact
a CSV data line.
(Of course you need to find this allusion in the bug tracker,
heaven forfend that the docs actually detail this kind of
thing.)

Rather that try to enumerate what needs escaping, here we use
the `csv` module to escape using the default "excel" dialect.

# Release Log



*Release 20240201*:
* mount_escape: strip trailing carriage return also.
* DockerRun: new output_map attribute much like input_map; also mount existing outputs within the container.

*Release 20231202*:
Initial PyPI release.
