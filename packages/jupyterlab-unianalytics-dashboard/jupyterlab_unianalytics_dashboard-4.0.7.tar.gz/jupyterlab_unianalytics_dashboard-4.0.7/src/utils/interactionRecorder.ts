import { BACKEND_API_URL } from './constants';
import { InteractionClick } from './interfaces';
import { CURRENT_NOTEBOOK_ID, PERSISTENT_USER_ID } from '..';

export class InteractionRecorder {
  private static _isInteractionRecordingEnabled = false;

  // this method is called in the dashboard plugin activation, which listens to setting updates
  static setPermission(value: boolean): void {
    InteractionRecorder._isInteractionRecordingEnabled = value;
  }

  static sendInteraction = (interactionData: InteractionClick): void => {
    if (InteractionRecorder._isInteractionRecordingEnabled) {
      // send data
      fetch(`${BACKEND_API_URL}/dashboard_interaction/add`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          ...interactionData,
          dashboard_user_id: PERSISTENT_USER_ID,
          time: new Date().toISOString(),
          notebook_id: CURRENT_NOTEBOOK_ID
        })
      });
      // .then(response => {});
    }
  };
}
