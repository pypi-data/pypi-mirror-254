import React, { useState, useEffect, useRef } from 'react';
import {
  Row,
  Col,
  Card,
  Form,
  ToggleButton,
  ButtonGroup
} from 'react-bootstrap';
import { BACKEND_API_URL } from '../../utils/constants';

import { useSelector } from 'react-redux';
import { RootState } from '../../redux/store';
import { CellLayer } from '../../redux/types';
import CellOutput from '../components/cell/CellOutput';
import CellInput from '../components/cell/CellInput';
import TimeDropDown from '../components/buttons/TimeDropDown';
import SortDropDown from '../components/buttons/SortDropDown';

import MarkdownComponent from '../components/cell/MarkdownComponent';
import { IRenderMime } from '@jupyterlab/rendermime';
import { InteractionRecorder } from '../../utils/interactionRecorder';
import { DashboardClickOrigin } from '../../utils/interfaces';
import { fetchWithCredentials } from '../../utils/utils';

interface ICellPageProps {
  notebookId: string;
  sanitizer: IRenderMime.ISanitizer;
}

// function to wait for a small delay before updating the value of the filter box input state value
const useSearchDebounce = (
  delay = 800
): [string, React.Dispatch<React.SetStateAction<string>>] => {
  const [search, setSearch] = useState<string>('');
  const [searchQuery, setSearchQuery] = useState<string>('');

  useEffect(() => {
    const delayFn = setTimeout(() => setSearch(searchQuery), delay);
    return () => clearTimeout(delayFn);
  }, [searchQuery, delay]);

  return [search, setSearchQuery];
};

const Cell = (props: ICellPageProps): JSX.Element => {
  const originalData = useRef([]);
  const [renderedData, setRenderedData] = useState([]);

  // declaring a 2nd boolean since state updates are async, which wouldn't be quick enough for the 2nd useEffect check
  let isAlreadyFetching = false;

  const navigationState = useSelector(
    (state: RootState) => state.sidedashboard.navigationState
  );
  const timeWindow = useSelector(
    (state: RootState) => state.commondashboard.timeWindow
  );
  const refreshRequired = useSelector(
    (state: RootState) => state.commondashboard.refreshBoolean
  );
  const displayRealTime = useSelector(
    (state: RootState) => state.commondashboard.displayRealTime
  );

  // filter header content

  const [showInputs, setShowInputs] = useState<boolean>(true);
  const [showOutputs, setShowOutputs] = useState<boolean>(true);

  const [radioValue, setRadioValue] = useState<number>(1);

  const [inputFilterText, setInputFilterText] = useSearchDebounce();

  const executionFilters = [
    { name: 'All', value: 1, status: 'all' },
    { name: 'Success', value: 2, status: 'ok' },
    { name: 'Error', value: 3, status: 'error' }
  ];
  const filterStatus = executionFilters.map(filter => filter.status);

  const [orderBy, setOrderBy] = useState<string>('timeDesc'); // timeDesc (default), timeAsc, inputDesc, inputAsc, outputDesc, outputAsc

  // sorting

  const orderAndSetData = (data: any): void => {
    // filter the data based on the input value
    const searchTerm = inputFilterText.toLowerCase();

    if (searchTerm.length > 0) {
      data = data.filter((item: any) => {
        return (
          item.cell_input?.toLowerCase().includes(searchTerm) ||
          (item.cell_output_model &&
            JSON.stringify(item.cell_output_model)
              .toLowerCase()
              .includes(searchTerm))
        );
      });
    }

    // sort the data according to the selected criterion
    data.sort((a: any, b: any) => {
      switch (orderBy) {
        case 'timeDesc':
          return new Date(a.t_finish) < new Date(b.t_finish) ? 1 : -1;
        case 'timeAsc':
          return new Date(a.t_finish) > new Date(b.t_finish) ? 1 : -1;
        case 'inputAsc':
          return a.cell_input.length - b.cell_input.length;
        case 'inputDesc':
          return b.cell_input.length - a.cell_input.length;
        case 'outputAsc':
          return a.cell_output_length - b.cell_output_length;
        case 'outputDesc':
          return b.cell_output_length - a.cell_output_length;
        default:
          return 0;
      }
    });
    setRenderedData(data);
  };

  // fetching

  const content = (navigationState[navigationState.length - 1] as CellLayer)
    .content;

  useEffect(() => {
    isAlreadyFetching = true;
    fetchWithCredentials(
      `${BACKEND_API_URL}/dashboard/${props.notebookId}/cell/${content.cellId}?timeWindow=${timeWindow}&displayRealTime=${displayRealTime}`
    )
      .then(response => response.json())
      .then(data => {
        originalData.current = data;
        orderAndSetData(data);
        isAlreadyFetching = false;
      });
  }, [navigationState, timeWindow, refreshRequired]);

  useEffect(() => {
    if (!isAlreadyFetching) {
      // to avoid sorting twice upon first render
      const data = [...originalData.current];
      orderAndSetData(data);
    }
  }, [orderBy, inputFilterText]);

  return (
    <>
      <div className="dashboard-title-container">
        <div className="dashboard-title-text">Cell ({content.cellId})</div>
        <div className="dashboard-dropdown-container">
          <SortDropDown setOrderBy={setOrderBy} />
          <TimeDropDown />
        </div>
      </div>
      {/* Filter Bar */}
      <Form className="cell-filter-container">
        <div className="cell-radio-container">
          <ButtonGroup size="sm">
            <ToggleButton
              style={{ marginRight: '3px' }}
              key="0"
              id="code-checkbox"
              type="radio"
              variant="outline-primary"
              // name="radio"
              value="Code"
              checked={showInputs}
              onClick={event => {
                if (showInputs && !showOutputs) {
                  // Prevent unchecking both checkboxes
                  event.preventDefault();
                } else {
                  InteractionRecorder.sendInteraction({
                    click_type: showInputs ? 'OFF' : 'ON',
                    signal_origin:
                      DashboardClickOrigin.CELL_DASHBOARD_FILTER_CODE_INPUT
                  });
                  setShowInputs(!showInputs);
                }
              }}
            >
              Code
            </ToggleButton>
            <ToggleButton
              key="1"
              id="output-checkbox"
              type="radio"
              variant="outline-primary"
              // name="radio"
              value="Output"
              checked={showOutputs}
              onClick={event => {
                if (!showInputs && showOutputs) {
                  // Prevent unchecking both checkboxes
                  event.preventDefault();
                } else {
                  InteractionRecorder.sendInteraction({
                    click_type: showOutputs ? 'OFF' : 'ON',
                    signal_origin:
                      DashboardClickOrigin.CELL_DASHBOARD_FILTER_CODE_OUTPUT
                  });
                  setShowOutputs(!showOutputs);
                }
              }}
            >
              Output
            </ToggleButton>
          </ButtonGroup>
        </div>
        <div className="cell-radio-container">
          <ButtonGroup size="sm">
            {executionFilters.map((execFilter, idx) => (
              <ToggleButton
                key={idx}
                id={`filter-${idx}`}
                type="radio"
                variant="outline-primary"
                name="radio"
                value={execFilter.value}
                checked={radioValue === execFilter.value}
                onChange={e => {
                  InteractionRecorder.sendInteraction({
                    click_type: 'ON',
                    signal_origin:
                      DashboardClickOrigin.CELL_DASHBOARD_FILTER_EXECUTION
                  });
                  setRadioValue(Number(e.currentTarget.value));
                }}
              >
                {execFilter.name}
              </ToggleButton>
            ))}
          </ButtonGroup>
        </div>
        <Form.Control
          size="sm"
          type="text"
          placeholder="Type text to filter..."
          onChange={e => setInputFilterText(e.target.value)}
        />
      </Form>
      <>
        {/* Cell Executions */}
        {renderedData.map((value: { [key: string]: any }, index: number) => {
          return (
            <Row key={index}>
              {/* for markdown executions, consider that the execution status is 'ok', not an error */}
              {value.cell_type === 'MarkdownExecution' &&
              ['all', 'ok'].includes(filterStatus[radioValue - 1]) ? (
                <Col md={12}>
                  <Card className="cell-card">
                    <Card.Body style={{ gap: '10px' }}>
                      <Row className="cell-card-wrapper">
                        <Col md={12} className="cell-user-title">
                          <Card.Text>User {index + 1}</Card.Text>
                        </Col>
                        <Col md={12}>
                          <MarkdownComponent
                            markdownContent={value.cell_input}
                            sanitizer={props.sanitizer}
                          />
                        </Col>
                      </Row>
                    </Card.Body>
                  </Card>
                </Col>
              ) : (
                <>
                  {(radioValue === 1 ||
                    filterStatus[radioValue - 1] === value.status) && (
                    <Col md={12}>
                      <Card className="cell-card">
                        <Card.Body style={{ gap: '10px' }}>
                          <Row className="cell-card-wrapper">
                            <Col md={12} className="cell-user-title">
                              <Card.Text>User {index + 1}</Card.Text>
                            </Col>
                            <Col md={12}>
                              {showInputs && (
                                <CellInput
                                  cell_input={value.cell_input}
                                  language_mimetype={value.language_mimetype}
                                  className="cell-content-container"
                                />
                              )}
                              {showInputs &&
                                showOutputs &&
                                value.cell_output_model.length > 0 && <br />}
                              {showOutputs &&
                                value.cell_output_model.length > 0 && (
                                  <CellOutput
                                    cell_output_model={value.cell_output_model}
                                  />
                                )}
                            </Col>
                          </Row>
                        </Card.Body>
                      </Card>
                    </Col>
                  )}
                </>
              )}
            </Row>
          );
        })}
      </>
    </>
  );
};

export default Cell;
