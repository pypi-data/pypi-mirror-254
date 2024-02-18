import logging
from typing import (  # for type hinting
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

# from byteblowerll.byteblower import HTTPResultDataList  # for type hinting
from byteblowerll.byteblower import HTTPResultData  # for type hinting
from byteblowerll.byteblower import (  # for type hinting
    ByteBlowerAPIException,
    DataRate,
    HTTPClient,
    HTTPClientMobile,
    HTTPRequestMethod,
    HTTPResultHistory,
    HTTPServer,
)
from pandas import DataFrame  # for type hinting
from pandas import Timestamp  # for type hinting
from pandas import Int64Dtype, to_datetime

from ..storage.tcp import HttpData
from .data_gatherer import DataGatherer


class HttpDataGatherer(DataGatherer):

    __slots__ = (
        '_http_data',
        '_bb_tcp_clients',
        '_bb_tcp_server',
        '_client_index',
    )

    def __init__(
        self,
        http_data: HttpData,
        bb_tcp_clients: Union[List[HTTPClient], List[HTTPClientMobile]],
    ) -> None:
        super().__init__()
        self._http_data = http_data
        self._bb_tcp_clients = bb_tcp_clients
        self._bb_tcp_server: Optional[HTTPServer] = None

        self._client_index = 0

    def set_http_server(self, bb_tcp_server: HTTPServer) -> None:
        self._bb_tcp_server = bb_tcp_server

    def updatestats(self) -> None:
        """
        Analyse the result.

        .. warning::
           What would be bad?

           - TCP sessions not going to ``Finished`` state.
        """
        # Let's analyse the result
        self._update_history_snapshots()

    def summarize(self) -> None:
        """
        Store the final results.

        Stores the average data speed over the complete session.

        .. warning::
           This summary does not support multiple clients yet.
           It is only created for the last client.
        """
        # NOTE: Could still end up as None
        #       when no client started at all!
        method = None

        # Set HTTP data transfer results
        # ! FIXME - Take average over multiple clients
        value_data_speed = None

        # Set HTTP client results
        value_data_speed_client = None
        mobile_client = None
        total_rx_client = 0
        total_tx_client = 0
        rx_first_client = None
        rx_last_client = None
        tx_first_client = None
        tx_last_client = None

        # Set HTTP server results
        value_data_speed_server = None
        total_rx_server = 0
        total_tx_server = 0
        rx_first_server = None
        rx_last_server = None
        tx_first_server = None
        tx_last_server = None

        # Sanity checks
        if len(self._bb_tcp_clients) > 1:
            logging.warning(
                'HttpAnalyser summary only supports one client for now.'
                ' The test used %d clients.', len(self._bb_tcp_clients)
            )

        # Add remaining history snapshots
        # ! FIXME: Avoid multiple HTTPResultHistory.Refresh() calls
        self._update_history_snapshots()

        # Take only the last client (if one available)
        for client in self._bb_tcp_clients[-1:]:
            mobile_client = isinstance(client, HTTPClientMobile)
            server_client_id = client.ServerClientIdGet()
            method: HTTPRequestMethod = client.HttpMethodGet()
            try:
                result_history_client: HTTPResultHistory = (
                    client.ResultHistoryGet()
                )
                (
                    value_data_speed_client,
                    total_rx_client,
                    total_tx_client,
                    rx_first_client,
                    rx_last_client,
                    tx_first_client,
                    tx_last_client,
                ) = self._get_summary_data(
                    f'HTTP Client {server_client_id!r}',
                    result_history_client,
                    self._http_data.df_tcp_client,
                    True,
                )
            except ByteBlowerAPIException as error:
                logging.warning(
                    "Couldn't get HTTP Client %r result history"
                    " in HttpAnalyser summary: %s",
                    server_client_id,
                    error.getMessage(),
                )

            try:
                result_history_server: HTTPResultHistory = (
                    self._bb_tcp_server.ResultHistoryGet(server_client_id)
                )
            except ByteBlowerAPIException as error:
                logging.warning(
                    "Couldn't get HTTP Server for Client %r"
                    " result history in HttpAnalyser summary: %s",
                    server_client_id,
                    error.getMessage(),
                )
                # No further processing
                continue
            (
                value_data_speed_server,
                total_rx_server,
                total_tx_server,
                rx_first_server,
                rx_last_server,
                tx_first_server,
                tx_last_server,
            ) = self._get_summary_data(
                f'HTTP Server for Client {server_client_id!r}',
                result_history_server,
                self._http_data.df_tcp_server,
                value_data_speed_client is None,
            )

        value_data_speed = (
            value_data_speed_client
            if value_data_speed_client is not None else value_data_speed_server
        )

        if method == HTTPRequestMethod.Get:
            self._http_data._http_method = "GET"
        elif method == HTTPRequestMethod.Put:
            self._http_data._http_method = "PUT"
        else:
            logging.warning(
                'HttpDataGatherer: Unsupported HTTP Method (%s).'
                ' Storing original value.', method
            )
            self._http_data._http_method = method

        self._http_data._avg_data_speed = value_data_speed
        # Set client results
        self._http_data._mobile_client = mobile_client
        self._http_data._total_rx_client = total_rx_client
        self._http_data._total_tx_client = total_tx_client
        self._http_data._ts_rx_first_client = rx_first_client
        self._http_data._ts_rx_last_client = rx_last_client
        self._http_data._ts_tx_first_client = tx_first_client
        self._http_data._ts_tx_last_client = tx_last_client
        # Make sure we store the count and duration (in nanoseconds) as Int64:
        self._http_data._df_tcp_client = (
            self._http_data._df_tcp_client.astype(
                {
                    'duration': Int64Dtype(),
                    'TX Bytes': Int64Dtype(),
                    'RX Bytes': Int64Dtype(),
                    # 'AVG dataspeed': Float64Dtype(),
                }
            )
        )
        # Set server results
        self._http_data._total_rx_server = total_rx_server
        self._http_data._total_tx_server = total_tx_server
        self._http_data._ts_rx_first_server = rx_first_server
        self._http_data._ts_rx_last_server = rx_last_server
        self._http_data._ts_tx_first_server = tx_first_server
        self._http_data._ts_tx_last_server = tx_last_server
        # Make sure we store the count and duration (in nanoseconds) as Int64:
        self._http_data._df_tcp_server = (
            self._http_data._df_tcp_server.astype(
                {
                    'duration': Int64Dtype(),
                    'TX Bytes': Int64Dtype(),
                    'RX Bytes': Int64Dtype(),
                    # 'AVG dataspeed': Float64Dtype(),
                }
            )
        )

    def release(self) -> None:
        super().release()
        # NOTE: HTTP Server and Clients will be released from the TcpFlow.
        try:
            del self._bb_tcp_clients
        except AttributeError:
            logging.warning(
                'HttpDataGatherer: TCP clients already destroyed?',
                exc_info=True
            )
        try:
            del self._bb_tcp_server
        except AttributeError:
            logging.warning(
                'HttpDataGatherer: TCP server already destroyed?',
                exc_info=True
            )

    def _get_summary_data(
        self, _name: str, result_history: HTTPResultHistory,
        over_time_results: DataFrame, need_value_data_speed: bool
    ) -> Tuple[
            Optional[float],
            Optional[int],
            Optional[int],
            Optional[Timestamp],
            Optional[Timestamp],
            Optional[Timestamp],
            Optional[Timestamp],
    ]:
        value_data_speed = None
        # Set HTTP results
        total_rx = 0
        total_tx = 0
        rx_first = None
        rx_last = None
        tx_first = None
        tx_last = None

        # Get interval result
        result_history.Refresh()

        if result_history.CumulativeLengthGet() > 0:
            http_result_data: HTTPResultData = (
                result_history.CumulativeLatestGet()
            )
            try:
                total_rx: int = http_result_data.RxByteCountTotalGet()
                total_tx: int = http_result_data.TxByteCountTotalGet()
                rx_first = to_datetime(
                    cast(int, http_result_data.RxTimestampFirstGet()),
                    unit='ns',
                    utc=True,
                )
                rx_last = to_datetime(
                    cast(int, http_result_data.RxTimestampLastGet()),
                    unit='ns',
                    utc=True,
                )
                tx_first = to_datetime(
                    cast(int, http_result_data.TxTimestampFirstGet()),
                    unit='ns',
                    utc=True,
                )
                tx_last = to_datetime(
                    cast(int, http_result_data.TxTimestampLastGet()),
                    unit='ns',
                    utc=True,
                )

                if need_value_data_speed:
                    average_data_speed: DataRate = (
                        http_result_data.AverageDataSpeedGet()
                    )
                    value_data_speed: float = average_data_speed.ByteRateGet()

                # Persist latest/final snapshot
                timestamp_ns: int = http_result_data.TimestampGet()
                interval_snapshot: HTTPResultData = (
                    result_history.IntervalGetByTime(timestamp_ns)
                )
                timestamp = to_datetime(timestamp_ns, unit='ns', utc=True)
                self._persist_history_snapshot(
                    _name, timestamp, interval_snapshot, over_time_results
                )
            except ByteBlowerAPIException as error:
                logging.warning(
                    "Couldn't get %r results in HttpAnalyser: %s",
                    _name,
                    error.getMessage(),
                    exc_info=True,
                )
        else:
            logging.info("HttpAnalyser: No final %r results", _name)

        return (
            value_data_speed,
            total_rx,
            total_tx,
            rx_first,
            rx_last,
            tx_first,
            tx_last,
        )

    def _update_history_snapshots(self) -> None:
        """Add all the history interval results."""
        # NOTE - Not analysing results for finished HTTP clients
        #        in a previous iteration of "update stats":
        for client in self._bb_tcp_clients[self._client_index:]:
            self._update_client_history_snapshots(client)

            self._update_server_history_snapshots(client)

        # NOTE - Don't analyse results for finished HTTP clients
        #        in a next iteration of updatestats:
        self._client_index = len(self._bb_tcp_clients)
        if self._client_index > 0:
            # ! FIXME - Shouldn't we check if HTTP client actually finished?
            self._client_index -= 1

    def _update_client_history_snapshots(
        self, client: Union[HTTPClient, HTTPClientMobile]
    ) -> None:
        """Add all the history interval results."""
        server_client_id = client.ServerClientIdGet()
        try:
            # Get result history
            result_history: HTTPResultHistory = client.ResultHistoryGet()

            # Update history snapshots
            self._update_http_history_snapshots(
                f'HTTP Client {server_client_id!r}',
                result_history,
                self._http_data.df_tcp_client,
            )
        except ByteBlowerAPIException as error:
            # "Session is not available" can happen when
            # the client request was not sent (yet)
            if not 'Session is not available' in error.getMessage():
                logging.warning(
                    "Couldn't get HTTP Client %r result in HttpAnalyser: %s",
                    server_client_id,
                    error.getMessage(),
                )

    def _update_server_history_snapshots(
        self, client: Union[HTTPClient, HTTPClientMobile]
    ) -> None:
        server_client_id = client.ServerClientIdGet()
        try:
            # Get result history
            result_history: HTTPResultHistory = (
                self._bb_tcp_server.ResultHistoryGet(server_client_id)
            )

            # Update history snapshots
            self._update_http_history_snapshots(
                f'HTTP Server for Client {server_client_id!r}',
                result_history,
                self._http_data.df_tcp_server,
            )
        except ByteBlowerAPIException as error:
            # "Session is not available" can happen when
            # the client request was not received (yet)
            if not 'Session is not available' in error.getMessage():
                logging.warning(
                    "Couldn't get HTTP Server for Client %r result"
                    " in HttpAnalyser: %s",
                    server_client_id,
                    error.getMessage(),
                )

    @classmethod
    def _update_http_history_snapshots(
        cls, _name: str, result_history: HTTPResultHistory,
        over_time_results: DataFrame
    ) -> None:
        # Refresh the result history
        result_history.Refresh()

        cls._persist_history_snapshots(
            _name, result_history, over_time_results
        )

        # Clear the result history
        result_history.Clear()

    @classmethod
    def _persist_history_snapshots(
        cls, _name: str, result_history: HTTPResultHistory,
        over_time_results: DataFrame
    ) -> None:
        # Cfr. HTTPResultDataList
        interval_snapshots: Sequence[HTTPResultData] = (
            result_history.IntervalGet()
        )

        for interval_snapshot in interval_snapshots[:-1]:
            timestamp_ns: int = interval_snapshot.TimestampGet()
            timestamp = to_datetime(timestamp_ns, unit='ns', utc=True)
            cls._persist_history_snapshot(
                _name, timestamp, interval_snapshot, over_time_results
            )

    @classmethod
    def _persist_history_snapshot(
        cls, _name: str, timestamp: Timestamp,
        interval_snapshot: HTTPResultData, over_time_results: DataFrame
    ) -> None:
        average_data_speed: DataRate = (
            interval_snapshot.AverageDataSpeedGet()
        )
        interval_duration = interval_snapshot.IntervalDurationGet()
        interval_rx_bytes = interval_snapshot.RxByteCountTotalGet()
        interval_tx_bytes = interval_snapshot.TxByteCountTotalGet()
        interval_avg_dataspeed = average_data_speed.ByteRateGet()
        try:
            existing_snapshot = over_time_results.loc[timestamp]
        except KeyError:
            over_time_results.loc[timestamp] = (
                interval_duration,
                interval_tx_bytes,
                interval_rx_bytes,
                interval_avg_dataspeed,
            )
        else:
            logging.warning(
                '%s: Found existing snapshot @ %r',
                _name,
                timestamp,
            )
            existing_duration = existing_snapshot['duration']
            if existing_duration != interval_duration:
                logging.warning(
                    '%s: Found existing snapshot'
                    ' with different duration (%r <> %r)',
                    _name,
                    existing_duration,
                    interval_duration,
                )
            existing_snapshot['TX Bytes'] += interval_tx_bytes
            existing_snapshot['RX Bytes'] += interval_rx_bytes
            existing_snapshot['AVG dataspeed'] += interval_avg_dataspeed
