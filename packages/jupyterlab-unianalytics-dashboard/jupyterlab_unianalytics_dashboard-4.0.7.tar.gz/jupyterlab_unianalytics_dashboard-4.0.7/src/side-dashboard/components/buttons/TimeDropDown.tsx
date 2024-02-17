import React from 'react';
import { DropdownButton, Dropdown } from 'react-bootstrap';
import { CalendarWeek as TimeLogo } from 'react-bootstrap-icons';
import { store, AppDispatch } from '../../../redux/store';
import { setTimeWindow } from '../../../redux/reducers/CommonDashboardReducer';
import { InteractionRecorder } from '../../../utils/interactionRecorder';
import { DashboardClickOrigin } from '../../../utils/interfaces';

const dispatch = store.dispatch as AppDispatch;

const TimeDropDown = (): JSX.Element => {
  return (
    <DropdownButton
      id="time-window-dropdown"
      title={<TimeLogo className="logo" />}
      variant="outline-secondary"
      onSelect={eventKey => {
        if (eventKey) {
          InteractionRecorder.sendInteraction({
            click_type: 'ON',
            signal_origin: DashboardClickOrigin.DASHBOARD_FILTER_TIME
          });
          dispatch(setTimeWindow(eventKey));
        }
      }}
      className="custom-dropdown"
    >
      <Dropdown.Header>Data to keep</Dropdown.Header>
      <Dropdown.Divider />
      <Dropdown.Item eventKey="60">Last minute</Dropdown.Item>
      <Dropdown.Item eventKey="600">Last 10 minutes</Dropdown.Item>
      <Dropdown.Item eventKey="3600">Last hour</Dropdown.Item>
      <Dropdown.Item eventKey="86400">Last day</Dropdown.Item>
      <Dropdown.Item eventKey="604800">Last week</Dropdown.Item>
      <Dropdown.Item eventKey="2592000">Last month</Dropdown.Item>
      <Dropdown.Item eventKey="15768000">Last 6 months</Dropdown.Item>
      <Dropdown.Item eventKey="null">All</Dropdown.Item>
    </DropdownButton>
  );
};

export default TimeDropDown;
