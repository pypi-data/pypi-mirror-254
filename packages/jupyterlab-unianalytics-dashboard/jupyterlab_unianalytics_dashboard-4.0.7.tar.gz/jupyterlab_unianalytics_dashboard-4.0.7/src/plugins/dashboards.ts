import {
  ILabShell,
  ILayoutRestorer,
  JupyterFrontEnd
} from '@jupyterlab/application';
import { analyticsIcon } from '../icons';
import { APP_ID, visuIconClass, CommandIDs } from '../utils/constants';
import { store, AppDispatch } from '../redux/store';
import {
  navigateToNotebook,
  navigateToCell
} from '../redux/reducers/SideDashboardReducer';
import { NotebookPanel } from '@jupyterlab/notebook';
import { IRenderMimeRegistry } from '@jupyterlab/rendermime';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { PanelManager } from '../dashboard-widgets/PanelManager';
import { VisuDashboardPanel } from '../dashboard-widgets/VisuDashboardPanel';
import { TocDashboardPanel } from '../dashboard-widgets/TocDashboardPanel';
// import { ChatDashboardPanel } from '../dashboard-widgets/ChatDashboardPanel';
import { displayRealTime } from '../redux/reducers/CommonDashboardReducer';
import { InteractionRecorder } from '../utils/interactionRecorder';
import { DashboardClickOrigin } from '../utils/interfaces';
import { addDashboardNotebookExtensions } from '../widget-extensions';

const dispatch = store.dispatch as AppDispatch;

export async function activateDashboardPlugins(
  app: JupyterFrontEnd,
  restorer: ILayoutRestorer,
  labShell: ILabShell,
  settingRegistry: ISettingRegistry,
  rendermime: IRenderMimeRegistry
) {
  console.log(`JupyterLab extension ${APP_ID}: dashboard plugins activated!`);

  // load the necessary settings
  let settings: ISettingRegistry.ISettings | undefined;
  if (settingRegistry) {
    try {
      // load the toc settings
      settings = await settingRegistry.load(`${APP_ID}:plugin`);

      onSettingsChanged(settings);
      settings.changed.connect(onSettingsChanged);
    } catch (error) {
      console.error(`${APP_ID}: Failed to load settings.\n${error}`);
    }
  }

  // adds the multiple notebook buttons associated with the dashboards
  addDashboardNotebookExtensions(app);

  // define the object that will track the state of the current panel and expose it to the sidebar widgets
  const panelManager = new PanelManager();

  // initializing sidebar widgets
  const visuDashboardPanel = new VisuDashboardPanel(
    panelManager,
    rendermime.sanitizer
  );
  const tocDashboardPanel = new TocDashboardPanel(
    panelManager,
    app.commands,
    rendermime.sanitizer,
    settings
  );

  // const chatDashboardPanel = new ChatDashboardPanel(panelManager);

  // add the widgets to the sidebars
  labShell.add(visuDashboardPanel, 'right', { rank: 1000 });
  labShell.add(tocDashboardPanel, 'left', { rank: 1000 });
  // labShell.add(chatDashboardPanel, 'right', { rank: 1000 });

  // define commands to open the dashboards
  app.commands.addCommand(CommandIDs.dashboardOpenVisu, {
    label: 'Notebook Visualizations',
    // caption = hovering caption
    caption: 'Open Notebook Dashboard',
    icon: analyticsIcon,
    iconClass: visuIconClass,
    execute: args => {
      if (args['from'] === 'Notebook') {
        InteractionRecorder.sendInteraction({
          click_type: 'ON',
          signal_origin: DashboardClickOrigin.NOTEBOOK_TOOLBAR_BUTTON
        });
        dispatch(navigateToNotebook());
      } else if (args['from'] === 'Cell') {
        InteractionRecorder.sendInteraction({
          click_type: 'ON',
          signal_origin: DashboardClickOrigin.NOTEBOOK_CELL_BUTTON
        });
        dispatch(
          navigateToCell({
            cellId: args['cell_id'] as string
          })
        );
      } else if (args['from'] === 'Toc') {
        InteractionRecorder.sendInteraction({
          click_type: 'ON',
          signal_origin: DashboardClickOrigin.TOC_OPEN_CELL_DASHBOARD
        });
        dispatch(
          navigateToCell({
            cellId: args['cell_id'] as string
          })
        );
      }
      // else, keep the current navigationState

      // open the dashboard
      if (!visuDashboardPanel.isVisible) {
        app.shell.activateById(visuDashboardPanel.id);
      }
    }
  });

  // add the widgets to the restorer
  if (restorer) {
    restorer.add(visuDashboardPanel, `${APP_ID}:dashboard-notebook-restorer`);
    restorer.add(tocDashboardPanel, `${APP_ID}:dashboard-toc-restorer`);
    // restorer.add(chatDashboardPanel, `${APP_ID}:dashboard-chat-restorer`);
  }

  // update the panel when the active widget changes
  if (labShell) {
    labShell.currentChanged.connect(onConnect);
  }

  // connect to current widget
  void app.restored.then(() => {
    onConnect();
  });

  function onConnect() {
    const widget = app.shell.currentWidget;
    if (!widget) {
      return;
    }
    // only proceed if the new widget is a notebook panel
    if (!(widget instanceof NotebookPanel)) {
      // if the previously used widget is still available, stick with it.
      // otherwise, set the current panel to null.
      if (panelManager.panel && panelManager.panel.isDisposed) {
        panelManager.panel = null;
      }
      return;
    }
    const notebookPanel = widget as NotebookPanel;
    panelManager.panel = notebookPanel;
  }

  function onSettingsChanged(settings: ISettingRegistry.ISettings) {
    const commonDashboardSettings = settings.composite.commonDashboardSettings;
    let isRealTimeActivated;
    if (commonDashboardSettings) {
      isRealTimeActivated = (commonDashboardSettings as any).realTime;
      InteractionRecorder.setPermission(
        (commonDashboardSettings as any).dashboardCollection || false
      );
    } else {
      isRealTimeActivated = (settings.default('commonDashboardSettings') as any)
        ?.realTime;
      InteractionRecorder.setPermission(
        (settings.default('commonDashboardSettings') as any)
          ?.dashboardCollection || false
      );
    }

    if (isRealTimeActivated !== null || isRealTimeActivated !== undefined) {
      dispatch(displayRealTime(isRealTimeActivated));
    }
  }
}
