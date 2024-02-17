import { refreshDashboards } from '../redux/reducers/CommonDashboardReducer';
import { AppDispatch, store } from '../redux/store';
import { APP_ID, WEBSOCKET_API_URL } from '../utils/constants';
import { NotebookTags } from '../utils/interfaces';

const dispatch = store.dispatch as AppDispatch;

export class WebsocketManager {
  constructor() {
    this._socket = null;
    this._ongoingConnectionInfo = null;

    this._pingInterval = 540000; // 9min (AWS disconnects after 10min idle)
    this._pingTimer = null;
  }

  private _createSocket(connectionInfo: NotebookTags) {
    this._socket = new WebSocket(
      `${WEBSOCKET_API_URL}?nbId=${connectionInfo.notebookId}&conType=TEACHER`
    );

    this._socket.addEventListener('open', () => {
      console.log(`${APP_ID}: WebSocket connection opened for`, connectionInfo);

      this._startPingTimer();
    });

    this._socket.addEventListener('message', event => {
      const message = JSON.parse(event.data);
      if (message.action === 'refreshDashboard') {
        dispatch(refreshDashboards());
      }
      console.log(`${APP_ID}: Received message from server:`, message);
      // Handle messages from the server
    });

    this._socket.addEventListener('close', event => {
      console.log(
        `${APP_ID}: WebSocket connection closed for `,
        connectionInfo,
        event
      );

      this._stopPingTimer();
    });

    this._socket.addEventListener('error', event => {
      console.error(`${APP_ID}: WebSocket error`, event);
    });
  }

  public establishSocketConnection(connectionInfo: NotebookTags | null) {
    // if there is already a connection, close it and set the socket to null
    this._closeSocketConnection();

    this._ongoingConnectionInfo = connectionInfo;

    if (!connectionInfo) {
      return;
    }

    this._createSocket(connectionInfo);
  }

  // close the connection without resetting connection info in case the connection is closed with setting change
  private _closeSocketConnection() {
    if (this._socket) {
      this._socket.close();
    }
    this._socket = null;
  }

  public terminateSocketConnection() {
    this._closeSocketConnection();
    this._ongoingConnectionInfo = null;
  }

  private _startPingTimer() {
    this._pingTimer = window.setInterval(() => {
      if (this._socket && this._socket.readyState === WebSocket.OPEN) {
        this._socket.send('{ "action":"ping" }');
      }
    }, this._pingInterval);
  }

  private _stopPingTimer() {
    if (this._pingTimer) {
      clearInterval(this._pingTimer);
      this._pingTimer = null;
    }
  }

  private _socket: WebSocket | null;
  private _ongoingConnectionInfo: NotebookTags | null;
  private _pingInterval: number;
  private _pingTimer: number | null;
}
