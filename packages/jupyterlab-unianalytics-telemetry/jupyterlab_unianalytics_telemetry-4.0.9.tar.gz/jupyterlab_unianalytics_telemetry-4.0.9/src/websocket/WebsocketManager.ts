import { PERSISTENT_USER_ID } from '..';
import { APP_ID, WEBSOCKET_API_URL } from '../utils/constants';

export class WebsocketManager {
  constructor() {
    this._socket = null;

    this._pingInterval = 540000; // 9min (AWS disconnects after 10min idle)
    this._pingTimer = null;
  }

  private _createSocket(notebookId: string, userId: string) {
    this._socket = new WebSocket(
      `${WEBSOCKET_API_URL}?conType=STUDENT&nbId=${notebookId}&usrId=${userId}`
    );

    this._socket.addEventListener('open', () => {
      console.log(`${APP_ID}: WebSocket connection opened for`, {
        notebookId,
        userId
      });

      this._startPingTimer();
    });

    this._socket.addEventListener('message', event => {
      const message = JSON.parse(event.data);
      if (message.action === 'BLA BLA BLA') {
        // process the message
      }
      console.log(`${APP_ID}: Received message from server:`, message);
      // Handle messages from the server
    });

    this._socket.addEventListener('close', event => {
      console.log(
        `${APP_ID}: WebSocket connection closed for `,
        { notebookId, userId },
        event
      );

      this._stopPingTimer();
    });

    this._socket.addEventListener('error', event => {
      console.error(`${APP_ID}: WebSocket error`, event);
    });
  }

  public establishSocketConnection(notebookId: string | null) {
    // if there is already a connection, close it and set the socket to null
    this._closeSocketConnection();

    if (!notebookId || !PERSISTENT_USER_ID) {
      return;
    }
    this._createSocket(notebookId, PERSISTENT_USER_ID);
  }

  // close the connection without resetting connection info in case the connection is closed with setting change
  private _closeSocketConnection() {
    if (this._socket) {
      this._socket.close();
    }
    this._socket = null;
  }

  // terminate connection when a panel is disposed/switched, reset connection info
  public terminateSocketConnection() {
    this._closeSocketConnection();
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
  private _pingInterval: number;
  private _pingTimer: number | null;
}
