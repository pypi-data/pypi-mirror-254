import React, { useEffect, useRef, useState } from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../redux/store';
import { NotebookPanel } from '@jupyterlab/notebook';
import { INotebookHeading } from '../utils/headings';
import { TocDashboardItem } from './tocDashboardItem';
import { ItemRenderer } from '../utils/interfaces';
import { APP_ID, BACKEND_API_URL, Selectors } from '../utils/constants';
import { LocationData } from '../utils/interfaces';
import { CommandRegistry } from '@lumino/commands';
import { CompatibilityManager } from '../utils/compatibility';
import { fetchWithCredentials } from '../utils/utils';

interface ITOCTreeProps {
  headings: INotebookHeading[];
  itemRenderer: ItemRenderer;
  notebookPanel: NotebookPanel;
  commands: CommandRegistry;
  notebookCells: string[] | null | undefined;
}

const TocDashboardTree: React.FC<ITOCTreeProps> = props => {
  const [locationData, setLocationData] = useState<LocationData>(null);

  const shouldDisplayDashboardRedux = useSelector(
    (state: RootState) => state.tocdashboard.displayDashboard
  );
  const refreshRequired = useSelector(
    (state: RootState) => state.commondashboard.refreshBoolean
  );
  const timeWindow = useSelector(
    (state: RootState) => state.commondashboard.timeWindow
  );
  const displayRealTime = useSelector(
    (state: RootState) => state.commondashboard.displayRealTime
  );

  // only fetch again when the list of cells actually changed
  useEffect(() => {
    fetchToCData();
    // callback to reset the locationData
    return () => {
      setLocationData(null);
    };
  }, [props.notebookCells, props.notebookPanel]);

  //  or when a refresh is requested (for smoother refresh, don't reset locationData here)
  useEffect(() => {
    fetchToCData();
  }, [refreshRequired, timeWindow]);

  // id to make sure only the last request resolves
  const currentRequestId = useRef<string>('12345678');
  const fetchToCData = async (): Promise<void> => {
    const notebookId = CompatibilityManager.getMetadataComp(
      props.notebookPanel.model,
      Selectors.notebookId
    );
    // only fetch if there is a notebook id, and there are cells
    if (!notebookId || !props.notebookCells) {
      return;
    }
    try {
      const newRequestId = crypto.randomUUID();
      currentRequestId.current = newRequestId;

      const response = await fetchWithCredentials(
        `${BACKEND_API_URL}/dashboard/${notebookId}/toc?timeWindow=${timeWindow}&displayRealTime=${displayRealTime}`
      );

      // check that it's the response from the current request and not a subsequent
      if (newRequestId === currentRequestId.current) {
        if (response.ok) {
          const data = await response.json();
          setLocationData(data.data);
          return;
        } else {
          console.log(`${APP_ID}: Error:`, response.status);
        }
      }
    } catch (error) {
      console.log(`${APP_ID}: Toc Fetch Error:`, error);
    }
    // if it didn't fetch, set the fetched data to null
    setLocationData(null);
  };

  const aggregateCollapsedData = (
    value: LocationData
  ): { [key: string]: number } => {
    const uncollapsedIds: string[] = props.headings.map(
      heading => heading.cellRef.model.id
    );
    const uniqueUncollapsedIds: string[] = [...new Set(uncollapsedIds)];

    const dict: { [key: string]: number } = {};
    const cells = props.notebookCells;
    if (cells && value) {
      // a list of indices between which data should be aggregated
      const mapping: number[] = uniqueUncollapsedIds.map(id =>
        cells.indexOf(id)
      );

      // adapt the boundaries
      mapping[0] = 0;
      mapping.push(cells.length);

      let total_count = 0;
      for (let i = 0; i < uniqueUncollapsedIds.length; i++) {
        const start = mapping[i];
        const end = mapping[i + 1];
        let total = 0;
        if (start === -1) {
          // not found
          total = 0;
        } else {
          for (let j = start; j < end; j++) {
            total += value.location_count[cells[j]] || 0;
          }
        }
        dict[uniqueUncollapsedIds[i]] = total;
        total_count += total;
      }

      dict['total_count'] = total_count;
    }

    return dict;
  };

  // on every re-render, aggregate locationData from collapsed headings
  const aggregatedData = aggregateCollapsedData(locationData);

  const renderedCells = new Set<string>();
  return (
    <ul className="dashboard-TableOfContents-content">
      {props.headings.map((el, index) => {
        const cellId = el.cellRef.model.id;
        const isFirstCellOccurrence = !renderedCells.has(cellId);

        if (isFirstCellOccurrence) {
          renderedCells.add(cellId);
        }
        return (
          <TocDashboardItem
            panel={props.notebookPanel}
            heading={el}
            headings={props.headings}
            itemRenderer={props.itemRenderer}
            // only display the dashboard component when not disabled with redux, when it's the first cell occurrence
            addReactComponent={shouldDisplayDashboardRedux}
            isFirstCellOccurrence={isFirstCellOccurrence}
            tocDashboardData={[
              aggregatedData[cellId],
              aggregatedData['total_count']
            ]}
            commands={props.commands}
            key={`${el.text}-${el.level}-${index++}`}
          />
        );
      })}
    </ul>
  );
};

export default TocDashboardTree;
