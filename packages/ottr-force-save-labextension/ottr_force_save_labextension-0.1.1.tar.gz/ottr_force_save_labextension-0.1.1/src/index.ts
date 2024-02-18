import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { INotebookTracker } from '@jupyterlab/notebook';

/**
 * Initialization data for the ottr-force-save-labextension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'ottr-force-save-labextension:plugin',
  description:
    'A JupyterLab extension for force-saving notebooks from ottr, the Otter-Grader R client.',
  autoStart: true,
  requires: [INotebookTracker],
  activate: async (app: JupyterFrontEnd, tracker: INotebookTracker) => {
    Object.assign(window, {
      __ottr_force_save_labextension_force_save: () => {
        tracker.currentWidget?.context
          .save()
          .then(() => console.log('Notebook saved by ottr-force-save-labextension'))
          .catch((e: Error) => console.error(`ottr force-save failed: ${e}`));
      },
    });
  },
};

export default plugin;
