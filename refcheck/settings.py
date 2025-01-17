from refcheck.parsers import get_command_line_arguments


class Settings:
    def __init__(self):
        try:
            args = get_command_line_arguments()
        except AssertionError:
            raise SystemExit(1)

        self._verbose = args.verbose
        self._check_remote = args.check_remote
        self._no_color = args.no_color
        self._allow_absolute = args.allow_absolute
        self._paths = args.paths
        self._exclude = args.exclude

    @property
    def verbose(self) -> bool:
        return self._verbose

    @property
    def check_remote(self) -> bool:
        return self._check_remote

    @property
    def no_color(self) -> bool:
        return self._no_color

    @property
    def allow_absolute(self) -> bool:
        return self._allow_absolute

    @property
    def paths(self) -> list[str]:
        return self._paths

    @property
    def exclude(self) -> list[str]:
        return self._exclude


settings = Settings()
