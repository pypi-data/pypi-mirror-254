import React, { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import { refreshIcon, runIcon } from '@jupyterlab/ui-components';
import { BACKEND_API_URL } from '../utils/constants';
import ConnectionComponent from './ConnectionComponent';
import { fetchWithCredentials } from '../utils/utils';

const ChatContainer = (props: { notebookId: string }) => {
  const [connectedUsers, setConnectedUsers] = useState<string[]>([]);
  const [selectedUser, setSelectedUser] = useState<string | null>(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    requestConnectedUsers();
  }, []);

  const requestConnectedUsers = async () => {
    const response = await fetchWithCredentials(
      `${BACKEND_API_URL}/dashboard/${props.notebookId}/connectedstudents`
    );

    if (response.ok) {
      const connectedUsers = await response.json();
      if (connectedUsers) {
        setConnectedUsers(connectedUsers);
        return;
      }
    }
    setConnectedUsers([]);
  };

  const sendMessage = (userId: string) => {
    if (message) {
      fetchWithCredentials(
        `${BACKEND_API_URL}/dashboard/${props.notebookId}/sendtouser/${userId}`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ message: message })
        }
      ).then();
    }
    setMessage('');
  };

  return (
    <div style={{ width: '100%', padding: '15px' }}>
      <div style={{ display: 'flex', width: '100%', paddingBottom: '15px' }}>
        <div style={{ color: 'white', fontSize: '20px', fontWeight: '500' }}>
          Chat with Users
        </div>
        <div className="breadcrumb-buttons-container">
          <Button
            className="breadcrumb-button"
            onClick={() => requestConnectedUsers()}
          >
            <refreshIcon.react elementSize="large" className="labicon-logo" />
          </Button>
        </div>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', flex: '1' }}>
        <div style={{ width: '100%', maxHeight: '50%', overflowY: 'auto' }}>
          {connectedUsers.map((userId: string) => (
            <ConnectionComponent
              connectionId={userId}
              onClick={() => setSelectedUser(userId)}
            />
          ))}
        </div>
        <div style={{ width: '100%', overflowY: 'auto' }}>
          {selectedUser && (
            <div
              style={{
                height: '50%',
                borderTop: 'solid 1px white',
                paddingTop: '10px'
              }}
            >
              <div
                style={{
                  color: 'white',
                  padding: '5px 0 15px 0',
                  fontWeight: '400'
                }}
                className="text-with-ellipsis"
              >
                Chat with {selectedUser}
              </div>
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  border: '1px solid white',
                  borderRadius: '2px',
                  padding: '2px 0 2px 3px'
                }}
              >
                <input
                  type="text"
                  placeholder="Send a chat..."
                  value={message}
                  onChange={e => setMessage(e.target.value)}
                  style={{
                    flex: 1,
                    color: 'white',
                    fontSize: '14px',
                    background: 'transparent',
                    border: 'none',
                    borderRight: '1px solid white',
                    outline: 'none'
                  }}
                />
                <button
                  onClick={() => sendMessage(selectedUser)}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    cursor: 'pointer'
                  }}
                >
                  <runIcon.react elementSize="large" className="send-icon" />
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ChatContainer;
