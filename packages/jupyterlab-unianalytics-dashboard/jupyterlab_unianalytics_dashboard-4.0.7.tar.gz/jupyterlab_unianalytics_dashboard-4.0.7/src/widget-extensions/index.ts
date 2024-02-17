import { JupyterFrontEnd } from '@jupyterlab/application';
import { CellButton } from './CellButton';
import { NotebookButton } from './NotebookButton';
import { NotebookPanel } from '@jupyterlab/notebook';
import { CompatibilityManager } from '../utils/compatibility';

// function that adds the multiple notebook buttons associated with the dashboards
export const addDashboardNotebookExtensions = (app: JupyterFrontEnd): void => {
  // since the plugin activation is async, some notebooks might have already been created without the buttons
  const widgetIterator = app.shell.widgets();
  // app.shell.widgets().next() returns a different Iterator between JupyterLab 3 and 4
  let nextWidget = CompatibilityManager.getNextWidgetValueComp(widgetIterator);
  while (nextWidget) {
    if (nextWidget instanceof NotebookPanel) {
      const panel = nextWidget as NotebookPanel;
      const notebookButton = new NotebookButton(app.commands);
      const cellButton = new CellButton(app.commands);

      const notebookButtonDisposable = notebookButton.createNew(panel);
      const cellButtonDisposable = cellButton.createNew(panel);

      panel.disposed.connect(() => {
        notebookButtonDisposable.dispose();
        cellButtonDisposable.dispose();
      });
    }
    nextWidget = CompatibilityManager.getNextWidgetValueComp(widgetIterator);
  }

  // add notebook cell button to future notebooks
  app.docRegistry.addWidgetExtension('Notebook', new CellButton(app.commands));

  // add notebook toolbar button to future notebooks
  app.docRegistry.addWidgetExtension(
    'Notebook',
    new NotebookButton(app.commands)
  );
};
