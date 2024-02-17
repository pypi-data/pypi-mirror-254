import { JupyterFrontEnd, LabShell } from '@jupyterlab/application';
import { APP_ID } from './utils/constants';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { PanelManager } from './PanelManager';
import { NotebookPanel } from '@jupyterlab/notebook';

export const dataCollectionPlugin = async (
  app: JupyterFrontEnd,
  settingRegistry: ISettingRegistry
) => {
  // to record duration of code executions, enable the recording of execution timing (JupyterLab default setting)
  settingRegistry
    .load('@jupyterlab/notebook-extension:tracker')
    .then((nbTrackerSettings: ISettingRegistry.ISettings) => {
      nbTrackerSettings.set('recordTiming', true);
    })
    .catch(error =>
      console.log(
        `${APP_ID}: Could not force cell execution metadata recording: ${error}`
      )
    );

  try {
    // wait for this extension's settings to load
    const [settings, dialogShownSettings] = await Promise.all([
      settingRegistry.load(`${APP_ID}:settings`),
      settingRegistry.load(`${APP_ID}:dialogShownSettings`)
    ]);

    const panelManager = new PanelManager(settings, dialogShownSettings);

    const labShell = app.shell as LabShell;

    // update the panel when the active widget changes
    if (labShell) {
      labShell.currentChanged.connect(() => onConnect(labShell, panelManager));
    }

    // connect to current widget
    void app.restored.then(() => {
      onConnect(labShell, panelManager);
    });
  } catch (error) {
    console.log(`${APP_ID}: Could not load settings, error: ${error}`);
  }
};

function onConnect(labShell: LabShell, panelManager: PanelManager) {
  const widget = labShell.currentWidget;
  if (!widget) {
    return;
  }

  if (widget instanceof NotebookPanel) {
    const notebookPanel = widget as NotebookPanel;
    panelManager.panel = notebookPanel;
  } else {
    panelManager.panel = null;
  }
}
