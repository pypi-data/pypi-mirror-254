# Changelog

<!-- <START NEW CHANGELOG ENTRY> -->

## 4.0.7

- Feature: adding text-based filtering in Cell dashboard
- Adding server extension component
- Generating or retrieving persistent user identifier
- Small bug fixes

<!-- <END NEW CHANGELOG ENTRY> -->

## 4.0.6

Fixed incompatibility with JupyterLab 3.

## 4.0.5

Changes since last release:

- Bug fixes
- Dashboard usage data collection
- Export notebook data to CSV
- Removing cell list check for robustness to cell list incompatibility
- Cleaning up redux store
- Emit authorized notebooks for telemetry extension to catch to avoid displaying your own data in the dashboard.
- Switching to JWT authentication
- Handling token refresh

## 4.0.4

No merged PRs

## 4.0.3

- Smoother Cell dashboard refresh
- Reading userId for authentication

## 4.0.2

Changing package name

## 4.0.1

Major changes :

- Adding websocket connection
- Refresh request over websocket sent by backend to enable real-time visualization
- Cleaning code
- Adding CompatibilityManager and making the extension compatible with JupyterLab 3
- Adding PanelManager to run the notebook checks and share the checks between all sidebar widgets
- Adding DashboardPanel abstract parent class to define shared logic between Right and Left dashboards

## 4.0.0

First release through the releaser. The extension was seeded with a template for JupyterLab 4.x.

New features :

- Including markdown executions to the dashboard using JupyterLab API
- Clicking on the TOC dashboard tile opens the corresponding cell dashboard
- Time filter is shared between both dashboard
- Refresh is shared between both dashboard
- Re-rendering is made smoother by not reloading the charts completely
