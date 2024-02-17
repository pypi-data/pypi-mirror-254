import React, { useEffect, useState } from 'react';
import { ChartData } from 'chart.js';
import { BACKEND_API_URL } from '../../../utils/constants';
import ChartContainer from './ChartContainer';
import { Bar } from 'react-chartjs-2';
import { codeExecOptions } from '../../../utils/chartOptions';
import { IChartProps } from '../../pages/Notebook';
import { useSelector } from 'react-redux';
import { RootState } from '../../../redux/store';
import { fetchWithCredentials } from '../../../utils/utils';

const CodeExecComponent = (props: IChartProps) => {
  const [codeExecData, setCodeExecData] = useState<ChartData<'bar'>>({
    labels: [],
    datasets: []
  });

  const displayRealTime = useSelector(
    (state: RootState) => state.commondashboard.displayRealTime
  );

  // fetching execution data
  useEffect(() => {
    fetchWithCredentials(
      `${BACKEND_API_URL}/dashboard/${props.notebookId}/user_code_execution?timeWindow=${props.timeWindow}&displayRealTime=${displayRealTime}`
    )
      .then(response => response.json())
      .then(data => {
        // filter elements of notebookCells that are of type 'code'
        const codeCells =
          props.notebookCells?.filter(cell => cell.cellType === 'code') || [];

        const chartData: ChartData<'bar'> = {
          labels: Array.from(
            { length: codeCells.length },
            (_, index) => index + 1
          ),
          datasets: [
            {
              label: 'clicks',
              data: Array(codeCells.length).fill(null),
              backgroundColor: 'rgba(51, 187, 238, 0.3)',
              borderColor: 'rgba(51, 187, 238, 0.3)',
              borderWidth: 1
            },
            {
              label: 'executions',
              data: Array(codeCells.length).fill(null),
              backgroundColor: 'rgba(0, 119, 187, 0.6)',
              borderColor: 'rgba(0, 119, 187, 0.6)',
              borderWidth: 1
            },
            {
              label: 'executions without errors',
              data: Array(codeCells.length).fill(null),
              backgroundColor: 'rgba(0, 153, 136, 0.9)',
              borderColor: 'rgba(0, 153, 136, 0.9)',
              borderWidth: 1
            }
          ]
        };

        // iterate through codeCells and find corresponding datasets from data
        codeCells.forEach((codeCell, index) => {
          const matchingData = data.find(
            (item: any) => item.cell === codeCell.id
          );
          if (matchingData) {
            chartData.datasets[0].data[index] = parseFloat(
              matchingData.cell_click_pct
            );
            chartData.datasets[1].data[index] = parseFloat(
              matchingData.code_exec_pct
            );
            chartData.datasets[2].data[index] = parseFloat(
              matchingData.code_exec_ok_pct
            );
          }
        });
        setCodeExecData(chartData);
      });
  }, [props.timeWindow, props.refreshRequired]);

  return (
    <ChartContainer
      PassedComponent={<Bar data={codeExecData} options={codeExecOptions} />}
      title="Code cell execution across users"
    />
  );
};

export default CodeExecComponent;
