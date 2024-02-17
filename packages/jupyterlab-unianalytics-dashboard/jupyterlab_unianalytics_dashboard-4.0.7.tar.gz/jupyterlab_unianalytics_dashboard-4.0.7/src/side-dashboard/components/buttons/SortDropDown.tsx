import React, { Dispatch, SetStateAction } from 'react';
import { DropdownButton, Dropdown } from 'react-bootstrap';
import { SortUp as SortLogo } from 'react-bootstrap-icons';
import { InteractionRecorder } from '../../../utils/interactionRecorder';
import { DashboardClickOrigin } from '../../../utils/interfaces';

const SortDropDown = ({
  setOrderBy
}: {
  setOrderBy: Dispatch<SetStateAction<string>>;
}): JSX.Element => {
  return (
    <DropdownButton
      id="order-by-dropdown"
      title={<SortLogo className="logo" />}
      variant="outline-secondary"
      onSelect={eventKey => {
        if (eventKey) {
          InteractionRecorder.sendInteraction({
            click_type: 'ON',
            signal_origin: DashboardClickOrigin.CELL_DASHBOARD_FILTER_SORT
          });
          setOrderBy(eventKey);
        }
      }}
      className="custom-dropdown"
    >
      <Dropdown.Header>Sort cells by</Dropdown.Header>
      <Dropdown.Divider />
      <Dropdown.Item eventKey="timeDesc">Time (most recent 1st)</Dropdown.Item>
      <Dropdown.Item eventKey="timeAsc">Time (oldest 1st)</Dropdown.Item>
      <Dropdown.Item eventKey="inputAsc">Input (shortest 1st)</Dropdown.Item>
      <Dropdown.Item eventKey="inputDesc">Input (longest 1st)</Dropdown.Item>
      <Dropdown.Item eventKey="outputAsc">Output (shortest 1st)</Dropdown.Item>
      <Dropdown.Item eventKey="outputDesc">Output (longest 1st)</Dropdown.Item>
    </DropdownButton>
  );
};

export default SortDropDown;
