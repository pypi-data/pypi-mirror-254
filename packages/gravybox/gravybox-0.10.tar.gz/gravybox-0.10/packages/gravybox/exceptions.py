from gravybox.betterstack import collect_logger

logger = collect_logger()


class GravyboxException(Exception):
    pass


class UpstreamAPIFailure(GravyboxException):
    def __init__(self, query, upstream_api, upstream_status_code, upstream_content):
        super().__init__("upstream api failure")
        logger.warning(
            "upstream api failure",
            extra={"query": query,
                   "upstream_api": upstream_api,
                   "status_code": upstream_status_code,
                   "payload": upstream_content
                   }
        )


class UnexpectedCondition(GravyboxException):
    def __init__(self, condition):
        super().__init__(f"encountered unexpected condition: {condition}")
        logger.warning(
            "encountered unexpected condition",
            extra={"condition": condition}
        )


class MalformedInput(GravyboxException):
    def __init__(self, malformed_input):
        super().__init__(f"malformed input: {malformed_input}")
        logger.warning(
            "malformed input",
            extra={"malformed_input": malformed_input}
        )
