Convenience facilities for using FFmpeg (ffmpeg.org),
with invocation via `ffmpeg-python`.

*Latest release 20240201*:
* New $FFMPEG_EXE envvar.
* convert: use $FFMPEG_EXE, return the ffmpeg argv.
* convert: include the media type in DEFAULT_CONVERSIONS, refactor the choice of codec conversion.
* convert: supply dummy results if doit is false - could do with some finesse.
* ffmpeg_docker: use DockerRun.{add_input,add_output}.
* New main_ffmpeg_docker to support the ffmpeg-docker command, add ffmpeg-docker to DISTINFO scripts.

## Class `ConversionSource(builtins.tuple)`

ConversionSource(src, srcfmt, start_s, end_s)

*Property `ConversionSource.end_s`*:
Alias for field number 3

*Property `ConversionSource.src`*:
Alias for field number 0

*Property `ConversionSource.srcfmt`*:
Alias for field number 1

*Property `ConversionSource.start_s`*:
Alias for field number 2

## Function `convert(*srcs, dstpath: str, doit=True, dstfmt=None, ffmpeg_exe=None, fstags: cs.fstags.FSTags, conversions=None, metadata: Optional[dict] = None, timespans=(), overwrite=False, acodec=None, vcodec=None, extra_opts=None) -> List[str]`

Transcode video to `dstpath` in FFMPEG compatible `dstfmt`.

## Function `ffmpeg_docker(*ffmpeg_args: Iterable[str], docker_run_opts: Union[List[str], Mapping, NoneType] = None, doit: Optional[bool] = None, quiet: Optional[bool] = None, ffmpeg_exe: Optional[str] = None, docker_exe: Optional[str] = None, image: Optional[str] = None, outputpath: str = '.') -> Optional[subprocess.CompletedProcess]`

Invoke `ffmpeg` using docker.

## Class `FFmpegSource`

A representation of an `ffmpeg` input source.

*Method `FFmpegSource.add_as_input(self, ff)`*:
Add as an input to `ff`.
Return `None` if `self.source` is a pathname,
otherwise return the file descriptor of the data source.

Note: because we rely on `ff.input('pipe:')` for nonpathnames,
you can only use a nonpathname `FFmpegSource` for one of the inputs.
This is not checked.

*Method `FFmpegSource.promote(source)`*:
Promote `source` to an `FFmpegSource`.

## Function `ffprobe(input_file, *, doit=True, ffprobe_exe='ffprobe', quiet=False)`

Run `ffprobe -print_format json` on `input_file`,
return format, stream, program and chapter information
as an `AttrableMapping` (a `dict` subclass).

## Function `main_ffmpeg_docker(argv=None)`

The `ffm[peg-docker` command line implementation.

## Class `MetaData(cs.tagset.TagSet, builtins.dict, cs.dateutils.UNIXTimeMixin, cs.lex.FormatableMixin, cs.lex.FormatableFormatter, string.Formatter, cs.mappings.AttrableMappingMixin)`

Object containing fields which may be supplied to ffmpeg's -metadata option.

*Method `MetaData.__init__(self, format, **kw)`*:
pylint: disable=redefined-builtin

*Method `MetaData.options(self)`*:
Compute the FFmpeg -metadata option strings and return as a list.

# Release Log



*Release 20240201*:
* New $FFMPEG_EXE envvar.
* convert: use $FFMPEG_EXE, return the ffmpeg argv.
* convert: include the media type in DEFAULT_CONVERSIONS, refactor the choice of codec conversion.
* convert: supply dummy results if doit is false - could do with some finesse.
* ffmpeg_docker: use DockerRun.{add_input,add_output}.
* New main_ffmpeg_docker to support the ffmpeg-docker command, add ffmpeg-docker to DISTINFO scripts.

*Release 20231202*:
Initial PyPI release.
