import React from 'react';
import { Stack, Button } from 'react-bootstrap';

import { useSelector } from 'react-redux';
import { RootState } from '../../../redux/store';
import { store, AppDispatch } from '../../../redux/store';
import { navigateToHistory } from '../../../redux/reducers/SideDashboardReducer';
import { refreshDashboards } from '../../../redux/reducers/CommonDashboardReducer';
import { refreshIcon } from '@jupyterlab/ui-components';
import { InteractionRecorder } from '../../../utils/interactionRecorder';
import { DashboardClickOrigin } from '../../../utils/interfaces';

const dispatch = store.dispatch as AppDispatch;

const TopBreadcrumb = (): JSX.Element => {
  const navigationState = useSelector(
    (state: RootState) => state.sidedashboard.navigationState
  );

  return (
    <Stack className="breadcrumb-container" direction="horizontal" gap={2}>
      {navigationState.map((value: any, index: number) => {
        return (
          <div
            className={
              index === navigationState.length - 1
                ? 'breadcrumb-tile-active breadcrumb-tile'
                : 'breadcrumb-tile'
            }
            onClick={() => {
              if (value.pageName === 'Notebook') {
                InteractionRecorder.sendInteraction({
                  click_type: 'ON',
                  signal_origin: DashboardClickOrigin.BREADCRUMB_TO_NOTEBOOK
                });
              } else if (value.pageName === 'Cell') {
                InteractionRecorder.sendInteraction({
                  click_type: 'ON',
                  signal_origin: DashboardClickOrigin.BREADCRUMB_TO_CELL
                });
              }
              // only change if actually going to a previous page
              if (index !== navigationState.length - 1) {
                // cut until page of interest since the last page will be loaded
                dispatch(navigateToHistory(index));
              }
            }}
          >
            {value.pageName}
          </div>
        );
      })}

      <div className="breadcrumb-buttons-container">
        <Button
          className="breadcrumb-button"
          onClick={() => {
            InteractionRecorder.sendInteraction({
              click_type: 'ON',
              signal_origin: DashboardClickOrigin.DASHBOARD_REFRESH_BUTTON
            });
            dispatch(refreshDashboards());
          }}
        >
          <refreshIcon.react elementSize="large" className="labicon-logo" />
        </Button>
      </div>
    </Stack>
  );
};

export default TopBreadcrumb;
