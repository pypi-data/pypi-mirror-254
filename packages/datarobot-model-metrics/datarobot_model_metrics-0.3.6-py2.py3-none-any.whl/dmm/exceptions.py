class DataRobotAPIError(Exception):
    pass


class DRCustomMetricConfigError(Exception):
    pass


class CustomMetricNotFound(Exception):
    pass


class ConflictError(Exception):
    pass


class DRSourceNotSupported(Exception):
    pass


class DataExportJobError(Exception):
    pass
