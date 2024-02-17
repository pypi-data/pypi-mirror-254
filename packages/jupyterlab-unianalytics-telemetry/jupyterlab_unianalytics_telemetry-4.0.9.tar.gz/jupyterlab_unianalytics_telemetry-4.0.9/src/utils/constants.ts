const LOCAL_DEV = false;

export let BACKEND_API_URL: string, WEBSOCKET_API_URL: string;
if (LOCAL_DEV) {
  // LOCAL
  BACKEND_API_URL = 'http://localhost:80/send/';
  WEBSOCKET_API_URL = 'ws://localhost:1337/ws';

  // LOCAL W/ GATEWAY
  // BACKEND_API_URL = 'http://localhost:1015/send/';
  // WEBSOCKET_API_URL = 'ws://localhost:1015/ws';

  // TEST NOTO
  // BACKEND_API_URL = 'https://test-noto.epfl.ch/api/unilytics/send/';
  // WEBSOCKET_API_URL = 'ws://test-noto.epfl.ch/api/unilytics/ws';
} else {
  BACKEND_API_URL = 'https://api.unianalytics.ch/send/';
  WEBSOCKET_API_URL =
    'wss://ax5pzl8bwk.execute-api.eu-north-1.amazonaws.com/production/';
}

export const APP_ID = 'jupyterlab_unianalytics_telemetry';

export const MAX_PAYLOAD_SIZE = 1048576; // 1*1024*1024 => 1Mb

export const EXTENSION_SETTING_NAME = 'SendExtension';

// notebook metadata field names
const SELECTOR_ID = 'unianalytics';
export namespace Selectors {
  export const notebookId = `${SELECTOR_ID}_notebook_id`;

  export const cellMapping = `${SELECTOR_ID}_cell_mapping`;
}

export namespace CommandIDs {
  export const dashboardOpenChat = `${APP_ID}:unianalytics-open-chat`;
}
