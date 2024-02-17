import {
  ILabShell,
  ILayoutRestorer,
  JupyterFrontEndPlugin,
  JupyterFrontEnd
} from '@jupyterlab/application';
import { IFileBrowserFactory } from '@jupyterlab/filebrowser';
import { IRenderMimeRegistry } from '@jupyterlab/rendermime';
import { ISettingRegistry } from '@jupyterlab/settingregistry';

//importing bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  ACCESS_TOKEN_KEY,
  APP_ID,
  BACKEND_API_URL,
  PLUGIN_ID,
  REFRESH_TOKEN_KEY
} from './utils/constants';
import { compareVersions } from './utils/utils';
import { activateUploadNotebookPlugin } from './plugins/uploadNotebook';
import { activateDashboardPlugins } from './plugins/dashboards';
import { CompatibilityManager } from './utils/compatibility';
import { requestAPI } from './handler';

// to join to the Dashboard Interaction Data logging
export let CURRENT_NOTEBOOK_ID: string | null = null;
export function setCurrentNotebookId(id: string | null): void {
  CURRENT_NOTEBOOK_ID = id;
}

// persistent user id retrieved from the server-side extension
export let PERSISTENT_USER_ID: string | null = null;

const activate = (
  app: JupyterFrontEnd,
  factory: IFileBrowserFactory,
  restorer: ILayoutRestorer,
  labShell: ILabShell,
  rendermime: IRenderMimeRegistry,
  settingRegistry: ISettingRegistry
): void => {
  console.log(`JupyterLab extension ${APP_ID} is activated!`);

  const targetVersion = '3.1.0';
  const appNumbers = app.version.match(/[0-9]+/g);

  // request user id from server-side extension
  const requestUserId: Promise<string> = requestAPI<string>(
    'get_anonymized_user_id'
  );

  if (appNumbers && compareVersions(app.version, targetVersion) >= 0) {
    const jupyterVersion = parseInt(appNumbers[0]);

    CompatibilityManager.setJupyterVersion(jupyterVersion).then(() => {
      // access the promise response
      requestUserId
        .then(data => {
          PERSISTENT_USER_ID = data;

          let authNotebooks: string[] = [];
          // authenticate the user and only activate the plugins if the user is logged in
          fetch(`${BACKEND_API_URL}/auth/login`, {
            method: 'POST',
            headers: {
              'Unianalytics-User-Id': PERSISTENT_USER_ID
            }
          })
            .then(loginResponse => {
              if (loginResponse.ok) {
                return loginResponse.json();
              } else {
                throw new Error('Unauthorized user');
              }
            })
            .then(loginJSON => {
              if (loginJSON.status === 'logged_in') {
                // retrieve the list of authorized notebooks from the login response
                authNotebooks = loginJSON.auth_notebooks || [];

                // save the tokens
                sessionStorage.setItem(
                  ACCESS_TOKEN_KEY,
                  loginJSON.access_token
                );
                sessionStorage.setItem(
                  REFRESH_TOKEN_KEY,
                  loginJSON.refresh_token
                );

                activateUploadNotebookPlugin(app, factory);

                activateDashboardPlugins(
                  app,
                  restorer,
                  labShell,
                  settingRegistry,
                  rendermime
                );
              } else {
                console.log(`${APP_ID}: User not authenticated`);
              }
            })
            .catch(error => {
              console.log(`${APP_ID}: Authentication error, ${error}`);
            })
            .finally(() => {
              // emit message with the list of auth notebooks to retrieve and know which notebooks to disable in the telemetry extension
              window.postMessage(
                {
                  identifier: 'unianalytics',
                  authNotebooks: authNotebooks
                },
                window.origin
              );
            });
        })
        .catch(reason => {
          console.error(
            `${APP_ID}: Failed to access userId, the jupyterlab_unianalytics_dashboard server extension appears to be missing.\n${reason}`
          );
        });
    });
  } else {
    console.log(
      `${APP_ID}: Use a more recent version of JupyterLab (>=${targetVersion})`
    );
  }
};

const plugin: JupyterFrontEndPlugin<void> = {
  id: PLUGIN_ID,
  autoStart: true,
  requires: [
    IFileBrowserFactory,
    ILayoutRestorer,
    ILabShell,
    IRenderMimeRegistry,
    ISettingRegistry
  ],
  optional: [],
  activate: activate
};

export default plugin;
